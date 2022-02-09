"""
Zadanie 13. Liczby naturalne a,b sa komplementarne jezeli ich suma jest liczba pierwsza. Dana jest tablica
T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która zeruje elementy nie posiadajace
liczby komplementarnej.
"""

# FIX THIS CODE (NOT ALL VALUES ARE CHECKED AS THEY SHOULD)

from functools import wraps
from math import sqrt


def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    """Creates a 2-dimensional list of a specified number of rows and columns"""
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    """Fills matrix with values provided by the user"""
    for i in range(len(matrix)):
        while True:
            row = input(f'{i + 1}. row > ').split()
            if len(row) == len(matrix[i]):
                break
            print('Wrong number of values specified. Please try again.')
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def memoized(fn):
    """Caches values returned by the function 'fn'. Not that function must be
    one-parameter only."""
    cache = {}  # Cached values will be stored here

    @wraps(fn)
    def inner(arg):
        if arg not in cache:
            cache[arg] = fn(arg)
        return cache[arg]

    return inner


@memoized
def is_prime(num: int) -> bool:
    """Checks if the number passed is prime or not"""
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for div in range(3, int(sqrt(num))+1):
        if num % div == 0:
            return False
    return True


def fill_non_complementary_numbers_with_zeros(matrix: list):
    """Replaces values of numbers that cannot create complementary pair with any of the
    remaining numbers in the 'matrix' list. A complementary numbers pair is a pair of values
    that sum up to the prime number."""
    have_comp_num = set()

    # Look for complementary numbers
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            curr_num = matrix[row_idx][col_idx]

            # Look for a number to create the complementary pair
            col_idx += 1  # Doesn't work properly !!!!!!
            for i in range(row_idx, len(matrix)):
                for j in range(col_idx, len(matrix[i])):
                    if is_prime(curr_num + matrix[i][j]):
                        have_comp_num.add(curr_num)
                        have_comp_num.add(matrix[i][j])
                col_idx = 0

    # Replace values of non-complementary numbers with zeros
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            if matrix[row_idx][col_idx] not in have_comp_num:
                matrix[row_idx][col_idx] = 0


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    fill_non_complementary_numbers_with_zeros(t)
    print(t)

"""
3
15 73 47 
85 100 69 
19 41 34

5
8806 24005 72870 81447 81272 
9215 36478 66412 501 92533 
99818 26635 93357 93627 10312 
11022 72058 43617 22345 86849 
97206 15578 96669 65253 12205

10
79359 67482 85024 13989 20288 12663 51269 81717 29775 62691 
64964 55042 62622 77139 98944 66648 72862 74671 31186 44752 
1454 19785 88973 74752 4573 8 22636 68658 21929 48241 
8888 86389 89971 806 59876 63522 67571 76336 30626 56481 
56416 49768 60024 74421 57116 67060 64383 87230 50239 97655 
50633 86911 84324 37224 83460 78321 7172 99879 88638 88999 
22745 87076 80617 35652 44571 50170 59209 51821 30394 19989 
95546 93182 11889 4565 77487 95519 47682 69817 57679 84502 
27629 97454 90252 55478 25838 56036 62811 84407 44781 33024 
48556 39418 81895 39161 12149 28242 26191 28200 16943 72858
"""
