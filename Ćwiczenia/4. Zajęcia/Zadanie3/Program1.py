"""
Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
odpowiada na pytanie, czy istnieje wiersz w tablicy w którym kazda z liczb zawiera przynajmniej jedna cyfre
parzysta.
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


def has_even_digit(num: int) -> bool:
    """Checks if at least one digit of a number is even"""
    while num > 0:
        num, digit = divmod(num, 10)
        if digit % 2 == 0:
            return True
    return False


def all_nums_in_one_row_have_even_digit(matrix: list) -> bool:
    """Checks if all numbers in at least one of the matrix's rows have at least
    one even digit"""
    for row in matrix:
        for num in row:
            if not has_even_digit(num):
                break
        else:
            return True
    return False


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(all_nums_in_one_row_have_even_digit(t))


'''
5
123 32 565 33 67
123 214 1 141 34
4134 13 134 17 215
264 75 252 522 324
52351 431 5412 151 31

5
123 32 565 33 67
123 214 1 141 34
4134 13 134 17 215
264 75 252 522 324
52351 431 5412 1561 310
'''
