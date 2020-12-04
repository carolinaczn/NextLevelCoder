from components.game import Game
import pygame

if __name__ == "__main__":
    game = Game()
    while game.runnig:
        if not game.playing:
            game.show_start_screen()
            game.run()

    pygame.quit()