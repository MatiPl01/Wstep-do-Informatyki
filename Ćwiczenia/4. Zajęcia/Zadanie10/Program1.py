"""
Zadanie 10. Napisac funkcje która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartosc
True w przypadku, gdy w kazdym wierszu i kazdej kolumnie wystepuje co najmniej jedno 0 oraz wartosc
False w przeciwnym przypadku.
"""

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


def value_in_every_row_and_column(matrix: list, target_value: 'value that is being searched') -> bool:
    """Checks if 'target_value' exists in every row and every column of the 'matrix' 2-dimensional list.
    Return True if searched value was found in every row and column else returns False."""
    found_columns_indices = set()  # Store indices of columns in which 'target_value' was found

    for row_idx in range(len(matrix)):
        found_in_row = False
        for col_idx in range(len(matrix[row_idx])):
            if matrix[row_idx][col_idx] == target_value:
                found_columns_indices.add(col_idx)
                found_in_row = True
        if not found_in_row:
            return False

    # If number of columns where 'target_value' was found matches the number of columns in the 'matrix', return True
    return len(found_columns_indices) == len(matrix[0])


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print('\n', value_in_every_row_and_column(t, 0))

'''
12
0 -19 87 0 66 -36 55 -8 74 0 -99 34 
-22 -79 51 78 88 39 10 0 -33 -49 11 26 
52 97 38 37 52 93 -92 -91 16 40 -76 -61 
-32 25 -28 -7 -19 -11 0 -5 95 0 81 0 
11 27 89 70 0 0 -54 56 -21 -20 -7 -30 
-81 0 -54 -11 0 40 -88 -26 -12 79 25 0 
98 -56 91 -69 0 -32 73 0 -84 11 -66 70 
9 -49 -97 -62 -79 38 42 -87 81 75 0 -75 
48 70 40 90 5 77 -38 -79 -6 -31 -40 54 
0 -65 31 96 0 75 -68 -53 23 28 -4 10 
-28 -55 -53 -97 -16 7 -87 0 0 55 -73 -12 
48 62 -48 42 75 -42 90 -70 61 -59 -51 14

10
32 0 -27 -7 -32 -81 94 4 65 -65 
-62 48 0 0 -13 -36 -14 0 -35 -77 
-24 62 -22 0 45 -42 89 35 0 0 
0 -55 0 0 0 -31 93 76 68 -62 
51 -87 61 0 37 0 0 15 0 78 
0 9 0 86 -18 56 0 -69 8 -32 
-48 65 -48 39 -85 2 0 42 -12 -77 
24 95 33 0 92 -33 0 -64 -96 -44 
-8 -37 -50 23 -60 -22 23 93 0 -71 
-30 -44 -22 77 0 92 48 15 -25 81
'''
