import pygame
import pygame._sdl2 as sdl
import sys
import board as bd
from mines import *

window_width = 1280
window_height = 720
window_flags = (pygame.RESIZABLE | pygame.SCALED)
window = pygame.display.set_mode((window_width, window_height), flags = window_flags)

clock = pygame.time.Clock()

mine_list = makemines(global_mode)
box_list = setboxes(mine_list, global_mode)
cellgroup = pygame.sprite.Group()
Gamebd = bd.GameBoard(mode1, box_list, 500, 9, 3, 10, cellgroup)
# print(Gamebd)
gbd = pygame.sprite.Group(); gbd.add(Gamebd)
# print(gbd)

while True:

    gbd.update()

    gbd.draw(window)
    cellgroup.draw(window)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

    clock.tick(60)
  