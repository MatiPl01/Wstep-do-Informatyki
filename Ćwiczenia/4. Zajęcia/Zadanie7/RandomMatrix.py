import random


def create_random_nondecreasing_matrix(rows, columns, min_num, max_num):
    res = []
    for i in range(rows):
        row = [random.randint(min_num, max_num) for _ in range(columns)]
        res.append(sorted(row))
    return res


if __name__ == '__main__':
    rows = columns = 10
    min_num = 0
    max_num = 100

    res = create_random_nondecreasing_matrix(rows, columns, min_num, max_num)

    for row in res:
        print(' '.join(str(v) for v in row))
