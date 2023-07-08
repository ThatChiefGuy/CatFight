import pygame
import snipets


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, angle):
        super().__init__()
        copy_image = pygame.transform.scale(image, snipets.bullet_size)
        self.image = pygame.transform.rotate(copy_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)
        self.image.set_colorkey((255, 255, 255))
        snipets.bullet_group.add(self)

