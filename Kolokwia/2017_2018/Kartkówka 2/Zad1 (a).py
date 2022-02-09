"""Zadanie 2.1a (2017/2018)
Dana jest tablica t[N][N] reprezentująca szachownicę, wypełniona liczbami naturalnymi. na
szachownicy znajdują się dwie wieże. Proszę napisać funkcję, która odpowiada na pytanie: czy
istnieje ruch wieży zwiększający sumę liczb na “szachowanych” przez wieże polach? Do funkcji
należy przekazać tablicę oraz położenia dwóch wież, funkcja powinna zwrócić wartość logiczną.
Uwagi: zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola, na którym stoi.
N to globalny const int.
"""

import random


def random_matrix(rows, cols, min_num, max_num):
    return [[random.randint(min_num, max_num) for _ in range(cols)] for _ in range(rows)]


def get_row_sum(matrix, row_idx):
    sum_ = 0
    for col_idx in range(len(matrix[row_idx])):
        sum_ += matrix[row_idx][col_idx]
    return sum_


def get_col_sum(matrix, col_idx):
    sum_ = 0
    for row_idx in range(len(matrix)):
        sum_ += matrix[row_idx][col_idx]
    return sum_


def get_possible_moves(n, y1, x1, y2, x2):
    if x1 != x2:
        return range(n)
    if y1 < y2:
        return range(y2)
    else:
        return range(y2+1, n)


def func(matrix, coords1, coords2):
    r1, c1 = coords1
    r2, c2 = coords2
    rows_sums = [get_row_sum(matrix, i) for i in range(len(matrix))]
    cols_sums = [get_col_sum(matrix, i) for i in range(len(matrix[0]))]

    def row_col_sum(r1, c1, r2, c2):
        sum_ = rows_sums[r1] + rows_sums[r2] + cols_sums[c1] + cols_sums[c2] - (matrix[r1][c1] + matrix[r2][c2])
        if r1 == r2:
            return sum_ - rows_sums[r1]
        if c1 == c2:
            return sum_ - cols_sums[c1]

        return sum_ - (matrix[r1][c2] + matrix[r2][c1])  # Subtract points of intersection of fields that are in check

    initial_sum = row_col_sum(r1, c1, r2, c2)

    # Move the first tower
    # Move this tower vertically
    for row1 in get_possible_moves(len(matrix), r1, c1, r2, c2):
        if row_col_sum(row1, c1, r2, c2) > initial_sum:
            return True

    # Move this tower horizontally
    for col1 in get_possible_moves(len(matrix[0]), c1, r1, c2, r2):
        if row_col_sum(r1, col1, r2, c2) > initial_sum:
            return True

    # Move the second tower
    # Move this tower vertically
    for row2 in get_possible_moves(len(matrix), r2, c2, r1, c1):
        if row_col_sum(row2, c2, r1, c1) > initial_sum:
            return True

    # Move this tower horizontally
    for col2 in get_possible_moves(len(matrix[0]), c2, r2, c1, r1):
        if row_col_sum(r2, col2, r1, c1) > initial_sum:
            return True

    return False


if __name__ == '__main__':
    N = 5
    min_num, max_num = 0, 10
    tower1_coords, tower2_coords = (0, 0), (1, 1)

    T = random_matrix(N, N, min_num, max_num)
    # T.pop()
    # T.pop()
    # T.pop()
    print(*T, sep='\n')

    print(func(T, tower1_coords, tower2_coords))
