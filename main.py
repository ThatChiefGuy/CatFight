import pygame

import player
import snipets
import sprite_sheet


class Game:
    def __init__(self, window_height, window_width):
        self.screen = pygame.display.set_mode((window_height, window_width))
        self.main_clock = pygame.time.Clock()
        main_sprite_sheet_image = pygame.image.load("Assets/sprites.png")
        snipets.bullet_image = pygame.image.load("Assets/bullet_image.png")
        snipets.main_sprite_sheet = sprite_sheet.SpriteSheet(main_sprite_sheet_image)
        self.player = player.Player()

    def draw(self):
        self.screen.fill((0, 150, 250))
        snipets.gas_group.draw(self.screen)
        snipets.bullet_group.draw(self.screen)
        snipets.player_group.draw(self.screen)
        self.screen.blit(self.player.propeller_image,
                         (self.player.rect.left + self.player.rect.width / 2 -
                          self.player.propeller_image.get_size()[0] / 2,
                          self.player.rect.top - self.player.propeller_image.get_size()[1] / 2))
        pygame.display.update()

    def main(self):
        run = True
        while run:
            self.main_clock.tick(snipets.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            snipets.player_group.update(pygame.key.get_pressed(), (snipets.screen_width, snipets.screen_height))
            snipets.gas_group.update()
            snipets.bullet_group.update()
            self.draw()


if __name__ == "__main__":
    game = Game(snipets.screen_width, snipets.screen_height)
    game.main()
