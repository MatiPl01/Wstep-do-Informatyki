A = lambda num: num+3
B = lambda num: 2*num


def C(num: int) -> int:
    new_num = 0
    mul = 1

    while num:
        num, digit = divmod(num, 10)
        if digit % 2 == 0:
            digit += 1
        new_num += mul * digit
        mul *= 10

    return new_num


def check_condition_init(operations: 'iterable') -> "'check_condition' function":
    def check_condition(curr_num: int, final_num: int, max_steps: int, curr_step: int = 0, last_op_idx: int = -1) -> int:
        if curr_step > max_steps:
            return 0
        if curr_num == final_num:
            return 1
        curr_sum = 0
        for idx, operation in enumerate(operations):
            if idx != last_op_idx:
                curr_sum += check_condition(operation(curr_num), final_num, max_steps, curr_step+1, idx)
        return curr_sum

    return check_condition


if __name__ == '__main__':
    X = int(input('(X) > '))
    Y = int(input('(Y) > '))
    N = int(input('(N) > '))
    check_condition = check_condition_init((A, B, C))
    print(check_condition(X, Y, N))


'''
11
31
4

11
32
4
'''
