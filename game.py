# src/checkers/game.py

from .board import Board
from .pieces import RED, BLUE
from .rules import is_legal_move


class Game:

    def __init__(self):

        self.board = Board()

        self.current_player = RED

        self.selected_piece = None

    def select_piece(self, position):

        row, col = position

        if self.board.grid[row][col] == self.current_player:

            self.selected_piece = position

            return True

        return False

    def make_move(self, destination):

        if self.selected_piece is None:
            return False

        if not is_legal_move(
            self.board,
            self.selected_piece,
            destination
        ):
            return False

        self.board.move_piece(
            self.selected_piece,
            destination
        )

        self.current_player *= -1

        self.selected_piece = None

        return True