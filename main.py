# main.py

import pygame

from game.game import Game
from ui.pygame_board import PygameBoard


WIDTH = 800
HEIGHT = 800

SQUARE_SIZE = WIDTH // 8


pygame.init()


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "FlyCheckers"
)


game = Game()

renderer = PygameBoard(
    screen
)


clock = pygame.time.Clock()

running = True


while running:

    for event in pygame.event.get():

        # QUIT

        if event.type == pygame.QUIT:

            running = False

        # KEYBOARD

        elif event.type == pygame.KEYDOWN:

            # Restart
            if event.key == pygame.K_r:

                game.reset()

        # MOUSE

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if game.game_over:

                continue

            x, y = event.pos

            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE

            position = (
                row,
                col
            )

            # SELECET

            if game.selected_piece is None:

                if game.select_piece(
                    position
                ):

                    print(
                        "Selected:",
                        position
                    )

            # MOVE

            else:

                if game.make_move(
                    position
                ):

                    print(
                        "Move:",
                        position
                    )

                else:

                    print(
                        "Illegal move"
                    )

    # DRAW

    renderer.draw(game)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()