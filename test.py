# this file is for testing new functions before integrating them into the main file
# so kind of a workspace before the project main result

def print_board(cell):
    print('-' * 15)
    print('|', cell[0], cell[1], cell[2], '|')
    print('|', cell[3], cell[4], cell[5], '|')
    print('|', cell[6], cell[7], cell[8], '|')
    print('-' * 15)


def row_check(board):
    for row in board:
        if row[0] != '_' and row.count(row[0]) == len(row):
            return row[0]
    return False


def col_check(board):
    row_list = []
    for i in range(3):
        row_list.append([])
        for k in range(3):
            row_list[i].append(board[k][i])

    return row_check(row_list)


def diagonal_check(board):
    flat = [col for row in board for col in row]
    left = [flat[i] for i in range(0, 9, 4)]
    middle = [flat[i] for i in range(1, 8, 3)]
    right = [flat[i] for i in range(2, 7, 2)]

    new_list = [left, middle, right]
    return row_check(new_list)


def empty_cells(board):
    return any([col == '_' for row in board for col in row])


def draw_check(board):
    return not empty_cells(board) and not row_check(board) and not col_check(board) and not diagonal_check(board)


def finish_check(board):
    return empty_cells(board) and not row_check(board) and not col_check(board) \
           and not diagonal_check(board) and not impossible_check(board)


def both_win(board):
    if row_check(board) == 'X' or col_check(board) == 'X':
        # Algorithm to check if both players won. 1- make a new list by changing the sign
        # of the already won player. 2- Exclusively check the other one
        new_list = []
        for i in range(3):
            new_list.append([])
            for k in range(3):
                if board[i][k] == 'X':
                    new_list[i].append('_')
                else:
                    new_list[i].append(board[i][k])

        if row_check(new_list) == 'O' or col_check(new_list) == 'O':
            return True

    if row_check(board) == 'O' or col_check(board) == 'O':
        new_list = []
        for i in range(3):
            new_list.append([])
            for k in range(3):
                if board[i][k] == 'O':
                    new_list[i].append('_')
                else:
                    new_list[i].append(board[i][k])

        if row_check(new_list) == 'X' or col_check(new_list) == 'X':
            return True

    return False


def impossible_check(board):
    x_count = [col for row in board for col in row].count('X')
    o_count = [col for row in board for col in row].count('O')

    difference = max(x_count, o_count) - min(x_count, o_count) >= 2
    return difference or both_win(board)


def empty_coordinates(board):
    coordinates = []
    row = len(board)
    col = len(board[0])

    for i in range(row):
        for k in range(col):
            if board[i][k] == '_':
                coordinates.append((i + 1, k + 1))

    return coordinates


def move_player(board, coordinates):
    coordinates = [item - 1 for item in coordinates]
    board[coordinates[0]][coordinates[1]] = 'X'
    return board


def take_coordinates(board):
    while True:
        try:
            row, col = input('Enter the coordinates: ').split()
            try:
                row, col = int(row), int(col)
                if (1 <= row <= 3) and (1 <= col <= 3):
                    coordinates = (row, col)
                    if coordinates in empty_coordinates(board):
                        return move_player(board, coordinates)
                    else:
                        print('This cell is occupied! Choose another one!')
                else:
                    print('Coordinates should be from 1 to 3!')
            except ValueError:
                print('You should enter numbers!')
        except ValueError:
            print('You should enter numbers!')


def check_state(board):
    if (not impossible_check(board)) and (row_check(board) == 'X' or col_check(board) == 'X'
                                          or diagonal_check(board) == 'X'):
        print('X wins')
    elif (not impossible_check(board)) and (row_check(board) == 'O' or col_check(board) == 'O'
                                            or diagonal_check(board) == 'O'):
        print('O wins')
    elif draw_check(board):
        print('Draw')
    elif finish_check(board):
        print('Game not finished')
    elif impossible_check(board):
        print('Impossible')


# while True:
#     cells = input('Enter cells: ')
#     if cells == 'exit':
#         break
#     else:
#         grid = [[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]
#
#         print_board(cells)
#         check_state(grid)
#         print()

def screen():
    cells = input('Enter cells: ')
    grid = [[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]
    print_board(cells)
    new_grid = take_coordinates(grid)
    new_cells = [col for row in new_grid for col in row]
    print_board(''.join(new_cells))


screen()
