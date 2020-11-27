import pygame

from utils.constans import (RED, SCREEN_HEIGHT, SCREEN_WIDTH)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.centery = SCREEN_HEIGHT/2

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if key[pygame.K_LEFT]:
            self.rect.x -= 5
        if self.rect.left >= SCREEN_WIDTH:
            self.rect.left = SCREEN_WIDTH