from create import load_arrow
import sys
import pygame as pg



class Arrow(pg.sprite.Sprite):
    def __init__(self, direction):
        super().__init__(self)
        self.direction = direction
        self.image = load_arrow(direction)
        self.x = places[direction]
        self.y = 0
    def draw_arrow(self):
        pass



class Game:
    def __init__(self, screenX, screenY, bg_colour):
        pg.init()
        self.screen = pg.display.set_mode((screenX, screenY))
        self.bg_colour = bg_colour
    
    def draw_window(self):
        self.screen.fill(self.bg_colour)
        pg.display.update()

    def play_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            self.draw_window()