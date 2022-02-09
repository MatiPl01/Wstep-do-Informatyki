def get_number_digits(num):
    digits = set()

    while num and len(digits) < 10:  # If a number has all possible digits, end the loop
        num, dgt = divmod(num, 10)
        digits.add(dgt)

    return digits


def are_friends(a, b):
    return get_number_digits(a) == get_number_digits(b)


def are_surrounding_elements_friends(matrix, row_idx, col_idx):
    for i in range(max(0, row_idx-1), min(len(matrix), row_idx+2)):
        for j in range(max(0, col_idx-1), min(len(matrix[0]), col_idx+2)):
            if not are_friends(matrix[row_idx][col_idx], matrix[i][j]):
                return False
    # print(row_idx, col_idx)
    return True


def count_matching_numbers(matrix):
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if are_surrounding_elements_friends(matrix, i, j):
                count += 1

    return count


if __name__ == '__main__':
    t = [
        [123, 12222223, 32211, 321, 12],
        [32121312, 321, 231, 3213, 42],
        [12, 12, 13, 2324, 3213],
        [211221, 1112, 414, 414, 421],
        [121, 2221, 231, 321, 32]
    ]
    # print(*t, sep='\n')
    print(count_matching_numbers(t))
