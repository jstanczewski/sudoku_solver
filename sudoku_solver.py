sudoku_board = [
    [0, 0, 0, 7, 0, 6, 0, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 4, 0, 9, 7, 0, 2],
    [6, 0, 1, 0, 0, 4, 0, 8, 0],
    [0, 9, 0, 0, 2, 0, 0, 4, 0],
    [0, 4, 0, 5, 0, 0, 6, 0, 9],
    [1, 0, 4, 8, 0, 5, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 9, 0, 7, 0, 0, 0],
]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True

            board[row][column] = 0

    return False


def valid(board, number, position):
    # check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check box
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None


print_board(sudoku_board)
solve(sudoku_board)
print("\n_______________________\n")
print_board(sudoku_board)
