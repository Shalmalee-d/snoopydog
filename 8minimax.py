
import math

board = [" "] * 9
X, O = "X", "O"

def print_board():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")

def winner():
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"
    return None

def minimax(is_max):
    result = winner()

    if result == X: return 1
    if result == O: return -1
    if result == "Draw": return 0

    best = -math.inf if is_max else math.inf
    player = X if is_max else O

    for i in range(9):
        if board[i] == " ":
            board[i] = player
            score = minimax(not is_max)
            board[i] = " "

            if is_max:
                best = max(best, score)
            else:
                best = min(best, score)

    return best

def best_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = X
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

def main():
    print("TIC-TAC-TOE USING MINIMAX")
    print("Computer = X | Human = O")
    print("Positions: 1 2 3 / 4 5 6 / 7 8 9")

    while True:
        move = best_move()
        board[move] = X
        print("\nComputer's move:")
        print_board()

        if winner():
            break

        while True:
            try:
                pos = int(input("Enter position (1-9): ")) - 1
                if 0 <= pos < 9 and board[pos] == " ":
                    board[pos] = O
                    break
                print("Invalid or occupied position!")
            except ValueError:
                print("Enter a valid number!")

        print("\nYour move:")
        print_board()

        if winner():
            break

    result = winner()
    if result == X:
        print("Computer wins!")
    elif result == O:
        print("You win!")
    else:
        print("It's a draw!")

main()
