def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    for i in range(len(matrix)):
        while True:
            row = input().split()
            if len(row) == len(matrix[i]):
                break
            print(f"Expected {len(matrix[i])} values, got {len(row)}.")
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def rewrite_values(source_matrix: list, target_matrix: list) -> list:
    for i, val in enumerate(sorted(val for row in source_matrix for val in row)):
        target_matrix[i] = val


if __name__ == '__main__':
    N = int(input())
    t1 = create_matrix(N, N)
    t2 = create_matrix(1, N*N)[0]
    fill_matrix(t1)
    print(t2)
    rewrite_values(t1, t2)
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
