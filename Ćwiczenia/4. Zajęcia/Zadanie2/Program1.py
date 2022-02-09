"""
Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
odpowiada na pytanie, czy w kazdym wierszu tablicy wystepuje co najmniej jedna liczba złozona wyłacznie
z nieparzystych cyfr.
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


def all_digits_odd(num: int) -> bool:
    """Checks if all digits of a number are odd"""
    while num > 0:
        num, digit = divmod(num, 10)
        if digit % 2 == 0:
            return False
    return True


def odd_digits_number_in_rows(matrix: list) -> bool:
    """Checks if all rows of a matrix contain at least one integer made up of odd digits"""
    for row in matrix:
        for num in row:
            if all_digits_odd(num):
                break
        else:
            return False
    return True


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(odd_digits_number_in_rows(t))


'''
1 2 3 4
32 22 21 11
90 123 45 17
23 67 1245 33

498 243 12341 431
32 22 21 11
90 123 45 17
23 67 1245 33
'''
