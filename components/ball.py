import pygame

from utils.constans import (GREEN, SCREEN_HEIGHT, SCREEN_WIDTH, IMG_DIR, BLACK, WHITE)
from os import path

import random

allowed_speed = list(range(3,5))


class Ball(pygame.sprite.Sprite):

    def __init__(self, size):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "rocket.png")).convert()
        self.image = pygame.transform.scale(self.image, (100//size, 100//size))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        #is assigned so that the ball appears on either side of the screen //
        # se asigna para que la bola aparezca a ambos lados de la pantalla

        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.choice(allowed_speed)
        self.speedx = random.choice(allowed_speed)

        self.size = size

    def update(self):

        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy

        #The ball bounces off the ends from left to right
        #La pelota rebota en los extremos de izquierda a derecha.

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.speedx = random.choice(allowed_speed) * -1

        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = random.choice(allowed_speed)

        #The ball bounces off the top and bottom ends
        #La pelota rebota en los extremos superior e inferior.

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speedy= random.choice(allowed_speed) * -1

        if self.rect.top < 0:
            self.rect.top =0
            self.speedy = random.choice(allowed_speed) + 1
