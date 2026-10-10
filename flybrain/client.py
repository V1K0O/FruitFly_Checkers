import requests

base_URL="http://127.0.0.1:8000"

def check_r_server():
    response=requests.get(f"{base_URL}/health",timeout=5)
    response.raise_for_status()
    return response.json()

def check_package():
    response=requests.get(f"{base_URL}/status",timeout=5)
    response.raise_for_status()
    return response.json()

def send_test_board(board, player=-1):
    payload = {
        "player": player,
        "board": board
    }

    response = requests.post(
        f"{base_URL}/test-board",
        json=payload,
        timeout=10
    )

    response.raise_for_status()
    return response.json()


def request_move(game):
    from flybrain.encoder import encode_game_state

    payload = encode_game_state(game)

    response = requests.post(
        f"{base_URL}/decide",
        json=payload,
        timeout=10,
    )
    response.raise_for_status()

    result = response.json()
    move_id = result["move_id"]

    if isinstance(move_id, list) and len(move_id) == 1:
        move_id = move_id[0]

    legal_moves = game.get_legal_moves()

    if not isinstance(move_id, int) or not (
        0 <= move_id < len(legal_moves)
    ):
        raise ValueError(f"R returned an invalid move ID: {move_id}")

    return legal_moves[move_id]



if __name__ == "__main__":
    print("Checking R server...")
    print(check_r_server())

    print("\nChecking packages...")
    print(check_package())

    print("\nSending an 8x8 test board...")
    test_board = [[0 for _ in range(8)] for _ in range(8)]

    print(send_test_board(test_board))
