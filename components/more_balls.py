import pygame

from os import path
import random

from utils.constans import IMG_DIR, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

allowed_speed = list(range(2, 5))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "satellite.png")).convert()
        self.image = pygame.transform.scale(self.image,(50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.choice(allowed_speed)
        self.speedx = random.choice(allowed_speed)

    def update(self):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.speedx = random.choice(allowed_speed) * -1

        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = random.choice(allowed_speed)

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speedy= random.choice(allowed_speed) * -1

        if self.rect.top < 0:
            self.rect.top =0
            self.speedy = random.choice(allowed_speed) + 1
