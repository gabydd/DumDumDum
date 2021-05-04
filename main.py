import os
import pygame as pg
import pyrythms

# Constants for reseting
SCORE = 0
FPS = 60
WAIT = 60
screen = pg.display.set_mode((800, 600))

# FIX THE PLACEMENT OF STUFF(make functions do rectangle stuff and maybe sprite classes) AND ADD IMAGERY SO IT IS APPEALING, DO PROPER COMMENTING AND DOCUMENTATION

# future ideas leaderboard file and song maker with a seperated file with all the songs in it   

test_song = pyrythms.Song(['a', 'b', 'c', 'd', '1', '2', '3'], 3)
test_song.with_reps()


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


crab_king = load_image('crab_king.png')


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


def show_letter(letter):
    font = pg.font.Font('freesansbold.ttf', 32)
    string_placeX = 372
    string_placeY = 284
    prompt_render = font.render(f'PRESS: {letter}', True, (255, 125, 55))
    screen.blit(prompt_render, (string_placeX, string_placeY))


def show_value(message, value, x, y):
    font = pg.font.Font('freesansbold.ttf', 32)
    value_render = font.render(f'{message} {value}', True, (255, 125, 55))
    screen.blit(value_render, (x, y))


def draw_window(key, score):
    screen.fill((55, 125, 255))
    screen.blit(crab_king, (700, 500))
    if key < len(test_song.keys):
        show_letter(test_song.keys[key])
    else:
        show_value('Your score was:', score, 50, 50)
    pg.display.update()


def correct_press(key, score, frames, correct, cmd_info):
    if key < len(test_song.keys):
        if frames % WAIT == 0 and frames != 0:
            if correct:
                score += 1
                correct = False
            key += 1
            for info in cmd_info:
                print(info)
            return ((key, score, correct))


def main():

    pg.init()
    # Variables to hold current values
    current_score = SCORE
    current_key = 0
    is_correct = False
    frames = 0
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        time = pg.time.get_ticks()

        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if current_key < len(test_song.keys):
                    if event.key == eval(test_song.correct_key(current_key)):
                        '''
                        create more accurate scoring with a furmula like:
                        if false:
                            add_score = WAIT - frames % current_key
                        '''
                        is_correct = True

            # pg.key.get_focused for holding down keys

            # start with the first num in a sequence then key for each one adding to list if '==' is true
        # Checks if it is the end of a cycle and then evaluates if you pressed the right key unpacking those values if needed
        key_press = correct_press(
            current_key, current_score, frames, is_correct, [time, clock, frames])
        if key_press != None:
            current_key, current_score, is_correct = key_press

        draw_window(current_key, current_score)
        frames += 1
    pg.quit()


if __name__ == "__main__":
    main()
