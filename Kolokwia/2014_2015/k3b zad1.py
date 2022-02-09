def create_matrix(rows: int, columns: int, *, fill_with=0):
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


def longest_diagonal_geometric_subsequence(matrix: list):
    max_length = 2

    def search_sequence(row_idx, col_idx):
        curr_max_length = curr_length = 2

        for _ in range(min(len(matrix)-row_idx-2, len(matrix)-col_idx-2)):
            if matrix[row_idx][col_idx] ** 2 == matrix[row_idx-1][col_idx-1] * matrix[row_idx+1][col_idx+1]:
                curr_length += 1
                if curr_length > curr_max_length:
                    curr_max_length = curr_length
            else:
                curr_length = 2
            row_idx += 1
            col_idx += 1

        return curr_max_length

    for start_idx in range(1, len(matrix)-1):
        curr_length = max(search_sequence(1, start_idx), search_sequence(start_idx, 1))
        if curr_length > max_length:
            max_length = curr_length

    return max_length if max_length > 2 else 0


if __name__ == '__main__':
    n = int(input())
    t = create_matrix(n, n)
    fill_matrix(t)
    longest_seq = longest_diagonal_geometric_subsequence(t)
    if longest_seq > 0:
        print(f'Found matching sequence of length: {longest_seq}')
    else:
        print('Couldn\'t have found appropriate subsequence')

'''
7
12 421 124 124 124 213 2145
1443 412 124 1413 513 141 124
88 532 265 65 346 58 623
252 44 636 457 345 1434 5232
3522 4632 22 25346 4563 2342 435
34134 36436 324 11 25245 6745 4543
4535 43636 23 41 1 6456 567
'''
