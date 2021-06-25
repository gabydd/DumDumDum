import os
from pygame.font import Font
from create import BLACK, WHITE, game_over_text, leaderboard, load_image, load_leaderboard_image, show_value, LAVENDER
import sys
import pygame as pg
from pygame import sprite
from pyrythms import ScoreArrow, Song
from songs import songs
from create import SCREENX, SCREENY, ARROW_HEIGHT
from pygame.locals import *
from math import  ceil






class Game:
    def __init__(self, screenX, screenY, bg_colour, song, fullscreen):
        pg.init()
        self.screen = pg.display.set_mode((screenX, screenY))
        try:
            self.background = load_image('sky-background.png')
        except FileExistsError:
            self.background = bg_colour
        self.screen.blit(self.background, (0,0))
        pg.display.update()
        self.song = song
        self.waiting_arrows = self.song.create_arrows()
        self.shown_arrows = pg.sprite.Group()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.frames = 0
        self.wait = 30
        self.score = 0
        self.update_rects = []
        self.pressed_keys = []
        self.old_rects = []
        self.score_updated = False
        self.fullscreen = fullscreen
        self.score_arrows = pg.sprite.Group()
        letters = ['u', 'd', 'l', 'r']
        for letter in letters:
            letter = ScoreArrow(letter)
            self.score_arrows.add(letter)
        self.game_over = False
        self.play_again = False
        self.song.music.play()


    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP or event.key == pg.K_w:
                    self.pressed_keys.append('u')
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.pressed_keys.append('d')
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.pressed_keys.append('l')
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.pressed_keys.append('r')
            if self.game_over:
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    if 248 < x < 600 and 310 < y < 358:
                        self.play_again = True


    def move_arrows(self):
        for arrow in self.shown_arrows:
            arrow.move()

    def new_shown_arrow(self):
        if self.frames % self.wait == 0:
            current_arrow = 0
            for arrow in self.waiting_arrows:
                if 0 == current_arrow:
                    arrow.show = True
                current_arrow += 1

    def handle_arrows(self):
        if self.frames % self.wait == 0:
            current_arrow = 0
            for arrow in self.waiting_arrows:
                if 0 == current_arrow:
                    arrow.show = True
                current_arrow += 1
        arrows_to_evaluate = sprite.Group()
        end_arrows = sprite.Group()
        if len(self.pressed_keys) == 0:
            self.pressed_keys.append('place holder')
        for key in self.pressed_keys:
            for arrow in self.shown_arrows:
                if arrow.rect.y == SCREENY - ARROW_HEIGHT:
                    end_arrows.add(arrow)
                elif key == arrow.direction:
                    directions = []
                    for far_arrow in arrows_to_evaluate:
                        directions.append(far_arrow.direction)
                        if arrow.direction == far_arrow.direction and arrow.rect.y > far_arrow.rect.y:
                            arrows_to_evaluate.remove(far_arrow)
                            arrows_to_evaluate.add(arrow)
                    if arrow.direction not in directions:
                        arrows_to_evaluate.add(arrow)


        for arrow in arrows_to_evaluate:
            if arrow.rect.y + ARROW_HEIGHT > SCREENY - 2 * ARROW_HEIGHT + 16 and arrow.rect.y < SCREENY - ARROW_HEIGHT - 16:
                self.score += 100 - abs(SCREENY - 2 * ARROW_HEIGHT - arrow.rect.y)
                self.shown_arrows.remove(arrow)
            else:
                self.score -= 10
                self.shown_arrows.remove(arrow)
        for arrow in end_arrows:
            self.score -= 10
            self.shown_arrows.remove(arrow)
        self.pressed_keys = []
        for arrow in self.waiting_arrows:
            if arrow.show:
                self.waiting_arrows.remove(arrow)
                self.shown_arrows.add(arrow)
            
        self.shown_arrows.update()
        self.shown_arrows.draw(self.screen)
        self.score_arrows.update()
        self.score_arrows.draw(self.screen)


    def draw_window(self):
        self.screen.blit(self.background, (0,0))
        self.old_rects.clear()
        self.handle_arrows()
        if len(self.waiting_arrows) == 0 and len(self.shown_arrows) == 0:
            game_over_text()
            if not self.score_updated:
                leaderboard(self.score, self.song.name)
            self.game_over = True
            self.score_updated = True
        show_value('SCORE: ', self.score, 10, 10, 32)


        pg.display.update()







    def play_game(self):
        while not self.play_again:
            self.clock.tick(self.fps)
            self.handle_events()
            self.new_shown_arrow()
            self.move_arrows()
            self.draw_window()
            self.frames += 1
        return self.fullscreen


class Menu:
    def __init__(self, screenX, screenY, bg_colour, fullscreen):
        pg.init()
        self.screen = pg.display.set_mode((screenX, screenY), RESIZABLE)
        if fullscreen:

            self.screenY, self.screenX = screenY, screenX
            self.screensize_mod = 2
        else:
            self.screenX = screenX
            self.screenY = screenY

        self.song_font = pg.font.Font('freesansbold.ttf', 64)
        self.menu_font = pg.font.Font('freesansbold.ttf', 100)

        self.bg_colour = bg_colour
        self.fullscreen = fullscreen
        self.picked_game = False
        self.picked_leaderboard = False
        self.song = None

        self.words = []
        self.leaderboards = []



        self.leaderboard_image = load_leaderboard_image()
        self.render_names()
    


    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN:
                if event.type == pg.QUIT or event.key == pg.K_q:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    mouse_rect = pg.Rect(x, y, 1, 1)
                    if mouse_rect.collidelist(self.words) != -1:
                        self.song_position = mouse_rect.collidelist(self.words)
                        self.picked_game = True
                    elif mouse_rect.collidelist(self.leaderboards) != -1:
                        self.leaderboard_position = mouse_rect.collidelist(self.leaderboards)
                        self.picked_leaderboard = True
            if event.type == pg.VIDEORESIZE:
                self.screenX, self.screenY = (event.dict['size'])


    def render_names(self):
        self.screen.fill(self.bg_colour)
        prompt_word = ['M', 'E', 'N', 'U']
        for letter in prompt_word:
            letter_render = self.menu_font.render(letter, True, (255, 125, 55))
            self.screen.blit(letter_render, (10, self.screenY//2 - 230 + 120 * prompt_word.index(letter)))
        current_line = 0
        for song in songs:
            name = song.name
            width, height = self.song_font.size(f'{name}')
            song_x = 130
            song_y = height * current_line  + 36 * (current_line + 1)
            leaderboard_x = song_x + width + 10
            leaderboard_y = song_y
            name = self.song_font.render(f'{name}', True, LAVENDER)
            self.words.append(pg.Rect(song_x, song_y, width, height))
            self.leaderboards.append(pg.Rect(leaderboard_x, leaderboard_y, 64, 64))
            self.screen.blit(self.leaderboard_image, (leaderboard_x, leaderboard_y))
            self.screen.blit(name, (song_x, song_y))
            current_line += 1

        pg.display.update()

    def choosing_screen(self):
        while not self.picked_game and not self.picked_leaderboard:
            self.handle_events()
            self.render_names()


        if self.picked_game:
            self.song = songs[self.song_position]
            return self.song, 'game', self.fullscreen
        if self.picked_leaderboard:

            self.leadboard = songs[self.leaderboard_position]
            return self.leadboard, 'leaderboard', self.fullscreen


class Leaderboards:
    def __init__(self, screenX, screenY, bg_colour, song_name, fullscreen):
        pg.init()
        self.screen = pg.display.set_mode((screenX, screenY), RESIZABLE)
        self.screenX = screenX
        self.screenY = screenY
        self.bg_colour = bg_colour
        self.song_name = song_name.name
        self.fullscreen = fullscreen
        self.display_leaderboard()
        self.closed = False


    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = pg.mouse.get_pos()
                    mouse_rect = pg.Rect(x, y, 1, 1)
                    if mouse_rect.colliderect(self.exit_rect):
                        self.closed = True
            if event.type == pg.VIDEORESIZE:
                self.screenX, self.screenY = (event.dict['size'])

    def display_leaderboard(self):
        self.screen.fill(self.bg_colour)
        file_path = os.path.join(os.getcwd(), 'leaderboards', (self.song_name + '.txt'))
        with open(file_path, 'r') as high_scores:
            scores = [score[:-1] for score in high_scores.readlines()]
            title_font = pg.font.Font('freesansbold.ttf', 100)
            score_font = pg.font.Font('freesansbold.ttf', 50)
            title_string = self.song_name
            title_length, title_height = title_font.size(title_string)
            title_render = title_font.render(title_string, True, LAVENDER)
            title_x = self.screenX // 2 - title_length // 2
            title_y = 10
            self.screen.blit(title_render, (title_x, title_y))
            current_line = 0
            fit = (self.screenY - 120) // 70 if (self.screenY - 120) // 70 != 0 else 1
            for score in scores:
                score_render = score_font.render(f'{score}', True, BLACK)
                score_x = 10 + (current_line // fit) * 200
                score_y = 50 * (current_line % fit)  +  20 * (current_line % fit + 1) + 100
                self.screen.blit(score_render, (score_x, score_y))
                current_line += 1
        exit_font = pg.font.Font('freesansbold.ttf', 32)
        exit_render = exit_font.render('EXIT', True, WHITE)
        exit_length, exit_height = exit_font.size('EXIT')
        exit_x = self.screenX - exit_length * 1.5
        exit_y = self.screenY - exit_height * 1.5
        self.exit_rect = pg.Rect(exit_x, exit_y, exit_length, exit_height)
        self.screen.blit(exit_render, (exit_x, exit_y))
        pg.display.update()

    def leaderboard_screen(self):
        while not self.closed:
            self.handle_events()
            self.display_leaderboard()
        return self.fullscreen