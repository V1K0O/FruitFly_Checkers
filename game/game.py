
from .board import Board

from .pieces import (
    RED,
    BLUE,
    EMPTY
)

from .rules import (
    get_all_moves,
    get_moves_for_piece
)


class Game:

    def __init__(self):

        self.board = Board()

        self.current_player = RED

        self.selected_piece = None

        self.winner = None

        self.game_over = False

        self.must_continue_capture = False

    def reset(self):

        self.board = Board()

        self.current_player = RED

        self.selected_piece = None

        self.winner = None

        self.game_over = False

        self.must_continue_capture = False

    def select_piece(self, position):

        if self.game_over:

            return False

        piece = self.board.get(position)

        
        if self.must_continue_capture:

            if position == self.selected_piece:

                return True

            return False


        if (
            self.current_player == RED
            and piece not in [RED, 2]
        ):

            return False

        if (
            self.current_player == BLUE
            and piece not in [BLUE, -2]
        ):

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

    def make_move(self, destination):

        if self.game_over:

            return False

        if self.selected_piece is None:

            return False

        legal_moves = self.get_selected_moves()

        chosen_move = None

        for move in legal_moves:

            if move.end == destination:

                chosen_move = move

                break

        if chosen_move is None:

            return False


        # MOVE PIECE


        self.board.move_piece(
            chosen_move.start,
            chosen_move.end
        )


        # CAPTURE
        

        if chosen_move.is_capture:

            self.board.remove_piece(
                chosen_move.captured
            )

    
        # PROMOTION

        self.board.promote_piece(
            chosen_move.end
        )


        # CHECK FOR ANOTHER CAPTURE


        if chosen_move.is_capture:

            next_captures = []

            from .rules import get_capture_moves

            next_captures = get_capture_moves(
                self.board,
                chosen_move.end
            )

            if next_captures:

                self.selected_piece = chosen_move.end

                self.must_continue_capture = True

                return True

        # TURN COMPLETE


        self.selected_piece = None

        self.must_continue_capture = False

        self.current_player *= -1

        # CHECK WIN

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