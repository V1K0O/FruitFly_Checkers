# src/checkers/rules.py

from .pieces import RED, BLUE


def is_legal_move(board, start, destination):

    start_row, start_col = start
    dest_row, dest_col = destination

    # Destination must be inside board
    if not (0 <= dest_row < 8 and 0 <= dest_col < 8):
        return False

    # Destination must be empty
    if board.grid[dest_row][dest_col] != 0:
        return False

    piece = board.grid[start_row][start_col]

    # Blue moves upward
    if piece == BLUE:

        if (
            start_row - dest_row == 1
            and abs(start_col - dest_col) == 1
        ):
            return True

    # Red moves downward
    elif piece == RED:

        if (
            dest_row - start_row == 1
            and abs(dest_col - start_col) == 1
        ):
            return True

    return False