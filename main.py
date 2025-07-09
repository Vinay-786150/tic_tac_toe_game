import numpy as np

def create_board():
    return np.zeros((3, 3), dtype=int)

def display_board(board):
    symbols = {0: ' ', 1: 'X', 2: 'O'}
    print("\n   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(symbols[cell] for cell in row))
        if i < 2:
            print("  ---|---|---")

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == 0

def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player} - Enter row (0, 1, 2): "))
            col = int(input(f"Player {player} - Enter col (0, 1, 2): "))
            if is_valid_move(board, row, col):
                board[row][col] = player
                break
            else:
                print("❌ Invalid move! Try again.")
        except ValueError:
            print("❌ Please enter valid integers for row and column.")

def check_winner(board, player):
    return (
        any(all(cell == player for cell in row) for row in board) or
        any(all(board[i][j] == player for i in range(3)) for j in range(3)) or
        all(board[i][i] == player for i in range(3)) or
        all(board[i][2 - i] == player for i in range(3))
    )

def evaluate(board):
    for player in [1, 2]:
        if check_winner(board, player):
            return player
    return -1 if np.all(board != 0) else 0

def play_game():
    board = create_board()
    current_player = 1
    move_count = 0

    print("\n🎮 Welcome to Tic Tac Toe!\n")
    display_board(board)

    while True:
        player_move(board, current_player)
        move_count += 1
        print(f"\nBoard after move {move_count}:")
        display_board(board)

        result = evaluate(board)
        if result == 1 or result == 2:
            print(f"\n🏆 Player {result} wins!")
            break
        elif result == -1:
            print("\n🤝 It's a draw!")
            break

        current_player = 2 if current_player == 1 else 1

def main():
    while True:
        play_game()
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("\n👋 Thanks for playing!")
            break

# Run the project
if __name__ == "__main__":
    main()
