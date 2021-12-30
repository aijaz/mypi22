import pygame
from pygame.constants import *
import math

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)
screen_size = (470, 620)
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font(None, 32)

running = True

hill = [
    ('#             @'),
    ('               '),
    ('               '),
    (' @  #          '),
    ('               '),
    ('               '),
    ('       @    @  '),
    ('               '),
    ('               '),
    ('     @    @    '),
    ('               '),
    ('               '),
    (' @  #          '),
    ('               '),
    ('               '),
    ('       @    @  '),
    ('               '),
    ('               '),
    ('     @    @    '),
    ('               '),]


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text

y_speed = 0.25
x_speed = 0.25
offset = 0
bg = pygame.image.load('images/bg.jpeg').convert()
rock = pygame.transform.scale(pygame.image.load('images/rock.png'), (30, 30)).convert_alpha()
snowman = pygame.transform.scale(pygame.image.load('images/snowman.png'), (30, 30)).convert_alpha()
ski_right = pygame.transform.scale(pygame.image.load('images/ski_right.png'), (30, 30)).convert_alpha()
ski_left = pygame.transform.scale(pygame.image.load('images/ski_left.png'), (30, 30)).convert_alpha()


screen.blit(bg, (0, 0))

first = True
skier_direction = 'right'
skier_location = 235
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_h:
                skier_direction = 'left'
            elif event.key == K_j:
                skier_direction = 'right'

    if game_over:
        continue

    # screen.blit(bg, (0, 0))
    dirty_rects = []

    # erase skier
    old_skier_rect = (skier_location, 10, 30, 30)
    dirty_rects.append(old_skier_rect)
    screen.blit(bg, old_skier_rect, old_skier_rect)

    for y, row in enumerate(hill):
        for x, item in enumerate(row):
            old_rect = pygame.Rect((int(10 + x * 30), int(10 + y * 30 - offset + y_speed), 30, 30))
            dirty_rects.append(old_rect)
            if first:
                first = False
            else:
                # erase old locations
                screen.blit(bg, old_rect, old_rect)

            new_location = pygame.Rect((10 + x * 30, int(10 + y * 30 - offset), 30, 30))
            dirty_rects.append(new_location)

            if item == '@':
                screen.blit(snowman, new_location)
            elif item == '#':
                screen.blit(rock, new_location)

    # move skier
    if skier_direction == 'right':
        skier_location += x_speed
        if skier_location > 420:
            skier_location = 420
        skier_image = ski_right
    else:
        skier_location -= x_speed
        if skier_location < 10:
            skier_location = 10
        skier_image = ski_left


    # draw skier
    new_skier_rect = pygame.Rect(int(skier_location), 10, 30, 30)
    screen.blit(skier_image, new_skier_rect)
    dirty_rects.append(new_skier_rect)

    # screen.blit(bg, (10, 0, 50, 50), (10, 0, 50, 50))
    # screen.blit(update_fps(), (10,0))

    pygame.display.update(dirty_rects)

    # check for collision
    for x, item in enumerate(hill[0]):
        skier_x = skier_location
        skier_y = 10
        if item != ' ':
            item_x = -30 + 10 + (x * 30)
            item_y = int(10 - offset)
        distance = math.sqrt(math.pow(skier_x - item_x, 2) + (math.pow(skier_y - item_y, 2)))

        if distance < 25 and skier_y <= item_y:
            game_over = True
            break

    offset += y_speed
    if offset == 30:
        offset = 0
        hill.append(hill.pop(0))
