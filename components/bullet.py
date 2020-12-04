import pygame


from utils.constans import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, IMG_DIR
from os import path

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "solar.png")).convert()
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()
