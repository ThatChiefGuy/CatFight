import pygame
import snipets


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = snipets.main_sprite_sheet.get_sprite(0, 0, 68, 55, 2, (0, 0, 0))
        self.rect = self.image.get_rect()
        snipets.player_group.add(self)
