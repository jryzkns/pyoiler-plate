# PYGAME BOILERPLATE CODE
# JRYZKNS 2019

res = (1200,600)


import pygame as pg
import time

pg.init()
clock = pg.time.Clock()
game_win = pg.display.set_mode(res)
running, paused, t, dt = True, False, pg.time.get_ticks(), 0

while running:

        # CALLBACKS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                print(event)
                if event.key == 32:     # kbd constant for spacebar
                        paused = not paused
                        print('flick')

        dt = (pg.time.get_ticks() - t)/1000.0

        if not paused:
                # actual game code

        pg.display.flip()

        t = pg.time.get_ticks()