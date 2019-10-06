# PYGAME BOILERPLATE CODE
# JRYZKNS 2019

res = (1200,600)

import pygame as pg

pg.init()
game_win = pg.display.set_mode(res)

running, paused, dt = True, False, 0
game_clock = pg.time.Clock()
game_clock.tick()

while running:

        # CALLBACKS
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == 32:     # kbd constant for spacebar
                        paused = not paused

        dt = game_clock.get_time()/1000.

        if not paused:
                pass # actual game code

        # draws

        pg.display.flip()
        game_clock.tick()
