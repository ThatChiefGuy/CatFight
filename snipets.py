import pygame

FPS = 60
main_sprite_sheet = None
screen_width = 1700
screen_height = 900

player_group = pygame.sprite.Group()
player_starting_position = (1700 / 2, 700)
player_speed = 6

gas_group = pygame.sprite.Group()
gas_spawn_time = 10

bullet_image = None
bullet_speed = 10
bullet_cooldown = 10
bullet_cooldown_timer = 0
bullet_group = pygame.sprite.Group()

cloud_group = pygame.sprite.Group()
cloud_images = []
cloud_speed = 5
cloud_time = 14
cloud_timer = 0
