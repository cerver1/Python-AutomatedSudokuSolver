sudoku_board = \
    [[0, 0, 9, 0, 0, 2, 0, 0, 5],
     [5, 3, 8, 0, 6, 4, 0, 0, 9],
     [1, 6, 2, 0, 0, 0, 0, 3, 0],
     [0, 0, 3, 0, 2, 7, 0, 0, 0],
     [0, 5, 4, 6, 0, 0, 1, 0, 0],
     [0, 0, 7, 0, 1, 5, 3, 4, 0],
     [3, 0, 0, 8, 0, 1, 9, 0, 6],
     [7, 0, 0, 3, 0, 0, 8, 5, 0],
     [0, 9, 1, 0, 0, 0, 4, 7, 0]]

sudoku_board2 = \
    [[0, 0, 9, 0, 0, 2, 0, 0, 5],
     [5, 3, 8, 0, 6, 4, 0, 0, 9],
     [1, 6, 2, 0, 0, 0, 0, 3, 0]]


def find_empty_locations(board):
    for i in board:
        for j in i:
            if j == 0:
                return board.index(i), i.index(j)
    return


def attempt_entry(board):
    position = find_empty_locations(board)
    if position == "":
        return True
    else:
        for i in range(1, 9):
            if validate_position(board, i, position):
                board[position[0]][position[1]] = i

                if attempt_entry(board):
                    return True

                board[position[0]][position[1]] = 0
    for i in board:
        print(i)
    return False


def validate_position(board, number, position):
    if number in board[position[0]]:
        return False

    for i in board:
        if i[position[1]] == number:
            return False

    x_cord = position[1] / 3
    y_cord = position[0] / 3

    for i in range(y_cord * 3, (y_cord * 3) + 3):
        for j in range(x_cord * 3, (x_cord * 3) + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


attempt_entry(sudoku_board)
