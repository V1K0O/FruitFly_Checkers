import random

from game.pieces import (
    RED,
    BLUE,
    RED_KING,
    BLUE_KING,
)

from game.rules import get_all_moves


class MinimaxAgent:

    def __init__(self, player, depth=2):

        self.player = player
        self.depth = depth

        # Piece values
        self.PIECE_VALUE = 100
        self.KING_VALUE = 175

        # Positional values
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

            simulated_game = game.copy()

            simulated_game.make_move(move)

            # Finish multiple capture sequence
            simulated_game = self.finish_capture_sequence(
                simulated_game
            )

            # -------------------------------------------------
            # ALPHA-BETA SEARCH
            # -------------------------------------------------

            score = self.minimax(
                simulated_game,
                self.depth - 1,
                False,
                float("-inf"),
                float("inf")
            )

            if score > best_score:

                best_score = score

                best_moves = [move]

            elif score == best_score:

                best_moves.append(move)

        if not best_moves:
            return None

        # If several moves have the same score,
        # choose randomly between them.
        chosen_move = random.choice(
            best_moves
        )

        print(
            "Minimax:",
            chosen_move,
            "Score:",
            best_score
        )

        return chosen_move

    # =========================================================
    # MINIMAX + ALPHA-BETA PRUNING
    # =========================================================

    def minimax(
        self,
        game,
        depth,
        maximizing,
        alpha,
        beta
    ):

        # -----------------------------------------------------
        # TERMINAL CONDITION
        # -----------------------------------------------------

        if depth == 0 or game.game_over:

            return self.evaluate(game)

        legal_moves = game.get_legal_moves()

        if not legal_moves:

            return self.evaluate(game)

        # =====================================================
        # MAXIMIZING PLAYER
        # =====================================================

        if maximizing:

            best_score = float("-inf")

            for move in legal_moves:

                simulated_game = game.copy()

                simulated_game.make_move(move)

                simulated_game = self.finish_capture_sequence(
                    simulated_game
                )

                score = self.minimax(
                    simulated_game,
                    depth - 1,
                    False,
                    alpha,
                    beta
                )

                best_score = max(
                    best_score,
                    score
                )

                # -------------------------------------------------
                # UPDATE ALPHA
                # -------------------------------------------------

                alpha = max(
                    alpha,
                    best_score
                )

                # -------------------------------------------------
                # ALPHA-BETA PRUNING
                # -------------------------------------------------

                if beta <= alpha:

                    break

            return best_score

        # =====================================================
        # MINIMIZING PLAYER
        # =====================================================

        else:

            best_score = float("inf")

            for move in legal_moves:

                simulated_game = game.copy()

                simulated_game.make_move(move)

                simulated_game = self.finish_capture_sequence(
                    simulated_game
                )

                score = self.minimax(
                    simulated_game,
                    depth - 1,
                    True,
                    alpha,
                    beta
                )

                best_score = min(
                    best_score,
                    score
                )

                # -------------------------------------------------
                # UPDATE BETA
                # -------------------------------------------------

                beta = min(
                    beta,
                    best_score
                )

                # -------------------------------------------------
                # ALPHA-BETA PRUNING
                # -------------------------------------------------

                if beta <= alpha:

                    break

            return best_score

    # =========================================================
    # FINISH MULTI-CAPTURE
    # =========================================================

    def finish_capture_sequence(self, game):

        while game.must_continue_capture:

            position = game.selected_piece

            capture_moves = []

            for move in game.get_legal_moves():

                if move.start == position:

                    capture_moves.append(move)

            # No further capture

            if not capture_moves:

                break

            # -------------------------------------------------
            # TEMPORARY MULTI-CAPTURE HANDLING
            # -------------------------------------------------
            #
            # If multiple continuation captures are available,
            # this currently selects the first one.
            #
            # This is NOT ideal for a perfect Checkers engine.
            #
            # Later we can make Minimax search every possible
            # continuation.
            # -------------------------------------------------

            move = capture_moves[0]

            game.make_move(move)

        return game

    # =========================================================
    # EVALUATE POSITION
    # =========================================================

    def evaluate(self, game):

        # -----------------------------------------------------
        # WINNING POSITION
        # -----------------------------------------------------

        if game.game_over:

            if game.winner == self.player:

                return 100000

            if game.winner == -self.player:

                return -100000

            return 0

        score = 0

        opponent = -self.player

        my_material = 0
        opponent_material = 0

        # =====================================================
        # BOARD
        # =====================================================

        for row in range(8):

            for col in range(8):

                piece = game.board.get(
                    (row, col)
                )

                # =================================================
                # MY PIECE
                # =================================================

                if self.belongs_to_player(
                    piece,
                    self.player
                ):

                    # ---------------------------------------------
                    # MATERIAL
                    # ---------------------------------------------

                    if self.is_king(piece):

                        my_material += (
                            self.KING_VALUE
                        )

                    else:

                        my_material += (
                            self.PIECE_VALUE
                        )

                    # ---------------------------------------------
                    # CENTER BONUS
                    # ---------------------------------------------

                    if (
                        2 <= row <= 5
                        and
                        2 <= col <= 5
                    ):

                        score += (
                            self.CENTER_BONUS
                        )

                    # ---------------------------------------------
                    # ADVANCEMENT BONUS
                    # ---------------------------------------------

                    if not self.is_king(piece):

                        if self.player == RED:

                            score += (
                                row
                                *
                                self.ADVANCEMENT_BONUS
                            )

                        else:

                            score += (
                                (7 - row)
                                *
                                self.ADVANCEMENT_BONUS
                            )

                # =================================================
                # OPPONENT PIECE
                # =================================================

                elif self.belongs_to_player(
                    piece,
                    opponent
                ):

                    # ---------------------------------------------
                    # MATERIAL
                    # ---------------------------------------------

                    if self.is_king(piece):

                        opponent_material += (
                            self.KING_VALUE
                        )

                    else:

                        opponent_material += (
                            self.PIECE_VALUE
                        )

                    # ---------------------------------------------
                    # OPPONENT CENTER CONTROL
                    # ---------------------------------------------

                    if (
                        2 <= row <= 5
                        and
                        2 <= col <= 5
                    ):

                        score -= (
                            self.CENTER_BONUS
                        )

        # =====================================================
        # MATERIAL DIFFERENCE
        # =====================================================

        score += (
            my_material
            -
            opponent_material
        )

        # =====================================================
        # MOBILITY
        # =====================================================

        my_moves = get_all_moves(
            game.board,
            self.player
        )

        opponent_moves = get_all_moves(
            game.board,
            opponent
        )

        score += (
            len(my_moves)
            -
            len(opponent_moves)
        ) * self.MOBILITY_BONUS

        return score

    # =========================================================
    # KING CHECK
    # =========================================================

    def is_king(self, piece):

        return (
            piece == RED_KING
            or
            piece == BLUE_KING
        )

    # =========================================================
    # PLAYER CHECK
    # =========================================================

    def belongs_to_player(
        self,
        piece,
        player
    ):

        if player == RED:

            return (
                piece == RED
                or
                piece == RED_KING
            )

        if player == BLUE:

            return (
                piece == BLUE
                or
                piece == BLUE_KING
            )

        return False