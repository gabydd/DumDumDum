import pygame as pg


class Song:
    def __init__(self, keys=None, reps=1):
        if keys == None:
            keys = []
        self.keys = keys
        self.reps = reps

    def add_key(self, key):
        self.keys.append(key)

    def correct_key(self, spot):
        return f'pg.K_{self.keys[spot]}'

    def with_reps(self):
        self.keys *= self.reps

    ''' 
    add ability for sequence of keys denotion and held key denotion
    '''