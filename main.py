import pygame
import time
import random
from matrix import *
from MovingDot import *
from EmptySpace import *
from ColorCycler import *

pygame.init()


# function of tick (time-control)
def tick(timing: int | float):
    time.sleep(timing)
    pygame.display.update()


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# color cycler init
color_cycler = ColorCycler()

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

                # bottom-side condition
                if i == 0:
                    second_matrix[i][j] = MovingDot(*matrix[i][j].get_color())
                # left-hand side condition
                elif j == 0:
                    # if bottom - empty => move down
                    if isinstance(matrix[i - 1][j], EmptySpace):
                        second_matrix[i - 1][j] = MovingDot(*matrix[i][j].get_color())
                        # second_matrix[i][j] = EmptySpace()
                    # if bottom - busy
                    elif isinstance(matrix[i - 1][j + 1], MovingDot):
                        second_matrix[i][j] = MovingDot(*matrix[i][j].get_color())
                    elif isinstance(matrix[i - 1][j + 1], EmptySpace):
                        second_matrix[i - 1][j + 1] = MovingDot(*matrix[i][j].get_color())
                # right-hand side condition
                elif j == matrix_dimension_x - 1:
                    # if bottom - empty => move down
                    if isinstance(matrix[i - 1][j], EmptySpace):
                        second_matrix[i - 1][j] = MovingDot(*matrix[i][j].get_color())
                        # second_matrix[i][j] = EmptySpace()
                    # if bottom - busy
                    elif isinstance(matrix[i - 1][j - 1], MovingDot):
                        second_matrix[i][j] = MovingDot(*matrix[i][j].get_color())
                    elif isinstance(matrix[i - 1][j - 1], EmptySpace):
                        second_matrix[i - 1][j - 1] = MovingDot(*matrix[i][j].get_color())
                # general behaviour condition
                else:
                    # if bottom is empty
                    if isinstance(matrix[i - 1][j], EmptySpace):
                        second_matrix[i - 1][j] = MovingDot(*matrix[i][j].get_color())
                        second_matrix[i][j] = EmptySpace()
                    # if bottom is occupied
                    else:
                        # if bot-right side occupied
                        if (isinstance(matrix[i - 1][j - 1], MovingDot) and
                                isinstance(matrix[i - 1][j + 1], MovingDot) and
                                isinstance(matrix[i - 1][j], MovingDot)):
                            second_matrix[i][j] = MovingDot(*matrix[i][j].get_color())
                        # if bot-left side occupied
                        elif isinstance(matrix[i - 1][j - 1], MovingDot):
                            # print('lh')
                            second_matrix[i - 1][j + 1] = MovingDot(*matrix[i][j].get_color())
                        # if both sides free => 50|50 %
                        elif (isinstance(matrix[i - 1][j - 1], EmptySpace) and
                              isinstance(matrix[i - 1][j + 1], EmptySpace)):
                            # print('50|50')
                            if random.randint(0, 1) == 1:
                                second_matrix[i - 1][j + 1] = MovingDot(*matrix[i][j].get_color())
                            else:
                                second_matrix[i - 1][j - 1] = MovingDot(*matrix[i][j].get_color())
                        # if everything's occupied
                        elif isinstance(matrix[i - 1][j + 1], MovingDot):
                            # print('rh')
                            second_matrix[i - 1][j - 1] = MovingDot(*matrix[i][j].get_color())

    mouse_coor = pygame.mouse.get_pos()
    mouse_matrix_position = [mouse_coor[0] // (cell_length + cell_gap),
                             (screen_height - mouse_coor[1]) // (cell_length + cell_gap)]

    if pygame.mouse.get_focused():
        if isinstance(matrix[mouse_matrix_position[1]][mouse_matrix_position[0]], EmptySpace) and isinstance(
                matrix[mouse_matrix_position[1] - 1][mouse_matrix_position[0]], EmptySpace):
            second_matrix[mouse_matrix_position[1]][mouse_matrix_position[0]] = MovingDot(
                *color_cycler.get_color_cycle())

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
    tick(0.001)

    matrix = second_matrix

pygame.quit()
