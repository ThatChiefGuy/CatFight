import pygame

FPS = 60
main_sprite_sheet = None

player_group = pygame.sprite.Group()
player_starting_position = (400, 600)
player_speed = 10

bullet_size = (908 / 16, 178 / 16)
bullet_group = pygame.sprite.Group()
