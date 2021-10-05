# PYGAME BOILERPLATE CODE
# JRYZKNS 2021
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

RES = (1200, 600)
MAX_FPS = 60

import time
import pygame as pg
pg.init()

game_win = pg.display.set_mode(RES)

running, paused, dt = True, False, 0
prev = time.time()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                paused = not paused

    now = time.time()
    dt = min(now - prev, 1/MAX_FPS)

    if not paused:
        pass # actual game code

    # draws
    pg.display.flip()
    prev = now
