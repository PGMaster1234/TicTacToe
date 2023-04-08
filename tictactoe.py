import pygame
import math
import random
import time
pygame.init()

# ---------------- Stuff
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((1200, 650))
clock = pygame.time.Clock()
fps = 60
screen_width = screen.get_width()
screen_height = screen.get_height()
screen2 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screen3 = pygame.Surface((screen_width, screen_height)).convert_alpha()
timer = 0
shake = [0, 0]
tile_size = (screen_height - 240) / 3


class Endesga:
    maroon_red = (87, 28, 39)
    lighter_maroon_red = (127, 36, 51)
    dark_green = (9, 26, 23)
    light_brown = (191, 111, 74)
    black = (19, 19, 19)
    dark_blue = (26, 25, 50)
    grey_blue = (66, 76, 110)
    cream = (237, 171, 80)
    white = (255, 255, 255)
    very_light_blue = (199, 207, 221)


tiles = [[[pygame.rect.Rect(370, 100, tile_size, tile_size), 0], [pygame.rect.Rect(370 + tile_size, 100, tile_size, tile_size), 0], [pygame.rect.Rect(370 + tile_size * 2, 100, tile_size, tile_size), 0]],
         [[pygame.rect.Rect(370, 100 + tile_size, tile_size, tile_size), 0], [pygame.rect.Rect(370 + tile_size, 100 + tile_size, tile_size, tile_size), 0], [pygame.rect.Rect(370 + tile_size * 2, 100 + tile_size, tile_size, tile_size), 0]],
         [[pygame.rect.Rect(370, 100 + tile_size * 2, tile_size, tile_size), 0], [pygame.rect.Rect(370 + tile_size, 100 + tile_size * 2, tile_size, tile_size), 0], [pygame.rect.Rect(370 + tile_size * 2, 100 + tile_size * 2, tile_size, tile_size), 0]]]


controller = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sums = [0, 0, 0, 0, 0, 0, 0, 0]


def CalcSums(cont):
    su = [0, 0, 0, 0, 0, 0, 0, 0]
    for c, r in enumerate(cont):
        for v, t in enumerate(r):
            su[c] += cont[c][v]
            su[v + 3] += cont[c][v]
            if c == v:
                su[6] += cont[c][v]
            if c + v == 2:
                su[7] += cont[c][v]
    print(su)
    return su


def botMove(su, con):
    for q, s in enumerate(su):
        if s == 20:
            for a in con[q]:
                if a != 10:
                    con[q][a] = 1
    return con


# CalcSums(controller)
last_time = time.time()
running = True
while running:

    # ---------------- Reset stuff
    click = False
    mx, my = pygame.mouse.get_pos()
    screen.fill(Endesga.dark_blue)
    screen2.fill(Endesga.dark_blue)
    screen3.fill((0, 0, 0, 0))
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()
    timer -= 1 * dt
    shake = 0, 0

    # ---------------- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    x = 0
    y = 0
    for row in tiles:
        for tile in row:
            controller[y][x] = tile[1]
            if tile[1] == 0:
                pygame.draw.rect(screen2, Endesga.black, tile[0], 0, 15)
            if tile[1] == 1:
                pygame.draw.rect(screen2, Endesga.maroon_red, tile[0], 0, 15)
            if tile[1] == 10:
                pygame.draw.rect(screen2, Endesga.grey_blue, tile[0], 0, 15)
            if tile[0].collidepoint((mx, my)):
                if click:
                    tile[1] = 10
            x += 1
        y += 1
        x = 0
    sums = CalcSums(controller)
    controller = botMove(sums, controller)

    # ---------------- End frame
    pygame.mouse.set_visible(False)
    pygame.draw.circle(screen3, Endesga.white, (mx, my), 5, 1)
    screen.blit(screen2, (shake[0], shake[1]))
    screen.blit(screen3, (0, 0))
    pygame.display.update()
    clock.tick(fps)
