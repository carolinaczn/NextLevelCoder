import pygame

from components.bullet import Bullet
from utils.constans import (RED, SCREEN_HEIGHT, SCREEN_WIDTH)


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT-10
        self.bullets = pygame.sprite.Group()

    def update(self):
        key = pygame.key.get_pressed()

        #It is assigned the movement that it will do when it plays a certain key //
        # Se le asigna el movimiento que hará cuando toque una determinada tecla

        if key[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if key[pygame.K_LEFT]:
            self.rect.x -= 5
        if self.rect.left >= SCREEN_WIDTH:
            self.rect.left = SCREEN_WIDTH


        #This part is for the player to avoid exiting the screen to the left //
        # Esta parte es para que el jugador evite salir de la pantalla por la izquierda

        if self.rect.x <= 0:
            self.rect.x = 0


    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(bullet)
        self.bullets.add(bullet)
