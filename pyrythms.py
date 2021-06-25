import pygame as pg
from pygame import rect
from create import load_arrow, ARROW_HEIGHT, SCREENX, SCREENY, load_sound
from pygame.locals import *

ONE_PRESS = 'o'
HOLD = 'h'
PLACES = {'u': (218), 'd': (318), 'l': (418), 'r': (518)}


class Arrow(pg.sprite.Sprite):

    def __init__(self, direction, velocity):
        pg.sprite.Sprite.__init__(self)
        self.direction = direction
        self.image = load_arrow(self.direction, 'regular')
        self.rect = self.image.get_rect()
        self.rect.x = PLACES[self.direction]
        self.rect.y = 0
        self.velocity = velocity
        self.show = False

    def draw_arrow(self):
        pass
    def move(self):
        if self.rect.y < SCREENY - ARROW_HEIGHT:
            self.rect.y += self.velocity
        else:
            self.rect.y = SCREENY -ARROW_HEIGHT


class ScoreArrow(pg.sprite.Sprite):
    def __init__(self, direction) -> None:
        super().__init__()
        self.direction = direction
        self.image = load_arrow(self.direction, 'score')
        self.rect = self.image.get_rect()
        self.rect.x = PLACES[self.direction]
        self.rect.y = SCREENY - 2 * ARROW_HEIGHT



class Song:
    def __init__(self, name, keys=None, reps=1, music = 'test-music.ogg'):
        if keys == None:
            keys = []
        self.keys = keys
        self.reps = reps
        self.name = name
        self.music = load_sound(music)

    def add_key(self, key):
        self.keys.append(key)

    def correct_key(self, spot, mode):
        key = self.keys[spot]
        if key[0] == ONE_PRESS and mode == 'one':
            key = key[1:]
            return f'pg.K_{key}'
        elif key[0] == HOLD and mode == 'hold':
            key = key[1:]
            return f'pg.K_{key}'
        else:
            return 'SKIP'
            
        #add special indicator recongnition and return different values based on the indicator also take in which spot in event loop is calling the method

    def with_reps(self):
        self.keys *= self.reps
    
    def create_arrows(self):
        arrows = pg.sprite.Group()
        for key in self.keys:
            key = Arrow(key[1], int(key[2:]))
            arrows.add(key)
        return arrows