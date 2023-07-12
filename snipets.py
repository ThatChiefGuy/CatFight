import pygame

FPS = 60
main_sprite_sheet = None

player_group = pygame.sprite.Group()
player_image_size = (18 * 2, 65 * 2)
player_starting_position = (400, 600)
player_starting_angle = 90
player_speed = 10
player_rotation_speed = 2

bullet_size = (908 / 16, 178 / 16)
bullet_group = pygame.sprite.Group()
