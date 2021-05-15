import pygame as pg
from game import *

#COLOURS
SCREEN_COLOUR = (55, 125, 255)

if __name__ == "__main__":
    game = Game(800, 600, (SCREEN_COLOUR))
    game.play_game()