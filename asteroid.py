import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    LINE_WIDTH = 2

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, Asteroid.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt


