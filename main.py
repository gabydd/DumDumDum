import os
import pygame as pg
import pyrythms

# Constants for reseting
SCORE = 0
FPS = 40
screen = pg.display.set_mode((800, 600))


# Variables to hold current values
current_score = SCORE
current_key = 0
is_correct = False

test_song = pyrythms.Song(['a', 'b', 'c', 'd', '1', '2', '3'], 5)

def load_image(file):
    """ loads an image, prepares it for play
    """
    file = os.path.join("data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()

test_person = load_image('Undertale_Character-removebg-preview-32xauto.png')


def load_sound(file):
    """ because pygame can be be compiled without mixer.
    """
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None

def showLetter(letter):
    font = pg.font.Font('freesansbold.ttf', 32)
    string_placeX = 372
    string_placeY = 284
    prompt_render = font.render(f'PRESS: {letter}', True, (255,125,55))
    screen.blit(prompt_render, (string_placeX, string_placeY))

def showValue(message, value, x, y):
    font = pg.font.Font('freesansbold.ttf', 32)
    value_render = font.render(f'{message} {value}', True, (255,125,55))
    screen.blit(value_render, (x, y))

def draw_window():
    screen.fill((55,125,255))
    screen.blit(test_person, (700, 500))
    showLetter(test_song.keys[current_key])
    if current_key >= len(test_song.keys) - 1:
        showValue('Your scpre was:', current_score, 50, 50)
    pg.display.update()

def main():
    
    pg.init()
    global current_key
    global is_correct
    global current_score
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
                if event.key == eval(test_song.correctKey(current_key)):
                    is_correct = True

                    print(f'score at eval: {current_score}')
        if current_key < len(test_song.keys) - 1:
            if time % 100 == 0:
                if is_correct:
                    current_score += 1
                    is_correct = False
                current_key += 1
                print(test_song.keys, current_key)
                print(test_song.keys[current_key])
                print(current_score)
                print(test_song.keys[current_key])
                print('key add time work')
                print(time)

        draw_window()
    pg.quit()

if __name__ == "__main__":
    main()