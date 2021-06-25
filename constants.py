import pygame as pg
SCREEN_COLOUR = (55, 125, 255)
ONE_PRESS = 'o'
HOLD = 'h'
PLACES = {'u': (218), 'd': (318), 'l': (418), 'r': (518)}
SCORE = 0
FPS = 120
WAIT = 40
SCREENX = 800
SCREENY = 600
SKIP = False
WHITE = (255,255,255)
BLACK = (0,0,0)
CURRENT_COLOUR = (0, 0, 255)
WRONG_COLOUR = (255, 0, 0)
RIGHT_COLOUR = (0, 255, 0)
NEXT_COLOUR = (255, 255, 255)
LAVENDER = (230, 230, 250)
GREEN_IMAGE = 'green_arrow_main.png'
RED_IMAGE = 'red_arrow_main.png'
YELLOW_IMAGE = 'yellow_arrow_main.png'
BLUE_IMAGE = 'blue_arrow_main.png'
LEADERBOARD_IMAGE = 'leaderboard.png'
LEADERBOARD_IMAGE_SIZE = 64
REGULAR_TRIANGLES = {
    'u': ('green_arrow_main.png', 0),
    'd': ('red_arrow_main.png', 180),
    'l': ('yellow_arrow_main.png', 90),
    'r': ('blue_arrow_main.png', 270)}

SCORE_TRIANGLES = {
    'u': ('green_arrow_score.png', 0),
    'd': ('red_arrow_score.png', 180),
    'l': ('yellow_arrow_score.png', 90),
    'r': ('blue_arrow_score.png', 270)}

ARROW_WIDTH = 64
ARROW_HEIGHT = 64
pg.display.init()
FULL_Y, FULL_X = (pg.display.Info().current_h, pg.display.Info().current_w)
pg.display.quit()