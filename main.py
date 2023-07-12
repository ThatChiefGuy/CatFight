import pygame

import Bullet
import player
import snipets


class Game:
    def __init__(self, window_height, window_width):
        self.screen = pygame.display.set_mode((window_height, window_width))
        self.main_clock = pygame.time.Clock()
        snipets.main_sprite_sheet = pygame.image.load("Assets/sprites.png")
        bullet_image = pygame.image.load("Assets/bullet_image.png").convert_alpha()

    def draw(self):
        self.screen.fill((250, 0, 250))

        pygame.display.update()

    def main(self):
        run = True
        while run:
            self.main_clock.tick(snipets.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            snipets.player_group.update(pygame.key.get_pressed())
            self.draw()


if __name__ == "__main__":
    game = Game(1700, 900)
    game.main()
