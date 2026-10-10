
from game.game import Game
from flybrain.client import request_move

game = Game()

print("Current player:", game.current_player)
print("Legal moves:", game.get_legal_moves())

move = request_move(game)

print("\nMove returned by R:", move)
print("Move is legal:", move in game.get_legal_moves())
