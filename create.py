import pygame as pg
import os
from pygame.key import name
from pygame.locals import *

SCORE = 0
FPS = 120
WAIT = 40
SCREENX = 800
SCREENY = 600
screen = pg.display.set_mode((SCREENX, SCREENY))
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


def load_image(file):
    """ loads an image, prepares it for play
    """
    file = os.path.join("data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' %
                         (file, pg.get_error()))
    return surface.convert()


def load_sound(file):
    """ because pygame can be be compiled without mixer.
    """
    pg.mixer.init()
    if not pg.mixer:
        return None
    file = os.path.join("data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None



def load_arrow(direction, type):
        if type == 'regular':
            image_properties = REGULAR_TRIANGLES[direction]
        if type == 'score':
            image_properties = SCORE_TRIANGLES[direction]
        arrow_image, rotation = image_properties
        image = pg.transform.rotate(pg.transform.scale((load_image(arrow_image).convert()), (ARROW_WIDTH, ARROW_HEIGHT)), rotation)
        image.set_colorkey(WHITE)
        return image

def load_leaderboard_image():
    image = pg.transform.scale((load_image(LEADERBOARD_IMAGE)).convert(), (LEADERBOARD_IMAGE_SIZE, LEADERBOARD_IMAGE_SIZE))
    image.set_colorkey(BLACK)
    return image

def show_value(message, value, x, y, size):
    font = pg.font.Font('freesansbold.ttf', size)
    value_render = font.render(f'{message} {value}', True, (255, 125, 55))
    screen.blit(value_render, (x, y))
    return

def game_over_text():
    over_font = pg.font.Font('freesansbold.ttf', 64)
    again_font = pg.font.Font('freesansbold.ttf', 48)
    over_text = over_font.render(f'GAME OVER', True, (255, 125, 55))
    again_text = again_font.render(f'Play Again?', True, (255, 125, 55))
    screen.blit(over_text, (200, 250))
    screen.blit(again_text, (248, 310))


def leaderboard(score, song_name):
    file_path = os.path.join(os.getcwd(), 'leaderboards', (song_name + '.txt'))
    if not os.path.exists(file_path):
        with open(file_path, 'x') as high_scores:
            high_scores.write(f'{score}\n')
    else:
        with open(file_path, 'r+') as high_scores:
            lines = high_scores.readlines()
            written = False
            line_num = 0
            for line in lines:
                line_score = int(line[:-1])
                if written:
                    continue
                elif line_score <= score:
                    lines.insert(line_num, f'{score}\n')
                    written = True
                elif line_num + 1 == len(lines):
                    lines.insert(line_num + 1, f'{score}\n')
                    written = True
                line_num += 1
            high_scores.seek(0)
            for line in lines:
                high_scores.write(line)
            

    

# Imagery and sounds
