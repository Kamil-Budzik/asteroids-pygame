import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    LINE_WIDTH = 2

    def __init__(self, x, y, radius, asteroid_group=None):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.asteroid_group = asteroid_group  # reference to global list/group

    def draw(self, screen):
        pygame.draw.circle(screen, "white",
                           (int(self.position.x), int(self.position.y)),
                           self.radius, Asteroid.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def kill(self):
        """Remove asteroid from its group (manual list-based)."""
        if self.asteroid_group and self in self.asteroid_group:
            self.asteroid_group.remove(self)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return []  # return empty list instead of None

        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle) * 1.2
        v2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2

        return [a1, a2]  # always return a list
