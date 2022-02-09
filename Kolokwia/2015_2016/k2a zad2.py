"""
UWAGA !!!!
"""
# POLE NA KTÓRYM STOI WIEŻA JEST SZACHOWANE !!!!

import random


def random_matrix(rows: int, cols: int, min_num: int, max_num: int) -> [[int]]:
    return [[random.randint(min_num, max_num) for _ in range(cols)] for _ in range(rows)]


def place_towers_init(matrix: list):
    row_sums = {}  # Store calculated sums to improve performance
    col_sums = {}

    taken_fields = set()  # Store information about already taken fields
    taken_rows = set()
    taken_cols = set()

    # A helper function to calculate sums
    def row_col_sum(row_idx, col_idx):
        # Get sum of values in a row
        if row_idx in taken_rows:  # Set row_sum to 0 if the row is already taken
            row_sum = 0
        else:
            if row_idx in row_sums:  # Return cached sum of a row if exists
                row_sum = row_sums[row_idx]
            else:
                row_sum = 0
                for i in range(len(matrix[row_idx])):
                    row_sum += matrix[row_idx][i]
                row_sums[row_idx] = row_sum          # Store calculated sum of all elements in a row

        # Get sum of values in a column
        if col_idx in taken_cols:  # Set col_sum to 0 if the row is already taken
            col_sum = 0
        else:
            if col_idx in col_sums:  # Return cached sum of a column if exists
                col_sum = col_sums[col_idx]
            else:
                col_sum = 0
                for i in range(len(matrix)):
                    col_sum += matrix[i][col_idx]
                col_sums[col_idx] = col_sum          # Store calculated sum of all elements in a column

        return row_sum + col_sum

    # Another helper function that subtracts proper values from sums of rows and columns
    def update_row_col_sums(row_idx, col_idx):
        # Subtract a value from taken column by new tower from sums of values in rows
        for i in range(len(matrix)):
            row_sums[i] -= matrix[i][col_idx]
        # Subtract a value from taken row by new tower from sums of values in columns
        for i in range(len(matrix[row_idx])):
            col_sums[i] -= matrix[row_idx][i]

    def place_tower() -> tuple:
        max_sum = 0
        max_sum_row_idx = None
        max_sum_col_idx = None
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[row_idx])):
                if (row_idx, col_idx) in taken_fields:
                    continue
                curr_sum = row_col_sum(row_idx, col_idx)
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_sum_row_idx = row_idx
                    max_sum_col_idx = col_idx

        coordinates = (max_sum_row_idx, max_sum_col_idx)
        if max_sum_row_idx is not None and max_sum_col_idx is not None:
            taken_rows.add(max_sum_row_idx)
            taken_cols.add(max_sum_col_idx)
            taken_fields.add(coordinates)
            update_row_col_sums(max_sum_row_idx, max_sum_col_idx)

        return coordinates

    return place_tower


def place_towers(matrix: list, count: int):
    place_tower = place_towers_init(matrix)
    return [place_tower() for _ in range(count)]


if __name__ == '__main__':
    N = 4
    min_num, max_num = -9, 9
    count = 2

    random.seed(0)
    t = random_matrix(N, N, min_num, max_num)
    print(*t, sep='\n')
    print(place_towers(t, count))
