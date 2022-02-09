"""
Zadanie 12. Dana jest tablica T[N][N][N]. Prosze napisac funkcje, do której przekazujemy tablice wypełniona
liczbami wiekszymi od zera. Funkcja powinna zwracac wartosc True, jezeli na wszystkich poziomach
tablicy liczba elementów sasiadujacych (w obrebia poziomu) z co najmniej 6 liczbami złozonymi jest jednakowa
albo wartosc False w przeciwnym przypadku.
"""

from functools import wraps
from math import sqrt
from colorama import Style, Fore
import time
import os


def show_colorized_matrix(matrix, lvl_idx, num_row, num_col, checked_row, checked_col, prev_found_nums, curr_found_nums,
                          rejected_neighbours_indices, *, sleep=.3):
    print_val = lambda color, value: print(f'{getattr(Fore, color.upper())}{value}{Style.RESET_ALL}', end=' ')

    level_matrix = matrix[lvl_idx]

    # Find number of greatest number of digits
    max_val_length = len(str(level_matrix[0][0]))
    for row in level_matrix:
        for val in row:
            val = str(val)
            if len(val) > max_val_length:
                max_val_length = len(val)

    # Print colorized output:
    os.system('cls')

    print(f'===== Current level: {lvl_idx+1}/{len(matrix)} =====')
    print(f'Values counted in the previous level: {prev_found_nums}')
    print(f'Values currently counted: {curr_found_nums}\n')

    for row_idx in range(len(level_matrix)):
        for col_idx in range(len(level_matrix[row_idx])):
            val = str(level_matrix[row_idx][col_idx]).ljust(max_val_length)

            if row_idx == num_row and col_idx == num_col:
                print_val('red', val)            # Currently checked number
            elif row_idx == checked_row and col_idx == checked_col:
                print_val('blue', val)          # Checked neighbour of the currently checked number
            elif (row_idx, col_idx) in rejected_neighbours_indices:
                print_val('LIGHTBLACK_EX', val)  # Rejected number
            elif num_row-1 <= row_idx <= num_row+1 and num_col-1 <= col_idx <= num_col+1:
                print_val('yellow', val)         # All values in the neighbourhood of the currently checked number
            else:
                print(val, end=' ')
        print()

    time.sleep(sleep)


def create_3D_matrix(levels: int, rows: int, columns: int, *, fill_with=0) -> list:
    """Returns a 3-dimensional list representing 3D matrix of specified number of levels
    each of which has 'rows' rows and 'columns' columns. All fields are filled with
    'fill_with' value"""
    matrix = []

    for lvl in range(levels):
        level = []
        for row in range(rows):
            row = []
            for col in range(columns):
                row.append(fill_with)
            level.append(row)
        matrix.append(level)

    return matrix


def fill_3D_matrix(matrix: list):
    """Fills a 3D matrix with values provided by user"""
    for lvl_idx in range(len(matrix)):
        print(f'===== {lvl_idx + 1}. Level =====')
        values_expected = len(matrix[0][0])
        print(f'Expects {values_expected} values for each row.')

        for row_idx in range(len(matrix[lvl_idx])):
            while True:
                values = input(f'{row_idx + 1}. row > ').split()
                if len(values) == len(matrix[lvl_idx][row_idx]):
                    break
                print(f'Wrong number of values provided. Expected {values_expected} values. Try again.')
            for col_idx in range(len(values)):
                matrix[lvl_idx][row_idx][col_idx] = int(values[col_idx])
        print()


def memoized(fn):
    """Caches values returned by the function 'fn' saving them in a dictionary with
    the key of an argument passed to teh funcition for which the value was returned."""
    cache = {}  # A dictionary to save cached values

    @wraps(fn)
    def inner(arg):
        if arg not in cache:
            cache[arg] = fn(arg)
        return cache[arg]

    return inner


@memoized
def is_prime(num: int) -> bool:
    """Checks if the number passed is prime or not."""
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False

    for div in range(3, int(sqrt(num))+1, 2):
        if num % div == 0:
            return False
    return True


def is_compound(num: int) -> bool:
    """Checks if the number passed is a compound number."""
    return not is_prime(num) if num > 1 else False


class FinishNumberCheck(Exception):
    pass


def search_neighbourhood(matrix: 'a 3-dimensional matrix', min_compound_neighbours: int = 6) -> bool:
    """Return True if all levels of the matrix contain the same number of elements that have
    at least 6 compound numbers in their neighbourhood on the same level."""
    if not 1 <= min_compound_neighbours <= 8:
        raise ValueError("Wrong value of 'min_compound_neighbours' variable. Expected an integer in range [1, 8].")

    prev_found_nums = None
    for lvl_idx, level in enumerate(matrix):
        curr_found_nums = 0
        for row_idx in range(1, len(level)-1):
            for col_idx in range(1, len(level[row_idx])-1):
                # Check a neighbourhood of the number
                rejected_neighbours = 0

                rejected_neighbours_indices = set()  # Only for visualisation (remove with show_colorized_matrix)

                try:
                    for i in range(row_idx-1, row_idx+2):
                        for j in range(col_idx-1, col_idx+2):
                            if (i, j) != (row_idx, col_idx) and not is_compound(level[i][j]):
                                rejected_neighbours += 1

                                rejected_neighbours_indices.add((i, j))  # Only for visualisation

                                # If it is impossible to find 'min_compound_neighbours' that are compound neighbours of
                                # the number, break the loop (number of neighbours required exceeds 8, which is the
                                # maximum total number of neighbours in one level (8 values around the checked one).
                                if rejected_neighbours + min_compound_neighbours > 8:
                                    raise FinishNumberCheck()

                            show_colorized_matrix(matrix, lvl_idx, row_idx, col_idx, i, j, prev_found_nums,
                                                  curr_found_nums, rejected_neighbours_indices, sleep=.05)

                except FinishNumberCheck:
                    continue  # Get to the next element if a loop was broken

                curr_found_nums += 1
                # Finish the function if a number of matching elements exceeded this number from the previous level
                if prev_found_nums is not None and curr_found_nums > prev_found_nums:
                    # print(f'Too much in {lvl_idx+1}')
                    return False

        if prev_found_nums is None:
            prev_found_nums = curr_found_nums
        elif curr_found_nums != prev_found_nums:
            # print(f'Not enough in {lvl_idx+1}')
            return False

    return True


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_3D_matrix(n, n, n)
    fill_3D_matrix(t)
    print(search_neighbourhood(t))

'''
5
14 8 16 8 19 
2 9 12 13 1 
9 10 13 9 9 
18 5 12 2 8 
1 14 5 18 17 
1 17 2 16 18 
2 11 14 6 19 
17 18 5 16 2 
18 17 6 1 7 
11 6 2 18 14 
4 16 11 17 8 
4 4 1 14 12 
11 8 7 3 12 
4 12 18 18 3 
4 15 11 19 6 
14 2 15 11 10 
2 10 7 6 19 
7 18 2 15 2 
14 6 3 13 13 
18 7 13 14 4 
15 15 1 10 7 
11 15 15 3 3 
17 17 9 3 2 
2 5 19 11 17 
5 2 10 10 9

7
56 27 78 30 53 37 84 
47 67 52 41 2 47 61 
4 55 70 49 15 14 88 
64 46 22 25 29 66 72 
47 55 1 73 99 69 35 
33 33 12 5 9 17 60 
53 41 78 100 62 78 39 
49 50 37 37 95 56 51 
53 44 73 94 39 37 32 
56 57 77 78 68 100 3 
57 12 36 24 50 9 34 
19 90 64 83 100 82 68 
13 27 22 62 94 83 24 
6 46 44 60 68 24 45 
12 78 72 85 56 9 89 
82 57 49 55 13 39 40 
54 6 21 24 36 6 73 
41 17 83 19 15 45 30 
86 78 29 22 3 9 82 
28 33 58 80 16 21 43 
83 33 28 80 2 63 23 
90 69 8 25 32 27 65 
21 10 59 33 32 29 29 
16 74 37 89 37 33 98 
19 78 36 34 20 65 84 
32 6 87 17 28 54 65 
27 68 32 84 68 4 72 
70 62 37 13 91 68 35 
62 91 46 16 21 18 18 
41 31 60 21 83 62 8 
6 23 98 10 68 30 34 
73 2 58 27 30 72 12 
79 4 12 49 40 1 76 
98 66 26 6 34 11 15 
48 99 40 65 17 23 7 
86 84 81 29 63 32 52 
21 5 8 33 70 90 43 
54 81 54 43 47 51 51 
87 97 61 47 39 62 19 
69 34 5 88 100 12 80 
74 63 78 84 76 68 46 
19 60 22 67 12 73 48 
57 49 55 20 7 33 92 
38 29 44 42 40 22 39 
99 5 98 77 69 4 42 
92 28 55 92 96 9 71 
98 85 98 86 85 49 100 
52 56 50 11 64 47 93 
65 79 65 84 81 80 49

6
8 16 10 3 9 5 
1 42 19 19 3 33 
34 20 8 29 26 3 
26 37 32 6 8 25 
35 34 37 16 16 43 
1 47 22 24 49 19 
12 42 27 11 42 10 
3 3 31 34 2 33 
40 42 34 27 21 20 
35 26 24 23 2 6 
22 45 2 1 38 19 
47 40 34 32 23 15 
20 32 4 36 47 41 
38 2 7 17 11 4 
19 40 44 3 16 13 
18 7 44 40 19 20 
20 12 39 27 6 3 
8 20 45 17 23 14 
9 38 46 45 33 11 
23 41 23 2 11 43 
39 86 40 1 19 27 
41 36 49 40 10 36 
48 48 29 36 30 3 
22 49 26 28 47 17 
43 44 70 5 6 65 
33 16 67 32 43 10 
8 12 10 23 11 37 
35 41 50 46 27 23 
25 9 13 48 17 68 
9 10 43 14 33 25 
17 56 26 10 8 23 
43 38 50 67 9 98 
72 9 56 3 16 9 
47 4 37 23 42 46 
49 10 37 45 38 48 
6 46 10 21 25 38
'''
