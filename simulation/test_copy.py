from game.game import Game
from game.pieces import RED


game = Game()

print("Original:")
print(game.board.grid)

# Copy the game

copy_game = game.copy()

# Get a legal move

moves = copy_game.get_legal_moves()

print("\nLegal moves:")
for move in moves:
    print(move)

# Make a move on the COPY

if moves:

    copy_game.make_move(moves[0])

print("\nOriginal after modifying copy:")
print(game.board.grid)

print("\nCopy:")
print(copy_game.board.grid)