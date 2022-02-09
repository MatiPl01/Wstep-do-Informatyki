"""
Zadanie 6. Dane sa dwie tablice mogace pomiescic taka sama liczbe elementów: T1[N][N] i T2[M], gdzie
M=N*N. W kazdym wierszu tablicy T1 znajduja sie uporzadkowane rosnaco (w obrebie wiersza) liczby
naturalne. Prosze napisac funkcje przepisujaca wszystkie singletony (liczby wystepujace dokładnie raz) z
tablicy T1 do T2, tak aby liczby w tablicy T2 były uporzadkowane rosnaco. Pozostałe elementy tablicy T2
powinny zawierac zera.
"""

def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    """Creates a 2-dimensional list of specified number of rows and columns"""
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


def rewrite_singletons(source_matrix: [[int]], target_list: list):
    """Rewrites singleton values from 'source_matrix' to 'target_matrix' in an increasing order.
    Note that all rows in 2-dimensional 'source_matrix' list must be sorted in an increasing
    order as well."""
    # A helper function
    def save_next_value(val):
        nonlocal target_list_idx
        target_list[target_list_idx] = val
        target_list_idx += 1

    # Store information about values that appear more than once in the 'source_matrix'
    sorted_vals = sorted(val for row in source_matrix for val in row)
    target_list_idx = 0

    # Extract singletons from all values
    # Check first value
    if sorted_vals[0] != sorted_vals[1]:
        save_next_value(sorted_vals[0])

    # Check others in a loop
    for i in range(1, len(sorted_vals)-1):
        if sorted_vals[i-1] != sorted_vals[i] != sorted_vals[i+1]:
            save_next_value(sorted_vals[i])

    # Check last value
    if sorted_vals[-1] != sorted_vals[-2]:
        save_next_value(sorted_vals[-1])


if __name__ == '__main__':
    n = int(input('(n) > '))
    t1 = create_matrix(n, n)
    fill_matrix(t1)
    t2 = [None] * n*n
    rewrite_singletons(t1, t2)
    print(t1, t2, sep='\n')


'''
6
1 431 515 634 744 2535
16 34 65 634 1234 9064
1 2 3 4 5 6
231 543 765 765 943 1234
6 98 712 819 6542 12334
1 654 3421 7523 9783 43212

10
2 22 40 68 77 77 86 92 94 100
47 48 49 52 67 68 79 85 90 100
2 23 24 28 52 90 91 95 100 100
2 5 14 28 47 48 50 56 70 71
1 7 9 18 21 32 33 62 63 90
34 52 56 57 68 80 85 86 96 100
2 8 17 38 39 39 43 43 66 89
13 21 26 49 53 59 90 93 96 99
2 6 13 15 34 64 70 72 72 91
32 40 50 63 69 70 75 75 79 91
'''