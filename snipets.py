import pygame

FPS = 60


player_group = pygame.sprite.Group()
player_image_size = (65 * 2, 18 * 2)
player_starting_position = (400, 600)
player_starting_angle = 90
player_speed = 5

bullet_size = (908 / 16, 178 / 16)
bullet_group = pygame.sprite.Group()
