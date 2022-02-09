from colorama import Fore, Style
from random import randint
import time
import os


def show_matrix(matrix: list, placed_coords: (int, int), *, sleep=.1):
    print_val = lambda val, color: print(f'{getattr(Fore, color.upper())}{value}{Style.RESET_ALL}', end=' ')
    os.system('cls')
    print()
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            value = matrix[row_idx][col_idx]
            if value:
                if (row_idx, col_idx) in placed_coords:
                    print_val(value, 'blue')
                else:
                    print_val(value, 'red')
            else:
                print(value, end=' ')
        print()
    time.sleep(sleep)


def generate_random_coordinates(count: int, max_row: int, max_col: int) -> list:
    return [(randint(0, max_row), randint(0, max_col)) for _ in range(count)]


def queens_not_checkmate(matrix: list, coordinates: [(int, int)]) -> bool:
    for idx, (row_idx, col_idx) in enumerate(coordinates):
        if matrix[row_idx][col_idx]:  # That means one of queens checkmate a current field
            return False
        place_queen(matrix, (row_idx, col_idx))
        show_matrix(board, coordinates[:idx+1])
    return True


def place_queen(matrix: list, coordinates: (int, int)):
    row_idx, col_idx = coordinates

    # Cross out the column
    for i in range(len(matrix)):
        matrix[i][col_idx] = 1

    # Cross out the row
    for i in range(len(matrix[0])):
        matrix[row_idx][i] = 1

    # Cross out the diagonal line from top-left corner to the bottom-right corner
    start_row_idx = max(0, row_idx-col_idx)
    start_col_idx = max(0, col_idx-row_idx)
    for i in range(len(matrix)-start_row_idx-start_col_idx):
        matrix[start_row_idx+i][start_col_idx+i] = 1

    # Cross out the diagonal line from bottom-left corner to the top-right corner
    start_row_idx = min(row_idx+col_idx, len(matrix)-1)
    start_col_idx = max(0, col_idx-(len(matrix)-1 - row_idx))
    for i in range(start_row_idx-start_col_idx+1):
        matrix[start_row_idx-i][start_col_idx+i] = 1


if __name__ == '__main__':
    board_size = 100
    board = [[0]*board_size for _ in range(board_size)]

    coordinates = generate_random_coordinates(15, board_size-1, board_size-1)
    print(queens_not_checkmate(board, coordinates))
