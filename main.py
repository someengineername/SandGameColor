import pygame
import time
import random
import functools

pygame.init()


# temp function of tick (time-control)
def tick(timing: int | float):
    time.sleep(timing)
    pygame.display.update()


# screen initialization with update to cell size
screen_width = 800
screen_height = 600
screen_base_color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))

# main loop
run = True

# mouse interaction variables
GLOBAL_MOUSE_PRESSED = False


# class of pixel - to draw with some
class MovingDot:
    def __init__(self, int1=50, int2=50, int3=50):
        self._color = (int1, int2, int3)

    def get_color(self):
        return self._color


class EmptySpace:
    def __init__(self):
        self._color = (20, 20, 20)

    def get_color(self):
        return self._color


# matrix preparation
matrix_dimension_y = 10
matrix_dimension_x = 15
cell_length = 25
cell_gap = 2
matrix = [[EmptySpace() for j in range(matrix_dimension_y)] for i in range(matrix_dimension_x)]

matrix[5][5] = MovingDot()

while run:

    for event in pygame.event.get():

        # window closing event
        if event.type == pygame.QUIT:
            run = False

        # mouse interaction event

        if event.type == pygame.MOUSEBUTTONDOWN:
            GLOBAL_MOUSE_PRESSED = True

        if event.type == pygame.MOUSEBUTTONUP:
            GLOBAL_MOUSE_PRESSED = False

    # ---------
    # drawing section
    # ---------

    # screen fill
    screen.fill(screen_base_color)

    # draw base matrix
    for i in range(matrix_dimension_x):
        for j in range(matrix_dimension_y):

            if isinstance(matrix[i][j], MovingDot):
                pygame.draw.rect(screen, matrix[i][j].get_color(), (i * (cell_length + cell_gap) + cell_gap,
                                                                    j * (cell_length + cell_gap) + cell_gap,
                                                                    cell_length, cell_length))
            else:
                pygame.draw.rect(screen, matrix[i][j].get_color(), (i * (cell_length + cell_gap) + cell_gap,
                                                                    j * (cell_length + cell_gap) + cell_gap,
                                                                    cell_length, cell_length))

    if GLOBAL_MOUSE_PRESSED:
        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 100))

    if pygame.mouse.get_focused():
        pygame.draw.rect(screen, (150, 150, 150), (10, 10, 10, 10))

    # -------------
    # frame generation
    # -------------
    tick(0.0001)

pygame.quit()
