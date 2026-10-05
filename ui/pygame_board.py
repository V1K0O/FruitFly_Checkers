

import pygame

from game.pieces import (
    RED,
    RED_KING,
    BLUE,
    BLUE_KING
)


WIDTH = 800
HEIGHT = 800

SQUARE_SIZE = WIDTH // 8


WHITE = (245, 245, 245)
BLACK = (40, 40, 40)

RED_COLOR = (220, 50, 50)
BLUE_COLOR = (50, 100, 220)

SELECT_COLOR = (255, 215, 0)
MOVE_COLOR = (100, 220, 100)

TEXT_COLOR = (255, 255, 255)


class PygameBoard:

    def __init__(self, screen):

        self.screen = screen

        self.font = pygame.font.Font(
            None,
            36
        )

    def draw(self, game):

        self.draw_squares()

        self.draw_moves(game)

        self.draw_pieces(game.board)

        self.draw_status(game)

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
                    (
                        x,
                        y,
                        SQUARE_SIZE,
                        SQUARE_SIZE
                    )
                )

    def draw_pieces(self, board):

        for row in range(8):

            for col in range(8):

                piece = board.get(
                    (row, col)
                )

                if piece == 0:
                    continue

                center_x = (
                    col * SQUARE_SIZE
                    + SQUARE_SIZE // 2
                )

                center_y = (
                    row * SQUARE_SIZE
                    + SQUARE_SIZE // 2
                )

                if piece in [RED, RED_KING]:

                    color = RED_COLOR

                else:

                    color = BLUE_COLOR

                pygame.draw.circle(
                    self.screen,
                    color,
                    (
                        center_x,
                        center_y
                    ),
                    SQUARE_SIZE // 2 - 10
                )

                # King marker
                if piece in [RED_KING, BLUE_KING]:

                    pygame.draw.circle(
                        self.screen,
                        (255, 215, 0),
                        (
                            center_x,
                            center_y
                        ),
                        15,
                        4
                    )

    def draw_moves(self, game):

        if game.selected_piece is None:

            return

        row, col = game.selected_piece

        x = col * SQUARE_SIZE
        y = row * SQUARE_SIZE

        pygame.draw.rect(
            self.screen,
            SELECT_COLOR,
            (
                x,
                y,
                SQUARE_SIZE,
                SQUARE_SIZE
            ),
            5
        )

        moves = game.get_selected_moves()

        for move in moves:

            row, col = move.end

            center_x = (
                col * SQUARE_SIZE
                + SQUARE_SIZE // 2
            )

            center_y = (
                row * SQUARE_SIZE
                + SQUARE_SIZE // 2
            )

            pygame.draw.circle(
                self.screen,
                MOVE_COLOR,
                (
                    center_x,
                    center_y
                ),
                12
            )

    def draw_status(self, game):

        if game.game_over:

            if game.winner == RED:

                text = "RED WINS!"

            else:

                text = "BLUE WINS!"

        else:

            if game.current_player == RED:

                text = "RED TURN"

            else:

                text = "BLUE TURN"

            if game.must_continue_capture:

                text += " - CONTINUE CAPTURE"

        surface = self.font.render(
            text,
            True,
            TEXT_COLOR
        )

        self.screen.blit(
            surface,
            (10, 10)
        )