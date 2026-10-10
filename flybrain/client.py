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


if __name__ == "__main__":
    print("Checking R server...")
    print(check_r_server())

    print("\nChecking packages...")
    print(check_package())

    print("\nSending an 8x8 test board...")
    test_board = [[0 for _ in range(8)] for _ in range(8)]

    print(send_test_board(test_board))
