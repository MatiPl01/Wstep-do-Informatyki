import random


def create_random_matrix(rows: int, columns: int, min_num: int, max_num: int) -> '2-dimensional list':
    """Creates a 2-dimensional list of specified number of rows and columns
    filled with random integer values from range 'min_num' to 'max_num'"""
    print(rows)
    for i in range(rows):
        for j in range(columns):
            print(random.randint(min_num, max_num), end=' ')
        print()


if __name__ == '__main__':
    # rows = columns = 15
    rows = 1
    columns = 250
    min_num, max_num = 0, 100
    # for _ in range(rows):
    create_random_matrix(rows, columns, min_num, max_num)
