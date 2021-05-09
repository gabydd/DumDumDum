import os
import sys
import pygame as pg
import create

SCREENX = 800
SCREENY = 600
screen = pg.display.set_mode((SCREENX, SCREENY))

up_arrow = create.load_image('green_arrow_main.png').convert()
down_arrow = create.load_image('red_arrow_main.png').convert().set_colorkey(create.WHITE)
left_arrow = create.load_image('yellow_arrow_main.png').convert().set_colorkey(create.WHITE)
right_arrow = create.load_image('blue_arrow_main.png').convert().set_colorkey(create.WHITE)

up_arrow = up_arrow.set_colorkey((0,0,0))
#isa = create.load_image('Balabala_Design.png').()
#print(isa.get_alpha())

def main():
    pg.init()
    run = True
    while run:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                run = False
                pg.quit
                sys.exit()
        screen.fill((125, 125, 125))
        #screen.blit(isa, (10, 20))
        #screen.blit(up_arrow, (0,0))
        pg.display.update()


if __name__ == '__main__':
    main()
