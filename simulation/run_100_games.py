from game.game import Game
from game.pieces import RED, BLUE
from agents.random_agents import RandomAgent
from agents.heuristic_agent import HeuristicAgent
from agents.minimax_agent import MinimaxAgent


NUM_GAMES = 50

red_wins = 0
blue_wins = 0
draws = 0


for game_number in range(1, NUM_GAMES + 1):

    game = Game()

    red_agent = RandomAgent(RED)
    blue_agent = MinimaxAgent(BLUE,depth=3)

    move_count = 0

    while not game.game_over:

        if game.current_player == RED:

            move = red_agent.choose_move(game)

        else:

            move = blue_agent.choose_move(game)

        if move is None:
            break

        game.make_move(move)

        move_count += 1

    # -------------------------
    # RECORD RESULT
    # -------------------------

    if game.winner == RED:

        red_wins += 1

    elif game.winner == BLUE:

        blue_wins += 1

    else:

        draws += 1

    print(
        f"Game {game_number}: "
        f"Winner = {game.winner}, "
        f"Moves = {move_count}"
    )


# -------------------------
# FINAL RESULTS
# -------------------------

print()
print("======================")
print("SIMULATION COMPLETE")
print("======================")

print("Games:", NUM_GAMES)
print("RED wins:", red_wins)
print("BLUE wins:", blue_wins)
print("Draws:", draws)

print()
print("RED win rate:", red_wins / NUM_GAMES * 100, "%")
print("BLUE win rate:", blue_wins / NUM_GAMES * 100, "%")