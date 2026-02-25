import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
import glm
import numpy as np
import time

from shader import Shader
from camera import Camera
from world import world
from client import Client

WIDTH = 1000
HEIGHT = 700

cube_vertices = [
    -0.5,-0.5,-0.5,
     0.5,-0.5,-0.5,
     0.5, 0.5,-0.5,
    -0.5, 0.5,-0.5,
]

indices = [0,1,2, 2,3,0]

def main():

    glfw.init()
    glutInit()

    window = glfw.create_window(WIDTH, HEIGHT, "The Cube OpenGL", None, None)
    glfw.make_context_current(window)

    glEnable(GL_DEPTH_TEST)

    shader = Shader("shaders/vertex.glsl", "shaders/fragment.glsl")

    vertices = np.array(cube_vertices, dtype=np.float32)
    inds = np.array(indices, dtype=np.uint32)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    EBO = glGenBuffers(1)

    glBindVertexArray(VAO)

    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, inds.nbytes, inds, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3*4, None)
    glEnableVertexAttribArray(0)

    camera = Camera()
    
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 5000

    client = Client(SERVER_IP, SERVER_PORT)

    chat_mode = False
    chat_input = ""

    last_time = time.time()

    while not glfw.window_should_close(window):

        current = time.time()
        delta = current - last_time
        last_time = current

        glfw.poll_events()

        speed = camera.speed * delta

        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            camera.position += camera.front * speed
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            camera.position -= camera.front * speed

        client.send({
            "type": "move",
            "pos": [camera.position.x,
                    camera.position.y,
                    camera.position.z]
        })

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        shader.use()

        projection = glm.perspective(glm.radians(70), WIDTH/HEIGHT, 0.1, 100)
        view = camera.get_view_matrix()

        shader.set_mat4("projection", projection)
        shader.set_mat4("view", view)

        glBindVertexArray(VAO)

        # Monde
        for pos in world:
            model = glm.translate(glm.mat4(1.0), glm.vec3(*pos))
            shader.set_mat4("model", model)
            glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        # Joueurs
        for p in client.players.values():
            model = glm.translate(glm.mat4(1.0), glm.vec3(*p["pos"]))
            shader.set_mat4("model", model)
            glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()