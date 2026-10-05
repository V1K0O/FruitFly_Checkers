

EMPTY = 0

RED = 1
RED_KING = 2

BLUE = -1
BLUE_KING = -2


def is_red(piece):
    return piece == RED or piece == RED_KING


def is_blue(piece):
    return piece == BLUE or piece == BLUE_KING


def is_king(piece):
    return piece == RED_KING or piece == BLUE_KING


def get_player(piece):

    if is_red(piece):
        return RED

    if is_blue(piece):
        return BLUE

    return EMPTY