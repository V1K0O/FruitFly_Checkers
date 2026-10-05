

import pygame

from game.pieces import RED, BLUE


WIDTH = 800
HEIGHT = 800
SQUARE_SIZE = WIDTH // 8

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED_COLOR = (255, 0, 0)
BLUE_COLOR = (0, 0, 255)


class PygameBoard:

    def __init__(self, screen):

        self.screen = screen

    def draw(self, board):

        self.draw_squares()
        self.draw_pieces(board)

    def draw_squares(self):

        for row in range(8):

            for col in range(8):

                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE

                if (row + col) % 2 == 0:
                    color = WHITE
                else:
                    color = BLACK

                pygame.draw.rect(
                    self.screen,
                    color,
                    (x, y, SQUARE_SIZE, SQUARE_SIZE)
                )

    def draw_pieces(self, board):

        for row in range(8):

            for col in range(8):

                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE

                center_x = x + SQUARE_SIZE // 2
                center_y = y + SQUARE_SIZE // 2

                piece = board.grid[row][col]

                if piece == RED:

                    pygame.draw.circle(
                        self.screen,
                        RED_COLOR,
                        (center_x, center_y),
                        SQUARE_SIZE // 2 - 10
                    )

                elif piece == BLUE:

                    pygame.draw.circle(
                        self.screen,
                        BLUE_COLOR,
                        (center_x, center_y),
                        SQUARE_SIZE // 2 - 10
                    )