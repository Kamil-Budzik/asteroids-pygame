import pygame
from circleshape import CircleShape
from constants import *
from shot import *


class Player(CircleShape):
    LINE_WIDTH = 2

    def __init__(self, x, y, shots):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots
        self.timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), Player.LINE_WIDTH)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.reverse(dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        # if keys[pygame.K_s]:
        #     self.move_backward(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def reverse(self, dt):
        self.rotation -= PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    # def move_backward(self, dt):
    #     forward = pygame.Vector2(0, 1).rotate(self.rotation)
    #     self.position -= forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return

        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot.rotate(self.rotation + 180)
        self.shots.append(shot)
