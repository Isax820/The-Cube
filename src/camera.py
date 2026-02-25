import glm
import math

class Camera:

    def __init__(self):
        self.position = glm.vec3(0, 5, 5)
        self.front = glm.vec3(0, 0, -1)
        self.up = glm.vec3(0, 1, 0)

        self.yaw = -90
        self.pitch = 0

        self.speed = 5

    def get_view_matrix(self):
        return glm.lookAt(
            self.position,
            self.position + self.front,
            self.up
        )