import pygame as pg
from game import *
from songs import *
from create import SCREENX, SCREENY
from pygame.locals import *

#COLOURS
SCREEN_COLOUR = (55, 125, 255)

if __name__ == "__main__":
    fullscreen = False
    while True:
        menu = Menu(SCREENX, SCREENY, (SCREEN_COLOUR), fullscreen)
        song, mode, fullscreen = menu.choosing_screen()
        if mode == 'game':
            game = Game(SCREENX, SCREENY, (SCREEN_COLOUR), song, fullscreen)
            fullscreen = game.play_game()
        if mode == 'leaderboard':
            current_leaderboard = Leaderboards(SCREENX, SCREENY, (SCREEN_COLOUR), song, fullscreen)
            fullscreen = current_leaderboard.leaderboard_screen()