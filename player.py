import pygame
import snipets
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.angle = 90
        self.image_copy = pygame.transform.scale(image, snipets.player_image_size)
        self.image = pygame.transform.rotate(self.image_copy, 0)
        self.rect = self.image.get_rect(center=snipets.player_starting_position)
        snipets.player_group.add(self)

    def update(self, key_input):
        self.rotate(key_input)
        self.movement()

    def rotate(self, key_input):
        if key_input[ord("w")]:
            self.angle += snipets.player_rotation_speed
        if key_input[ord("s")]:
            self.angle -= snipets.player_rotation_speed

        self.image = pygame.transform.rotate(self.image_copy, self.angle)

    def movement(self):
        dx = snipets.player_speed * math.cos(self.angle)
        dy = snipets.player_speed * math.sin(self.angle)
        self.rect.x += dx
        self.rect.y += dy
        print(dy, dx)
