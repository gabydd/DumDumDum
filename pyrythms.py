import pygame as pg

class Song:
    def __init__(self, keys = None, reps = 0):
        if keys == None:
            keys = []
        self.keys = keys
        self.reps = reps

    def addKey(self, key):
        self.keys.append(key)

    def correctKey(self, spot):
        return f'pg.K_{self.keys[spot]}'
