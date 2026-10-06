import random

from game.pieces import (
    RED,
    BLUE,
)


class HeuristicAgent:

    def __init__(self, player):

        self.player = player

        # Piece values
        self.PIECE_VALUE = 100
        self.KING_VALUE = 175

        # Move bonuses
        self.CAPTURE_BONUS = 80
        self.KING_BONUS = 120

        # Position bonuses
        self.CENTER_BONUS = 5
        self.ADVANCEMENT_BONUS = 3

        # Mobility
        self.MOBILITY_BONUS = 2

    # =========================================================
    # CHOOSE MOVE
    # =========================================================

    def choose_move(self, game):

        legal_moves = game.get_legal_moves()

        if not legal_moves:
            return None

        best_score = float("-inf")
        best_moves = []

        for move in legal_moves:

            score = self.evaluate_move(
                game,
                move
            )

            if score > best_score:

                best_score = score

                best_moves = [move]

            elif score == best_score:

                best_moves.append(move)

        # If several moves have the same score,
        # choose randomly between them.

        chosen_move = random.choice(best_moves)

        print(
            "AI:",
            chosen_move,
            "Score:",
            best_score
        )

        return chosen_move

    # =========================================================
    # EVALUATE A MOVE
    # =========================================================

    def evaluate_move(self, game, move):

        score = 0

        # -----------------------------------------------------
        # 1. CAPTURE
        # -----------------------------------------------------

        if move.is_capture:

            score += self.CAPTURE_BONUS

            # Capturing a king is more valuable

            captured_piece = game.board.get(
                move.captured
            )

            if self.is_king(captured_piece):

                score += 50


        # -----------------------------------------------------
        # 2. PROMOTION
        # -----------------------------------------------------

        piece = game.board.get(
            move.start
        )

        if self.will_become_king(
            piece,
            move.end
        ):

            score += self.KING_BONUS


        # -----------------------------------------------------
        # 3. CENTER CONTROL
        # -----------------------------------------------------

        score += self.center_score(
            move.end
        )


        # -----------------------------------------------------
        # 4. ADVANCEMENT
        # -----------------------------------------------------

        score += self.advancement_score(
            piece,
            move.end
        )


        # -----------------------------------------------------
        # 5. MATERIAL
        # -----------------------------------------------------

        material_score = self.material_score(
            game
        )

        score += material_score


        # -----------------------------------------------------
        # 6. MOBILITY
        # -----------------------------------------------------

        mobility_score = self.mobility_score(
            game
        )

        score += mobility_score


        return score

    # =========================================================
    # MATERIAL SCORE
    # =========================================================

    def material_score(self, game):

        my_score = 0
        opponent_score = 0

        opponent = -self.player

        for row in range(8):

            for col in range(8):

                piece = game.board.get(
                    (row, col)
                )

                # My piece

                if self.belongs_to_player(
                    piece,
                    self.player
                ):

                    if self.is_king(piece):

                        my_score += self.KING_VALUE

                    else:

                        my_score += self.PIECE_VALUE


                # Opponent piece

                elif self.belongs_to_player(
                    piece,
                    opponent
                ):

                    if self.is_king(piece):

                        opponent_score += self.KING_VALUE

                    else:

                        opponent_score += self.PIECE_VALUE

        return my_score - opponent_score

    # =========================================================
    # CENTER SCORE
    # =========================================================

    def center_score(self, position):

        row, col = position

        # Central four columns/rows are valuable

        if 2 <= row <= 5 and 2 <= col <= 5:

            return self.CENTER_BONUS

        return 0

    # =========================================================
    # ADVANCEMENT SCORE
    # =========================================================

    def advancement_score(
        self,
        piece,
        position
    ):

        row, col = position

        # Kings don't need advancement

        if self.is_king(piece):

            return 0

        # RED moves downward

        if self.player == RED:

            return row * self.ADVANCEMENT_BONUS

        # BLUE moves upward

        else:

            return (7 - row) * self.ADVANCEMENT_BONUS

    # =========================================================
    # MOBILITY
    # =========================================================

    def mobility_score(self, game):

        try:

            from game.rules import get_all_moves

            my_moves = get_all_moves(
                game.board,
                self.player
            )

            opponent_moves = get_all_moves(
                game.board,
                -self.player
            )

            return (
                len(my_moves)
                - len(opponent_moves)
            ) * self.MOBILITY_BONUS

        except Exception:

            return 0

    # =========================================================
    # CHECK PROMOTION
    # =========================================================

    def will_become_king(
        self,
        piece,
        destination
    ):

        row, col = destination

        # RED reaches row 7

        if piece == RED:

            return row == 7

        # BLUE reaches row 0

        if piece == BLUE:

            return row == 0

        return False

    # =========================================================
    # CHECK KING
    # =========================================================

    def is_king(self, piece):

        return piece == 2 or piece == -2

    # =========================================================
    # CHECK PLAYER OWNERSHIP
    # =========================================================

    def belongs_to_player(
        self,
        piece,
        player
    ):

        if player == RED:

            return piece == RED or piece == 2

        if player == BLUE:

            return piece == BLUE or piece == -2

        return False