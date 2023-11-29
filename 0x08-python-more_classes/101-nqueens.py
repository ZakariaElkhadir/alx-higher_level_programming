def solve(board, N):
    # base case: if all queens are placed
    if board[N - 1] != -1:
        return True

    # consider this cell for the current queen
    for i in range(N):
        if is_safe(board, N, i):
            # place this queen in the current cell
            board[N - 1] = i

            # recursively check if we can place the rest of the queens
            if solve(board, N + 1):
                return True

            # if the solution placing this queen doesn't lead to a solution, remove it
            board[N - 1] = -1

    return False

def is_safe(board, N, col):
    # check if there is a queen in the same column
    for i in range(N):
        if board[i] == col:
            return False

    return True

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = int(sys.argv[1])

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N

    if not solve(board, 0):
        print("Solution does not exist")
        sys.exit(1)

    print_solution(board, N)

if __name__ == "__main__":
    main()
