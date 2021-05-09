import pygame as pg

ONE_PRESS = 'o'
HOLD = 'h'

class Song:
    def __init__(self, keys=None, reps=1):
        if keys == None:
            keys = []
        self.keys = keys
        self.reps = reps

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

    ''' 
    add ability for sequence of keys denotion and held key denotion
    '''


'''
    def correct_key(self, spot, mode):
        key = self.keys[spot]
        if key[0] == ONE_PRESS and mode == 'one':
            key = key[1:]
            return f'pg.K_{key}'
        elif key[0] == HOLD and mode == 'hold':
'''            