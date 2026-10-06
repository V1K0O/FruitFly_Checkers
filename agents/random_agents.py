import random


class RandomAgent:

    def __init__(self, player):
        self.player = player

    def choose_move(self, game):

        # Get every legal move for the current player
        legal_moves = game.get_legal_moves()

        # No moves available
        if not legal_moves:
            return None

        # Choose one randomly
        return random.choice(legal_moves)