import random


def create_random_matrix(rows, columns, digits_to_use, min_digits_count, max_digits_count):
    """Creates a 2-dimensional list of specified number of rows and columns
    filled with random integer values from range 'min_num' to 'max_num'"""
    for i in range(rows):
        for j in range(columns):
            num_digits = random.randint(min_digits_count, max_digits_count)
            digits = random.choices(digits_to_use, k=num_digits)
            print(int(''.join(str(v) for v in digits)), end=' ')
        print()


if __name__ == '__main__':
    rows = columns = 25
    digits_to_use = (0, 1, 2)
    min_digits_count = 2
    max_digits_count = 5
    create_random_matrix(rows, columns, digits_to_use, min_digits_count, max_digits_count)
