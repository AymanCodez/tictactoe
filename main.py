def print_board(cell):
    print('-' * 15)
    print('|', cell[0], cell[1], cell[2], '|')
    print('|', cell[3], cell[4], cell[5], '|')
    print('|', cell[6], cell[7], cell[8], '|')
    print('-' * 15)


def row_check(board):
    for row in board:
        if row[0] != ' ' and row.count(row[0]) == len(row):
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
    return any([col == ' ' for row in board for col in row])


def draw_check(board):
    return not empty_cells(board) and not row_check(board) and not col_check(board) and not diagonal_check(board)


def empty_coordinates(board):
    coordinates = []
    row = len(board)
    col = len(board[0])

    for i in range(row):
        for k in range(col):
            if board[i][k] == ' ':
                coordinates.append((i + 1, k + 1))

    return coordinates


def move_player(board, coordinates, player_sign):
    coordinates = [item - 1 for item in coordinates]
    board[coordinates[0]][coordinates[1]] = player_sign
    return board, player


def change_player():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


def manage_coordinates(board):
    while True:
        try:
            row, col = input('Enter the coordinates: ').split()
            try:
                row, col = int(row), int(col)
                if (1 <= row <= 3) and (1 <= col <= 3):
                    coordinates = (row, col)
                    if coordinates in empty_coordinates(board):
                        return coordinates
                    else:
                        print('This cell is occupied! Choose another one!')
                else:
                    print('Coordinates should be from 1 to 3!')
            except ValueError:
                print('You should enter numbers!')
        except ValueError:
            print('You should enter numbers!')


def check_state(starting_grid):
    while True:
        position = manage_coordinates(starting_grid)
        new_grid, new_player = move_player(starting_grid, position, player)
        change_player()
        new_cells = [col for row in new_grid for col in row]
        print_board(''.join(new_cells))
        if row_check(new_grid) == 'X' or col_check(new_grid) == 'X' or diagonal_check(new_grid) == 'X':
            print('X wins')
            break
        elif row_check(new_grid) == 'O' or col_check(new_grid) == 'O' or diagonal_check(new_grid) == 'O':
            print('O wins')
            break
        elif draw_check(new_grid):
            print('Draw')
            break


cells = '         '
grid = [[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]
print_board(cells)
player = 'X'
check_state(grid)
