import pygame
import player
import snipets


class Game:
    def __init__(self, window_height, window_width):
        self.screen = pygame.display.set_mode((window_height, window_width))
        self.main_clock = pygame.time.Clock()
        self.player_image = pygame.image.load("Assets/player_plane.gif").convert_alpha()
        self.player = player.Player(pygame.transform.flip(self.player_image, True, False))

    def draw(self):
        self.screen.fill((250, 0, 250))
        self.screen.blit(self.player.image, (self.player.rect.x - int(self.player.image.get_width()) / 2,
                                            self.player.rect.y - int(self.player.image.get_height()) / 2))
        pygame.display.update()

    def main(self):
        run = True
        while run:
            self.main_clock.tick(snipets.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            snipets.player_group.update(pygame.mouse.get_pos())
            self.draw()


if __name__ == "__main__":
    game = Game(1000, 1000)
    game.main()
