import os
import sys
import pygame as pg
import pyrythms
import create
from create import draw_window
from create import test_song

# Constants for reseting
SCORE = 0
FPS = 60
WAIT = 40
SCREENX = 800
SCREENY = 600
screen = pg.display.set_mode((SCREENX, SCREENY))
SKIP = False
CURRENT_COLOUR = (0, 0, 255)
WRONG_COLOUR = (255, 0, 0)
RIGHT_COLOUR = (0, 255, 0)
NEXT_COLOUR = (255, 255, 255)

# FIX THE PLACEMENT OF STUFF(make functions do rectangle stuff and maybe sprite classes) AND ADD IMAGERY SO IT IS APPEALING, DO PROPER COMMENTING AND DOCUMENTATION

# future ideas leaderboard file and song maker with a seperated file with all the songs in it   

#test_song = pyrythms.Song(['o1', 'o2', 'o3', 'o4', 'h5', 'o6', 'o7'], 3)
#test_song.with_reps()


def correct_press(key, score, frames, correct, cmd_info, add_score, right_letters, wrong_letters):
    if key < len(test_song.keys):
        if frames % WAIT == 0 and frames != 0:
            for info in cmd_info:
                print(info)
            if correct:
                score += add_score
                add_score = 0
                correct = False
                right_letters.append((test_song.keys[key])[1:])
            else:
                score += add_score
                add_score = 0
                wrong_letters.append((test_song.keys[key])[1:])
            key += 1
            return ((key, score, correct, add_score, right_letters, wrong_letters))

#crab_king = load_image('crab_king.png')


def main():

    pg.init()
    # Variables to hold values used during the game
    current_score = SCORE
    current_key = 0
    is_correct = False
    frames = 0
    clock = pg.time.Clock()
    run = True
    add_score = 0
    right_letters = []
    wrong_letters = []
    while run:
        clock.tick(FPS)
        time = pg.time.get_ticks()

        events = pg.event.get()
        pressed = pg.key.get_pressed()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit
                sys.exit()
            if event.type == pg.KEYDOWN:
                if current_key < len(test_song.keys):
                    if event.key == eval(test_song.correct_key(current_key, 'one')):

                        #more accurate scoring with a furmula using the amount of frames passed till
                        if not is_correct:
                            add_score += (WAIT - (frames - WAIT * current_key)) * (60 / WAIT)
                        is_correct = True
                    else:
                        add_score -= 5
            if current_key >= len(test_song.keys):
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    if 248 < x < 600 and 310 < y < 358:
                        main()

        if current_key < len(test_song.keys) and (test_song.keys[current_key])[0] == 'h':
            if pressed[eval(test_song.correct_key(current_key, 'hold'))]:
                add_score += 1
                is_correct = True
            # start with the first num in a sequence then key for each one adding to list if '==' is true

        # Checks if it is the end of a cycle and then evaluates if you pressed the right key unpacking those values if needed
        key_press = correct_press(
            current_key, current_score, frames, is_correct, [time, clock, frames, add_score], add_score, right_letters, wrong_letters)
        if key_press != None:
            current_key, current_score, is_correct, add_score, right_letters, wrong_letters = key_press

        draw_window(current_key, current_score, right_letters, wrong_letters)
        frames += 1


if __name__ == "__main__":
    main()
