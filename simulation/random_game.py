from game.game import Game
from game.pieces import RED, BLUE
from agents.random_agents import RandomAgent


game = Game()

red_agent = RandomAgent(RED)
blue_agent = RandomAgent(BLUE)


while not game.game_over:

    if game.current_player == RED:

        move = red_agent.choose_move(game)

    else:

        move = blue_agent.choose_move(game)

    if move is None:

        break

    game.make_move(move)


print("Game finished")

if game.winner == RED:

    print("Winner: RED")

elif game.winner == BLUE:

    print("Winner: BLUE")

else:

    print("No winner")