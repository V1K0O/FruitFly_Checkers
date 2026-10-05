

from .pieces import (
    EMPTY,
    RED,
    RED_KING,
    BLUE,
    BLUE_KING,
    is_red,
    is_blue,
    is_king
)


class Board:

    def __init__(self):

        self.grid = self.create_initial_board()

    def create_initial_board(self):

        board = [
            [EMPTY for _ in range(8)]
            for _ in range(8)
        ]

        # RED

        for row in range(3):

            for col in range(8):

                if (row + col) % 2 == 1:

                    board[row][col] = RED

        # BLUE
        for row in range(5, 8):

            for col in range(8):

                if (row + col) % 2 == 1:

                    board[row][col] = BLUE

        return board

    def get(self, position):

        row, col = position

        return self.grid[row][col]

    def set(self, position, value):

        row, col = position

        self.grid[row][col] = value

    def move_piece(self, start, end):

        piece = self.get(start)

        self.set(start, EMPTY)
        self.set(end, piece)

    def remove_piece(self, position):

        self.set(position, EMPTY)

    def promote_piece(self, position):

        piece = self.get(position)

        row, col = position

        
        if piece == RED and row == 7:

            self.set(position, RED_KING)

        
        elif piece == BLUE and row == 0:

            self.set(position, BLUE_KING)

    def count_pieces(self, player):

        count = 0

        for row in range(8):

            for col in range(8):

                piece = self.grid[row][col]

                if player == RED and is_red(piece):
                    count += 1

                elif player == BLUE and is_blue(piece):
                    count += 1

        return count