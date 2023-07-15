import pygame
import snipets


class Bullet(pygame.sprite.Sprite):
    def __init__(self, starting_position):
        super().__init__()
        width, height = snipets.bullet_image.get_size()
        self.image = pygame.transform.scale(snipets.bullet_image, (width / 16, height / 16))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = starting_position
        self.image.set_colorkey((255, 255, 255))
        snipets.bullet_group.add(self)

    def update(self):
        self.rect.y -= snipets.bullet_speed
