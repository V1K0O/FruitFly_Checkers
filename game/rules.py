

from .pieces import (
    EMPTY,
    RED,
    BLUE,
    is_red,
    is_blue,
    is_king
)

from .move import Move


DIRECTIONS = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]


def is_inside_board(row, col):

    return (
        0 <= row < 8
        and
        0 <= col < 8
    )


def belongs_to_player(piece, player):

    if player == RED:

        return is_red(piece)

    if player == BLUE:

        return is_blue(piece)

    return False


def get_move_directions(piece):

    
    if is_king(piece):

        return DIRECTIONS

    
    if piece == RED:

        return [
            (1, -1),
            (1, 1)
        ]

    
    if piece == BLUE:

        return [
            (-1, -1),
            (-1, 1)
        ]

    return []


def get_normal_moves(board, position):

    row, col = position

    piece = board.get(position)

    moves = []

    for dr, dc in get_move_directions(piece):

        new_row = row + dr
        new_col = col + dc

        if not is_inside_board(new_row, new_col):
            continue

        if board.get((new_row, new_col)) == EMPTY:

            moves.append(
                Move(
                    position,
                    (new_row, new_col)
                )
            )

    return moves


def get_capture_moves(board, position):

    row, col = position

    piece = board.get(position)

    moves = []

    for dr, dc in get_move_directions(piece):

        middle_row = row + dr
        middle_col = col + dc

        landing_row = row + 2 * dr
        landing_col = col + 2 * dc

        if not is_inside_board(
            landing_row,
            landing_col
        ):
            continue

        if not is_inside_board(
            middle_row,
            middle_col
        ):
            continue

        middle_piece = board.get(
            (middle_row, middle_col)
        )

        landing_piece = board.get(
            (landing_row, landing_col)
        )

        if middle_piece == EMPTY:
            continue

        if belongs_to_player(
            middle_piece,
            RED if is_blue(piece) else BLUE
        ):

            if landing_piece == EMPTY:

                moves.append(
                    Move(
                        position,
                        (landing_row, landing_col),
                        captured=(middle_row, middle_col)
                    )
                )

    return moves


def get_piece_moves(board, position):

    capture_moves = get_capture_moves(
        board,
        position
    )

    if capture_moves:

        return capture_moves

    return get_normal_moves(
        board,
        position
    )


def get_all_moves(board, player):

    all_moves = []

    capture_moves = []

    # First find ALL captures
    for row in range(8):

        for col in range(8):

            position = (row, col)

            piece = board.get(position)

            if belongs_to_player(piece, player):

                captures = get_capture_moves(
                    board,
                    position
                )

                capture_moves.extend(captures)

    # Mandatory capture rule
    if capture_moves:

        return capture_moves

    
    for row in range(8):

        for col in range(8):

            position = (row, col)

            piece = board.get(position)

            if belongs_to_player(piece, player):

                moves = get_normal_moves(
                    board,
                    position
                )

                all_moves.extend(moves)

    return all_moves


def get_moves_for_piece(board, position, player):

    piece = board.get(position)

    if not belongs_to_player(piece, player):

        return []

    all_player_moves = get_all_moves(
        board,
        player
    )

    piece_moves = []

    for move in all_player_moves:

        if move.start == position:

            piece_moves.append(move)

    return piece_moves