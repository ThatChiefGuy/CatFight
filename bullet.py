import pygame
import snipets


class Bullet(pygame.sprite.Sprite):
    def __init__(self, starting_position):
        super().__init__()
        self.image = snipets.bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = starting_position
        snipets.bullet_group.add(self)

    def update(self):
        self.rect.y -= snipets.bullet_speed
