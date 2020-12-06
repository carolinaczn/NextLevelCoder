import pygame

from components.bullet import Bullet
from utils.constans import (SCREEN_HEIGHT, SCREEN_WIDTH, IMG_DIR, WHITE)
from os import path


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.image = pygame.image.load(path.join(IMG_DIR, "nave.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.bullets = pygame.sprite.Group()


    def update(self):
        key = pygame.key.get_pressed()

        # It is assigned the movement that it will do when it plays a certain key //
        # Se le asigna el movimiento que hará cuando toque una determinada tecla

        if key[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if key[pygame.K_LEFT]:
            self.rect.x -= 5
        if self.rect.left >= SCREEN_WIDTH:
            self.rect.left = SCREEN_WIDTH

        # This part is for the player to avoid exiting the screen to the left //
        # Esta parte es para que el jugador evite salir de la pantalla por la izquierda

        if self.rect.x <= 0:
            self.rect.x = 0

    def shoot(self, has_power_up):

        powerUp = has_power_up

        if not powerUp:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.game.all_sprites.add(bullet)
            self.bullets.add(bullet)

        if powerUp :
            bullet5 = Bullet(self.rect.centerx, self.rect.top)

            bullet1 = Bullet(self.rect.centerx + 20, self.rect.top)

            bullet2 = Bullet(self.rect.centerx - 20, self.rect.top)

            bullet3 = Bullet(self.rect.centerx + 20, self.rect.top)

            bullet4 = Bullet(self.rect.centerx - 20, self.rect.top)
            self.game.all_sprites.add(bullet5, bullet1, bullet2, bullet3, bullet4)
            self.bullets.add(bullet5, bullet1, bullet2, bullet3, bullet4)
