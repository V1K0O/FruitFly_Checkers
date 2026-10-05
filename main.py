import pygame

from game.game import Game
from ui.pygame_board import PygameBoard


WIDTH = 800
HEIGHT = 800


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHECKERAI")

game = Game()
renderer = PygameBoard(screen)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            col = x // 100
            row = y // 100

            position = (row, col)

            if game.selected_piece is None:

                if game.select_piece(position):
                    print("Selected:", position)

            else:

                if game.make_move(position):

                    print("Move successful")

                else:

                    print("Illegal move!")

    renderer.draw(game.board)

    pygame.display.flip()


pygame.quit()