import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.dt = 0

        # game objects
        self.asteroids = []
        self.shots = []
        self.updatable = []
        self.drawable = []

        # asteroid spawner
        self.asteroid_field = AsteroidField(self.asteroids)
        self.updatable.append(self.asteroid_field)

        # player
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, self.shots)
        self.updatable.append(self.player)
        self.drawable.append(self.player)

        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update_objects()
            self.handle_collisions()
            self.draw()
            self.dt = self.clock.tick(60) / 1000

        print("Game Over!")
        pygame.quit()

    # --------------------
    # 🔹 Event handling
    # --------------------
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # --------------------
    # 🔹 Updates
    # --------------------
    def update_objects(self):
        for obj in self.updatable:
            obj.update(self.dt)

        for asteroid in self.asteroids:
            asteroid.update(self.dt)

        for shot in self.shots:
            shot.update(self.dt)

    # --------------------
    # 🔹 Collisions
    # --------------------
    def handle_collisions(self):
        self.handle_player_collision()
        self.handle_bullet_asteroid_collision()
        self.cleanup_objects()

    def handle_player_collision(self):
        for asteroid in self.asteroids:
            if asteroid.check_collisions(self.player):
                self.running = False

    def handle_bullet_asteroid_collision(self):
        self.to_remove_asteroids = []
        self.to_remove_shots = []
        for asteroid in self.asteroids:
            for bullet in self.shots:
                if asteroid.check_collisions(bullet):
                    self.to_remove_asteroids.append(asteroid)
                    self.to_remove_shots.append(bullet)

    def cleanup_objects(self):
        for asteroid in self.to_remove_asteroids:
            if asteroid in self.asteroids:
                self.asteroids.remove(asteroid)
        for bullet in self.to_remove_shots:
            if bullet in self.shots:
                self.shots.remove(bullet)

    # --------------------
    # 🔹 Drawing
    # --------------------
    def draw(self):
        self.screen.fill("black")
        for obj in [self.player] + self.asteroids + self.shots:
            obj.draw(self.screen)
        pygame.display.flip()


def main():
    Game().run()


if __name__ == "__main__":
    main()
