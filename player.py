import pygame
import snipets


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = snipets.main_sprite_sheet.get_sprite(0, 0, 68, 55, 2, (0, 0, 0))
        self.rect = self.image.get_rect()
        snipets.player_group.add(self)

    def update(self, keys_pressed):
        self.movement(keys_pressed)

    def movement(self, keys_pressed):
        if keys_pressed[ord("d")]:
            self.rect.x += snipets.player_speed

        if keys_pressed[ord("a")]:
            self.rect.x -= snipets.player_speed

        if keys_pressed[ord("s")]:
            self.rect.y += snipets.player_speed

        if keys_pressed[ord("w")]:
            self.rect.y -= snipets.player_speed
