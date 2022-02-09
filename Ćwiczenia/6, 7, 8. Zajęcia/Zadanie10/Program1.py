# Rozwinięcie Laplace’a

def cross_off_row_col(matrix, row_idx, col_idx):
    new_matrix = []
    for i in range(len(matrix)):
        if i != row_idx:
            row = []
            for j in range(len(matrix[i])):
                if j != col_idx:
                    row.append(matrix[i][j])
            new_matrix.append(row)
    return new_matrix


def determinant_recur(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    result = 0
    for i in range(len(matrix)):
        if matrix[i][0] != 0:
            crossed_matrix = cross_off_row_col(matrix, i, 0)
            result += (-1)**i * matrix[i][0] * determinant_recur(crossed_matrix)

    return result if result != int(result) else int(result)


def determinant(matrix) -> int:
    if len(matrix) != len(matrix[0]):
        raise ValueError('Cannot calculate a determinant of non-square matrix')
    return determinant_recur(matrix)


if __name__ == '__main__':
    m1 = [
        [1, -1, 2, 4],
        [0, 1, 0, 3],
        [5, 7, -2, 0],
        [2, 0, -1, 4]
    ]
    m2 = [
        [2, .5, 3],
        [0, 1.5, 5],
        [0, 0, 7]
    ]
    m3 = [
        [1, 3, 2],
        [0, 5, -1],
        [1, 3, 4]
    ]
    m4 = [
        [2, 7, -1, 3, 2],
        [0, 0, 1, 0, 1],
        [-2, 0, 7, 0, 2],
        [-3, -2, 4, 5, 3],
        [1, 0, 0, 0, 1]
    ]
    print(determinant(m4))
