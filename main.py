import pygame
import time
import random
import functools
from matrix_definition import *
from MovingDot import *
from EmptySpace import *

pygame.init()

# function of tick (time-control)
def tick(timing: int | float):
    time.sleep(timing)
    pygame.display.update()

# matrix preparation
matrix = [[EmptySpace() for j in range(matrix_dimension_x)] for i in range(matrix_dimension_y)]

# screen initialization with update to cell size
screen_width = (cell_gap + cell_length) * matrix_dimension_x + cell_gap
screen_height = (cell_gap + cell_length) * matrix_dimension_y + cell_gap
screen_base_color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height))

# main loop bool
run = True

# mouse interaction variables
GLOBAL_MOUSE_PRESSED = False

while run:

    for event in pygame.event.get():

        # window closing event
        if event.type == pygame.QUIT:
            run = False

        # mouse interaction event
        if event.type == pygame.MOUSEBUTTONDOWN:

            # pressing-nesting of Moving|Empty spaces
            mouse_coor = pygame.mouse.get_pos()
            mouse_matrix_position = [mouse_coor[0] // (cell_length + cell_gap),
                                     (screen_height - mouse_coor[1]) // (cell_length + cell_gap)]

            if isinstance(matrix[mouse_matrix_position[1]][mouse_matrix_position[0]], MovingDot):
                matrix[mouse_matrix_position[1]][mouse_matrix_position[0]] = EmptySpace()
            else:
                matrix[mouse_matrix_position[1]][mouse_matrix_position[0]] = MovingDot()

            GLOBAL_MOUSE_PRESSED = True

        if event.type == pygame.MOUSEBUTTONUP:
            GLOBAL_MOUSE_PRESSED = False

    # ---------
    # drawing section
    # ---------

    # screen fill
    screen.fill(screen_base_color)

    # nesting second matrix (for falling process)

    second_matrix = [[EmptySpace() for j in range(matrix_dimension_x)] for i in range(matrix_dimension_y)]

    for i in range(matrix_dimension_y):
        for j in range(matrix_dimension_x):

            if isinstance(matrix[i][j], MovingDot):

                if i != 0:
                    second_matrix[i][j] = EmptySpace()
                    second_matrix[i - 1][j] = MovingDot()
                else:
                    second_matrix[i][j] = MovingDot()

    # drawing matrix
    for i in range(matrix_dimension_y):
        for j in range(matrix_dimension_x):
            pygame.draw.rect(screen, second_matrix[i][j].get_color(), (cell_gap + ((cell_length + cell_gap) * j),
                                                                       screen_height - cell_gap - cell_length - (
                                                                               cell_gap + cell_length) * i,
                                                                       cell_length,
                                                                       cell_length))

    if GLOBAL_MOUSE_PRESSED:
        pygame.draw.rect(screen, (150, 150, 150), (10, 30, 10, 10))

    if pygame.mouse.get_focused():
        pygame.draw.rect(screen, (150, 150, 150), (10, 10, 10, 10))

    # -------------
    # frame generation
    # -------------
    tick(0.1)

    matrix = second_matrix

pygame.quit()
