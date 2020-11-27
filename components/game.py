import pygame

from components.player import Player
from utils.constans import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TITTLE,
    BLACK
)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITTLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        self.create_components()
        # Game loop:

        self.playing = True

        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(120)
        pygame.quit()




    def create_components(self):
        self.all_sprites = pygame.sprite.Group()
        player = Player()
        self.all_sprites.add(player)

    def update(self):
        self.all_sprites.update()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
