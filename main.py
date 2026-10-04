import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800
SQUARE_SIZE = WIDTH // 8

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)


board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

board[0][1] = 1
board[0][3] = 1
board[0][5] = 1
board[0][7] = 1


board[1][0] = 1
board[1][2] = 1
board[1][4] = 1
board[1][6] = 1


board[2][1] = 1
board[2][3] = 1
board[2][5] = 1
board[2][7] = 1



board[5][0] = -1
board[5][2] = -1
board[5][4] = -1
board[5][6] = -1

# Row 6 -> columns 1,3,5,7
board[6][1] = -1
board[6][3] = -1
board[6][5] = -1
board[6][7] = -1

# Row 7 -> columns 0,2,4,6
board[7][0] = -1
board[7][2] = -1
board[7][4] = -1
board[7][6] = -1


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHECKERAI")

running = True
selected_piece = None

while running:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        #MOUSE CLICK CHECK
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_click, y_click = event.pos

            col = x_click // SQUARE_SIZE
            row = y_click // SQUARE_SIZE
            
            print("row =", row, "col =", col)
            if selected_piece is None:
                if board[row][col]==1 or board[row][col]==-1:
                    selected_piece=(row,col)
            else:
                old_row, old_col = selected_piece
                if board[row][col] == 0:
                    board[row][col] = board[old_row][old_col]
                    board[old_row][old_col] = 0
                    print("Moved from",selected_piece,"to",(row, col))
                else:
                    print("Cannot move there!")
                selected_piece = None

    for row in range(8):
        for col in range(8):

            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE

            if (row + col) % 2 == 0:
                color = white
            else:
                color = black

            pygame.draw.rect(
                screen,
                color,
                (x, y, SQUARE_SIZE, SQUARE_SIZE)
            )




    for row in range(8):
        for col in range(8):

            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE

            center_x = x + SQUARE_SIZE // 2
            center_y = y + SQUARE_SIZE // 2

            if board[row][col] == 1:

                pygame.draw.circle(
                    screen,
                    red,
                    (center_x, center_y),
                    SQUARE_SIZE // 2 - 10
                )

            elif board[row][col] == -1:

                pygame.draw.circle(
                    screen,
                    blue,
                    (center_x, center_y),
                    SQUARE_SIZE // 2 - 10
                )


    pygame.display.flip()


pygame.quit()