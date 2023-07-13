import pygame
import snipets


class Gas(pygame.sprite.Sprite):
    def __init__(self, starting_position):
        super().__init__()
        self.image = snipets.main_sprite_sheet.get_sprite(84, 71, 29, 27, 2, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = starting_position
        self.disappear_timeer = 0
        self.disappear_time = 20
        snipets.gas_group.add(self)

    def update(self):
        size_x, size_y = self.image.get_size()
        self.disappear_timeer += 1
        self.rect.y += 3
        if self.rect.top == snipets.screen_height:
            self.kill()
        if self.disappear_timeer >= self.disappear_time and not size_x < 0 and not size_y < 0:
            self.image = pygame.transform.scale(self.image, (size_x / 1.1, size_y / 1.1)).convert_alpha()
