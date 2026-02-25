import glfw
from OpenGL.GL import *
import glm
import numpy as np
import time
import math

from shader import Shader
from camera import Camera

WIDTH = 1280
HEIGHT = 720

# ===== MONDE =====
blocks = {}

# Génère un sol
for x in range(-10, 11):
    for z in range(-10, 11):
        blocks[(x, 0, z)] = True


# ===== CUBE DATA =====
cube_vertices = np.array([
    -0.5,-0.5,-0.5,  0.5,-0.5,-0.5,  0.5, 0.5,-0.5,
     0.5, 0.5,-0.5, -0.5, 0.5,-0.5, -0.5,-0.5,-0.5,

    -0.5,-0.5, 0.5,  0.5,-0.5, 0.5,  0.5, 0.5, 0.5,
     0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5,-0.5, 0.5,

    -0.5, 0.5, 0.5, -0.5, 0.5,-0.5, -0.5,-0.5,-0.5,
    -0.5,-0.5,-0.5, -0.5,-0.5, 0.5, -0.5, 0.5, 0.5,

     0.5, 0.5, 0.5,  0.5, 0.5,-0.5,  0.5,-0.5,-0.5,
     0.5,-0.5,-0.5,  0.5,-0.5, 0.5,  0.5, 0.5, 0.5,

    -0.5,-0.5,-0.5,  0.5,-0.5,-0.5,  0.5,-0.5, 0.5,
     0.5,-0.5, 0.5, -0.5,-0.5, 0.5, -0.5,-0.5,-0.5,

    -0.5, 0.5,-0.5,  0.5, 0.5,-0.5,  0.5, 0.5, 0.5,
     0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5,-0.5,
], dtype=np.float32)


def raycast(camera, max_distance=6):
    step = 0.1
    pos = glm.vec3(camera.position)

    for i in range(int(max_distance / step)):
        pos += camera.front * step
        block_pos = (round(pos.x), round(pos.y), round(pos.z))
        if block_pos in blocks:
            return block_pos
    return None


def main():
    glfw.init()
    window = glfw.create_window(WIDTH, HEIGHT, "Minecraft Python", None, None)
    glfw.make_context_current(window)
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

    glEnable(GL_DEPTH_TEST)

    shader = Shader("vertex.glsl", "fragment.glsl")
    camera = Camera(WIDTH, HEIGHT)

    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, cube_vertices.nbytes, cube_vertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, None)
    glEnableVertexAttribArray(0)

    last_time = time.time()
    frames = 0

    while not glfw.window_should_close(window):

        # FPS
        current = time.time()
        frames += 1
        if current - last_time >= 1:
            glfw.set_window_title(window, f"FPS: {frames}")
            frames = 0
            last_time = current

        glfw.poll_events()
        camera.process_input(window)

        # ===== CLIC GAUCHE : casser =====
        if glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
            hit = raycast(camera)
            if hit:
                del blocks[hit]

        # ===== CLIC DROIT : poser =====
        if glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_RIGHT) == glfw.PRESS:
            hit = raycast(camera)
            if hit:
                place_pos = glm.vec3(hit) + glm.round(camera.front)
                blocks[(int(place_pos.x), int(place_pos.y), int(place_pos.z))] = True

        glClearColor(0.5, 0.7, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        shader.use()

        projection = glm.perspective(glm.radians(70), WIDTH/HEIGHT, 0.1, 100)
        view = camera.get_view_matrix()

        shader.set_mat4("projection", projection)
        shader.set_mat4("view", view)

        glBindVertexArray(VAO)

        # ===== DRAW TOUS LES BLOCS =====
        for pos in blocks:
            model = glm.translate(glm.mat4(1.0), glm.vec3(pos))
            shader.set_mat4("model", model)
            glDrawArrays(GL_TRIANGLES, 0, 36)

        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()