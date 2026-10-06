# main.py

import pygame

from game.game import Game
from ui.pygame_board import PygameBoard
from agents.random_agents import RandomAgent


# -------------------------
# SETTINGS
# -------------------------

WIDTH = 800
HEIGHT = 800

SQUARE_SIZE = WIDTH // 8

HUMAN_PLAYER = 1
AI_PLAYER = -1


# -------------------------
# INITIALIZE PYGAME
# -------------------------

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "FlyCheckers"
)

clock = pygame.time.Clock()


# -------------------------
# GAME
# -------------------------

game = Game()

renderer = PygameBoard(
    screen
)

agent = RandomAgent(AI_PLAYER)


# -------------------------
# MAIN LOOP
# -------------------------

running = True

while running:

    # -------------------------
    # EVENTS
    # -------------------------

    for event in pygame.event.get():

        # QUIT

        if event.type == pygame.QUIT:

            running = False


        # -------------------------
        # KEYBOARD
        # -------------------------

        elif event.type == pygame.KEYDOWN:

            # Restart game

            if event.key == pygame.K_r:

                game.reset()

                print("Game restarted")


        # -------------------------
        # MOUSE
        # -------------------------

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if game.game_over:

                continue

            # Only allow human to play RED

            if game.current_player != HUMAN_PLAYER:

                continue

            x, y = event.pos

            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE

            position = (
                row,
                col
            )


            # -------------------------
            # SELECT PIECE
            # -------------------------

            if game.selected_piece is None:

                if game.select_piece(position):

                    print(
                        "Selected:",
                        position
                    )

                else:

                    print(
                        "Cannot select:",
                        position
                    )


            # -------------------------
            # MAKE MOVE
            # -------------------------

            else:

                selected_moves = game.get_selected_moves()

                chosen_move = None

                # Find the Move object
                # whose destination was clicked

                for move in selected_moves:

                    if move.end == position:

                        chosen_move = move

                        break


                if chosen_move is not None:

                    if game.make_move(chosen_move):

                        print(
                            "Move:",
                            chosen_move
                        )

                    else:

                        print(
                            "Illegal move"
                        )

                else:

                    print(
                        "Illegal destination"
                    )


    # -------------------------
    # RANDOM AI TURN
    # -------------------------

    if (
        not game.game_over
        and
        game.current_player == AI_PLAYER
    ):

        ai_move = agent.choose_move(game)

        if ai_move is not None:

            print(
                "AI chose:",
                ai_move
            )

            game.make_move(ai_move)


    # -------------------------
    # DRAW
    # -------------------------

    renderer.draw(game)

    pygame.display.flip()

    clock.tick(60)


# -------------------------
# EXIT
# -------------------------

pygame.quit()