from .pieces import EMPTY, RED, BLUE


class Board:

    def __init__(self):
        self.grid = self.create_initial_board()

    def create_initial_board(self):

        board = [
            [0] * 8 for _ in range(8)
        ]

        # Red pieces
        board[0][1] = RED
        board[0][3] = RED
        board[0][5] = RED
        board[0][7] = RED

        board[1][0] = RED
        board[1][2] = RED
        board[1][4] = RED
        board[1][6] = RED

        board[2][1] = RED
        board[2][3] = RED
        board[2][5] = RED
        board[2][7] = RED

        # Blue pieces
        board[5][0] = BLUE
        board[5][2] = BLUE
        board[5][4] = BLUE
        board[5][6] = BLUE

        board[6][1] = BLUE
        board[6][3] = BLUE
        board[6][5] = BLUE
        board[6][7] = BLUE

        board[7][0] = BLUE
        board[7][2] = BLUE
        board[7][4] = BLUE
        board[7][6] = BLUE

        return board

    def move_piece(self, start, destination):

        start_row, start_col = start
        dest_row, dest_col = destination

        self.grid[dest_row][dest_col] = self.grid[start_row][start_col]
        self.grid[start_row][start_col] = EMPTY