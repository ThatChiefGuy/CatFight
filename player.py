import pygame
import snipets
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image_copy = pygame.transform.scale(image, snipets.player_image_size)
        self.image = pygame.transform.rotate(self.image_copy, 0)
        self.rect = self.image.get_rect(center=snipets.player_starting_position)
        snipets.player_group.add(self)
