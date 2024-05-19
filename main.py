import pygame
import time
import random

print('hello!')

pygame.init()


# temp function of tick (time-control)
def tick(timing: int | float):
    time.sleep(timing)
    pygame.display.update()


# screen initialization with update to cell size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# main loop
run = True

GLOBAL_MOUSE_PRESSED = False

while run:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        # different variations of events goes here...
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            GLOBAL_MOUSE_PRESSED = True

        if event.type == pygame.MOUSEBUTTONUP:
            GLOBAL_MOUSE_PRESSED = False

    if GLOBAL_MOUSE_PRESSED:
        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 100))

    # -------------
    # frame-generation-like
    # -------------
    tick(0.0001)

pygame.quit()
