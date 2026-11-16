
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1, n):
                return True

            board[row] = -1

    return False


def print_board(board, n):
    print("\nChessboard:")
    for i in range(n):
        for j in range(n):
            print("Q" if board[i] == j else ".", end=" ")
        print()


# Main program
n = int(input("Enter number of queens: "))

if n <= 0:
    print("Enter a positive number.")
elif n == 2 or n == 3:
    print("No solution exists.")
else:
    board = [-1] * n

    if solve(board, 0, n):
        print("\nSolution Found!")
        print("Queen Positions:")

        for i in range(n):
            print("Queen", i+1, ":", (i+1, board[i]+1))

        print_board(board, n)
    else:
        print("No solution exists.")
