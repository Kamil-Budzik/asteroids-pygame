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


    asteroids = []
    asteroid_field = AsteroidField(asteroids)
    updatable.append(asteroid_field)

    shots = []
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    updatable.append(player)
    drawable.append(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for obj in updatable:
            obj.update(dt)

        
        to_remove_asteroids = []
        to_remove_shots = []

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                running = False
            asteroid.update(dt)
            
            for bullet in shots:
                if asteroid.check_collisions(bullet):
                    to_remove_shots.append(bullet)
                    to_remove_asteroids.append(asteroid)


        for asteroid in to_remove_asteroids:
            if asteroid in asteroids:
                asteroids.remove(asteroid)

        for bullet in to_remove_shots:
            if bullet in shots:
                shots.remove(bullet)

        for shot in shots:
            shot.update(dt)

        screen.fill("black")

        for obj in [player] + asteroids + shots:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    print("Game Over!")
    pygame.quit()



if __name__ == "__main__":
    main()
