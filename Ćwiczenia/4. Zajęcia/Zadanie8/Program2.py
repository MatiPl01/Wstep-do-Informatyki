"""
Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która w
poszukuje w tablicy najdłuzszego ciagu geometrycznego lezacego ukosnie w kierunku prawo-dół, liczacego
co najmniej 3 elementy. Do funkcji nalezy przekazac tablice. Funkcja powinna zwrócic informacje czy udało
sie znalezc taki ciag oraz długosc tego ciagu.
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


def longest_diagonal_geometric_subsequence(matrix: list) -> int:
    """Returns length of the longest geometric sequence found in the matrix (0 if not found; 2-element
    sequences aren't counted). Sequence is searched diagonally from the top-left corner to the bottom-right corner."""
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
    n = int(input('(n) > '))
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

8
1 424 345 33636 234 2 534 355
41241 4 324 265345 1 214 314 324
14341 452 16 2342 3663 4747 4354 654
141341 34 521 64 897987 3249 342 7643
145 84593 298789 238759 256 89419 4234 6543
5262 253252 533 4646 252 1024 97789 9942
872569 9853479 124 78543 90239 673 294 324
98593 3478 1 681 9823 4289 18732 28792
'''
