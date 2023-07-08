import pygame
import snipets
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.angle = 0
        self.image_copy = pygame.transform.scale(image, snipets.player_image_size)
        self.image = pygame.transform.rotate(self.image_copy, self.angle)
        self.rect = self.image.get_rect(center=snipets.player_starting_position)
        snipets.player_group.add(self)

    def update(self, mouse_position):
        self.rotate(mouse_position)
        self.movement(mouse_position)

    def rotate(self, mouse_position):
        distance_x = mouse_position[0] - self.rect.x
        distance_y = -(mouse_position[1] - self.rect.y)
        self.angle = math.degrees(math.atan2(distance_y, distance_x))
        self.image = pygame.transform.rotate(self.image_copy, self.angle)

    def movement(self, mouse_position):
        radians = math.atan2(mouse_position[1] - self.rect.y, mouse_position[0] - self.rect.x)
        dx = math.cos(radians)
        dy = math.sin(radians)
        self.rect.x += dx * snipets.player_speed
        self.rect.y += dy * snipets.player_speed


