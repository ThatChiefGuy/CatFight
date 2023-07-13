import pygame
import snipets


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.normal_image = snipets.main_sprite_sheet.get_sprite(0, 0, 68, 55, 2, (0, 0, 0))
        self.image_left = snipets.main_sprite_sheet.get_sprite(74, 0, 68, 55, 2, (0, 0, 0))
        self.image_right = snipets.main_sprite_sheet.get_sprite(148, 0, 68, 55, 2, (0, 0, 0))
        self.image = self.normal_image
        self.rect = self.image.get_rect()
        self.animation_state = "forward"
        snipets.player_group.add(self)

    def update(self, keys_pressed, window_size):
        self.movement(keys_pressed)
        self.collisions(window_size[0], window_size[1])
        self.animation()

    def movement(self, keys_pressed):
        if keys_pressed[ord("s")]:
            self.rect.y += snipets.player_speed

        if keys_pressed[ord("w")]:
            self.rect.y -= snipets.player_speed

        if keys_pressed[ord("a")]:
            self.rect.x -= snipets.player_speed
            self.animation_state = "left"

        if keys_pressed[ord("d")]:
            self.rect.x += snipets.player_speed
            self.animation_state = "right"

    def collisions(self, window_height, window_width):
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > window_height:
            self.rect.bottom = window_height

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > window_width:
            self.rect.right = window_width

    def animation(self):
        if self.animation_state == "forward":
            self.image = self.normal_image

        if self.animation_state == "left":
            self.image = self.image_left

        if self.animation_state == "right":
            self.image = self.image_right

        self.animation_state = "forward"
