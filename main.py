import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = []
    drawable = []

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.append(player)
    drawable.append(player)

    asteroids = []
    asteroid_field = AsteroidField(asteroids)
    updatable.append(asteroid_field)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids:
            asteroid.update(dt)

        screen.fill("black")
        for obj in [player] + asteroids:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
