"""
Zadanie 12. Dana jest tablica T[N][N][N]. Prosze napisac funkcje, do której przekazujemy tablice wypełniona
liczbami wiekszymi od zera. Funkcja powinna zwracac wartosc True, jezeli na wszystkich poziomach
tablicy liczba elementów sasiadujacych (w obrebia poziomu) z co najmniej 6 liczbami złozonymi jest jednakowa
albo wartosc False w przeciwnym przypadku.
"""
# A cleaned version of Program1 (without colorized output)

from functools import wraps
from math import sqrt


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
    for level in matrix:
        curr_found_nums = 0
        for row_idx in range(1, len(level)-1):
            for col_idx in range(1, len(level[row_idx])-1):
                # Check a neighbourhood of the number
                rejected_neighbours = 0
                try:
                    for i in range(row_idx-1, row_idx+2):
                        for j in range(col_idx-1, col_idx+2):
                            if (i, j) != (row_idx, col_idx) and not is_compound(level[i][j]):
                                rejected_neighbours += 1
                                # If it is impossible to find 'min_compound_neighbours' that are compound neighbours of
                                # the number, break the loop (number of neighbours required exceeds 8, which is the
                                # maximum total number of neighbours in one level (8 values around the checked one).
                                if rejected_neighbours + min_compound_neighbours > 8:
                                    raise FinishNumberCheck()
                except FinishNumberCheck:
                    continue  # Get to the next element if a loop was broken

                curr_found_nums += 1
                # Finish the function if a number of matching elements exceeded this number from the previous level
                if prev_found_nums is not None and curr_found_nums > prev_found_nums:
                    return False

        if prev_found_nums is None:
            prev_found_nums = curr_found_nums
        elif curr_found_nums != prev_found_nums:
            return False

    return True


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_3D_matrix(n, n, n)
    fill_3D_matrix(t)
    print(search_neighbourhood(t))

'''
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
