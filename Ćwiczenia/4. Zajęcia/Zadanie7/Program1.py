"""
Zadanie 7. Dane sa dwie tablice mogace pomiescic taka sama liczbe elementów: T1[N][N] i T2[M], gdzie
M=N*N. W kazdym wierszu tablicy T1 znajduja sie uporzadkowane niemalejaco (w obrebie wiersza) liczby
naturalne. Prosze napisac funkcje przepisujaca wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
T2 były uporzadkowane niemalejaco.
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


def get_sorted_values(source_matrix: list) -> list:
    """Returns sorted values of a matrix"""
    return sorted(val for row in source_matrix for val in row)


if __name__ == '__main__':
    n = int(input('(n) > '))
    t1 = create_matrix(n, n)
    fill_matrix(t1)
    t2 = get_sorted_values(t1)
    print(t1)
    print(t2)

'''
6
12 431 515 634 744 2535
16 34 65 634 1234 9064
1 2 3 4 5 6
231 543 765 765 943 1234
6 98 712 819 6542 12334
345 654 3421 7523 9783 43212
'''
