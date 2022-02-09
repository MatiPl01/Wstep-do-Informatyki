def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    for i in range(len(matrix)):
        while True:
            row = input().split()
            if len(row) == len(matrix[i]):
                break
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def get_product(matrix, row, col, d):
    return matrix[row+d][col+d] * matrix[row+d][col-d] * matrix[row-d][col+d] * matrix[row-d][col-d]


def search_square(matrix, searched_product):
    size = 3

    while size <= min(len(matrix), len(matrix[0])):
        square_center = size//2
        for centre_row in range(square_center, len(matrix)-square_center):
            for centre_col in range(square_center, len(matrix[0])-square_center):

                if get_product(matrix, centre_row, centre_col, square_center) == searched_product:
                    return centre_row, centre_col
        size += 2

    return None


if __name__ == '__main__':
    k = int(input())
    N = int(input())
    t = create_matrix(N, N)
    fill_matrix(t)
    print(search_square(t, k))


'''
14276737555440
7
12 421 124 124 124 213 2145
1443 412 124 1413 513 141 124
88 532 265 65 346 58 623
252 44 636 457 345 1434 5232
3522 4632 22 25346 4563 2342 435
34134 36436 324 11 25245 6745 4543
4535 43636 23 41 1 6456 567
'''
