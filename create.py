import pygame as pg
import os
import pyrythms


SCORE = 0
FPS = 60
WAIT = 40
SCREENX = 800
SCREENY = 600
screen = pg.display.set_mode((SCREENX, SCREENY))
SKIP = False
WHITE = (0,0,0)
CURRENT_COLOUR = (0, 0, 255)
WRONG_COLOUR = (255, 0, 0)
RIGHT_COLOUR = (0, 255, 0)
NEXT_COLOUR = (255, 255, 255)


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
    if not pg.mixer:
        return None
    file = os.path.join("data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


def show_letters(current_letter, right_letters, wrong_letters):
    FONT_SIZE = 72
    font = pg.font.Font('freesansbold.ttf', 72)
    SPACE = FONT_SIZE + 10
    letter_placeX = SCREENX - (SPACE + 10) * len(test_song.keys)
    letter_placeY = 268

    for letter in test_song.keys:
        letter = letter[1:]
        if letter == current_letter[1:]:
            letter_render = font.render(letter, True, CURRENT_COLOUR)
            screen.blit(letter_render, (letter_placeX, letter_placeY))
            letter_placeX += SPACE
        elif letter in right_letters:
            letter_render = font.render(letter, True, RIGHT_COLOUR)
            screen.blit(letter_render, (letter_placeX, letter_placeY))
            letter_placeX += SPACE
        elif letter in wrong_letters:
            letter_render = font.render(letter, True, WRONG_COLOUR)
            screen.blit(letter_render, (letter_placeX, letter_placeY))
            letter_placeX += SPACE
        else:
            letter_render = font.render(letter, True, NEXT_COLOUR)
            screen.blit(letter_render, (letter_placeX, letter_placeY))
            letter_placeX += 70
    letter_mode = current_letter[0]
    current_letter = current_letter[1:]
    string_placeX = 232
    string_placeY = 350
    if letter_mode == 'o':
        prompt_render = font.render(f'PRESS: {current_letter}', True, (255, 125, 55))
    if letter_mode == 'h':
        prompt_render = font.render(f'HOLD: {current_letter}', True, (255, 125, 55))    
    screen.blit(prompt_render, (string_placeX, string_placeY))


def show_value(message, value, x, y):
    font = pg.font.Font('freesansbold.ttf', 32)
    value_render = font.render(f'{message} {value}', True, (255, 125, 55))
    screen.blit(value_render, (x, y))

def game_over_text():
    over_font = pg.font.Font('freesansbold.ttf', 64)
    again_font = pg.font.Font('freesansbold.ttf', 48)
    over_text = over_font.render(f'GAME OVER', True, (255, 125, 55))
    again_text = again_font.render(f'Play Again?', True, (255, 125, 55))
    screen.blit(over_text, (200, 250))
    screen.blit(again_text, (248, 310))


def draw_window(key, score, right_letters, wrong_letters):
    screen.fill((55, 125, 255))
    screen.blit(crab_king, (700, 500))
    if key < len(test_song.keys):
        show_letters(test_song.keys[key], right_letters, wrong_letters)
    else:
        show_value('Your score was:', score, 50, 50)
    if key >= len(test_song.keys):
        game_over_text()
    pg.display.update()

class Arrow:
    def __init__()

# Imagery and sounds

crab_king = load_image('crab_king.png')
test_song = pyrythms.Song(['o1', 'o2', 'o3', 'o4', 'h5', 'o6', 'o7'], 3)