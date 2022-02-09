from math import sqrt


def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    for i in range(len(matrix)):
        while True:
            row = input(f'{i + 1}. row > ').split()
            if len(row) == len(matrix[i]):
                break
            print('Wrong number of values specified. Please try again.')
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for div in range(3, int(sqrt(num))+1):
        if num % div == 0:
            return False
    return True


def check_pos(matrix: list) -> bool:
    for row_idx in range(len(matrix)-1):
        for col_idx in range(len(matrix[row_idx])-2):
            if is_prime(matrix[row_idx][col_idx] + matrix[row_idx+1][col_idx+2]):
                return True
    for row_idx in range(len(matrix)-2):
        for col_idx in range(len(matrix[row_idx])-1):
            if is_prime(matrix[row_idx][col_idx] + matrix[row_idx+2][col_idx+1]):
                return True
    for row_idx in range(len(matrix)-1):
        for col_idx in range(len(matrix[row_idx])-2):
            if is_prime(matrix[row_idx][col_idx] + matrix[row_idx+2][col_idx-1]):
                return True
    for row_idx in range(len(matrix)-1):
        for col_idx in range(len(matrix[row_idx])-2):
            if is_prime(matrix[row_idx][col_idx] + matrix[row_idx+1][col_idx-2]):
                return True
    return False


if __name__ == '__main__':
    N = int(input('(N) > '))
    t = create_matrix(N, N)
    fill_matrix(t)
    print(check_pos(t))

'''
4
14901 45942 22758 98447
78494 30646 10647 35258
70276 63475 12257 51118
11310 28257 89447 90665
'''
