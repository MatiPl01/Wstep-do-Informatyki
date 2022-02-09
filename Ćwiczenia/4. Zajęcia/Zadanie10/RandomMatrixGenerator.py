import random


def create_random_matrix(rows: int, columns: int, min_num: int, max_num: int, higher_probability_value: tuple):
    """Creates a 2-dimensional list of specified number of rows and columns
    filled with random integer values from 'range min_num' to 'max_num'"""
    high_prob_val, probability = higher_probability_value

    for i in range(rows):
        for j in range(columns):
            if 0 <= random.random() < probability:
                print(high_prob_val, end=' ')
            else:
                print(random.randint(min_num, max_num), end=' ')
        print()


if __name__ == '__main__':
    rows = columns = 10
    max_num = 100
    min_num = -100
    higher_probability_value = (0, .25)
    create_random_matrix(rows, columns, min_num, max_num, higher_probability_value)
