import random


def random_matrix(rows, cols, min_num, max_num):
    return [[random.randint(min_num, max_num) for _ in range(cols)] for _ in range(rows)]


def get_number_digits(num):
    digits = set()

    while num and len(digits) < 10:  # If a number has all possible digits, end the loop
        num, dgt = divmod(num, 10)
        digits.add(dgt)

    return digits


def are_mates(a, b):
    return len(get_number_digits(a) & get_number_digits(b)) >= 2


def remove_non_mate_nums(matrix):
    have_mates = set()

    for i in range(len(matrix)**2):
        num1 = matrix[i//len(matrix)][i%len(matrix)]
        if num1 in have_mates:  # If already assessed that num1 has at least one mate, skip this number
            continue
        for j in range(i+1, len(matrix)**2):
            num2 = matrix[j//len(matrix)][j%len(matrix)]
            if are_mates(num1, num2):  # If True, go to another number
                have_mates.add(num1)
                have_mates.add(num2)
                break
        else:  # If a for loop hasn't been broken, there is not mate of the num1
            matrix[i//len(matrix)][i%len(matrix)] = 0


if __name__ == '__main__':
    N = 5
    min_num, max_num = 1, 100
    t = random_matrix(N, N, min_num, max_num)
    print(*t, sep='\n')
    remove_non_mate_nums(t)
    print(*t, sep='\n')
