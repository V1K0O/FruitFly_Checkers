
def encode_game_state(game):
    """Convert the current Checkers state into JSON-compatible data."""

    board = game.board.grid
    legal_moves = game.get_legal_moves()

    encoded_moves = []

    for move_id, move in enumerate(legal_moves):
        encoded_moves.append({
            "id": move_id,
            "start": list(move.start),
            "end": list(move.end),
            "captured": (
                list(move.captured)
                if move.captured is not None
                else None
            ),
        })

    return {
        "player": game.current_player,
        "board": [list(row) for row in board],
        "legal_moves": encoded_moves,
    }
