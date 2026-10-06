from .board import Board

from .pieces import (
    RED,
    BLUE,
)

from .rules import (
    get_all_moves,
    get_moves_for_piece,
    get_capture_moves,
)


class Game:

    def __init__(self):

        self.board = Board()

        self.current_player = RED

        self.selected_piece = None

        self.winner = None

        self.game_over = False

        self.must_continue_capture = False

    def get_legal_moves(self):

        return get_all_moves(
            self.board,
            self.current_player
        )

    def reset(self):

        self.board = Board()

        self.current_player = RED

        self.selected_piece = None

        self.winner = None

        self.game_over = False

        self.must_continue_capture = False

    # =========================================================
    # COPY GAME
    # =========================================================

    def copy(self):

        new_game = Game()

        # Copy the board
        new_game.board = self.board.copy()

        # Copy game state
        new_game.current_player = self.current_player

        new_game.selected_piece = self.selected_piece

        new_game.winner = self.winner

        new_game.game_over = self.game_over

        new_game.must_continue_capture = (
            self.must_continue_capture
        )

        return new_game

    def select_piece(self, position):

        if self.game_over:
            return False

        piece = self.board.get(position)

        if self.must_continue_capture:

            if position == self.selected_piece:
                return True

            return False

        if self.current_player == RED:

            if piece not in [RED, 2]:
                return False

        elif self.current_player == BLUE:

            if piece not in [BLUE, -2]:
                return False

        legal_moves = get_moves_for_piece(
            self.board,
            position,
            self.current_player
        )

        if not legal_moves:
            return False

        self.selected_piece = position

        return True

    def get_selected_moves(self):

        if self.selected_piece is None:
            return []

        return get_moves_for_piece(
            self.board,
            self.selected_piece,
            self.current_player
        )

    def make_move(self, move):

        if self.game_over:
            return False

        # Get all legal moves
        legal_moves = self.get_legal_moves()

        # Make sure the supplied move is legal
        if move not in legal_moves:
            return False

        # -------------------------
        # MOVE PIECE
        # -------------------------

        self.board.move_piece(
            move.start,
            move.end
        )

        # -------------------------
        # CAPTURE
        # -------------------------

        if move.is_capture:

            self.board.remove_piece(
                move.captured
            )

        # -------------------------
        # PROMOTION
        # -------------------------

        self.board.promote_piece(
            move.end
        )

        # -------------------------
        # CHECK FOR ANOTHER CAPTURE
        # -------------------------

        if move.is_capture:

            next_captures = get_capture_moves(
                self.board,
                move.end
            )

            if next_captures:

                self.selected_piece = move.end

                self.must_continue_capture = True

                return True

        # -------------------------
        # TURN COMPLETE
        # -------------------------

        self.selected_piece = None

        self.must_continue_capture = False

        self.current_player *= -1

        # -------------------------
        # CHECK WIN
        # -------------------------

        self.check_game_over()

        return True

    def check_game_over(self):

        opponent_moves = get_all_moves(
            self.board,
            self.current_player
        )

        opponent_piece_count = (
            self.board.count_pieces(
                self.current_player
            )
        )

        if opponent_piece_count == 0:

            self.winner = -self.current_player

            self.game_over = True

            return

        if not opponent_moves:

            self.winner = -self.current_player

            self.game_over = True

            return