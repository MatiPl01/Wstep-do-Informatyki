from math import sqrt


def is_prime(num: int) -> bool:
    if num in {2, 3}:
        return True
    if not num % 2 or not num % 3 or num < 2:
        return False

    for div in range(5, int(sqrt(num))+1, 6):
        if not num % div or not num % (div + 2):
            return False
    return True


def A(num: int) -> int:
    return num + 3


def B(num: int) -> int:
    return num * 2


def C(num: int) -> int:
    # I assume that num = 5 is the same as 05 which will be converted to 50
    num, last_dgt = divmod(num, 10)
    num, prev_dgt = divmod(num, 10)
    return 100*num + 10*last_dgt + prev_dgt


def can_modify_to_prime(num: int, max_steps: int) -> bool:

    def recur(curr_num=num, remaining_steps=max_steps, operations=''):
        if is_prime(curr_num):
            print(operations)
            return True

        if not remaining_steps:
            return False

        remaining_steps -= 1
        return recur(A(curr_num), remaining_steps, operations + 'A')\
            or recur(B(curr_num), remaining_steps, operations + 'B')\
            or recur(C(curr_num), remaining_steps, operations + 'C')

    return recur()


if __name__ == '__main__':
    num = 49
    n = 2
    print(can_modify_to_prime(num, n))
