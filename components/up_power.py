import random

import pygame

from utils.constans import SCREEN_WIDTH, SCREEN_HEIGHT, IMG_DIR, WHITE
from os import path

allowed_speed = list(range(3,4))

class Up_power(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "sun.png")).convert()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.speedy = random.choice(allowed_speed)

    def update(self):
        self.rect.y = self.rect.y + self.speedy


