from math import sqrt


def is_composite(num: int) -> bool:
    if num < 4:
        return False
    if not num % 2 or not num % 3:
        return True

    for div in range(5, int(sqrt(num))+1, 6):
        if not num % div or not num % (div + 2):
            return True
    return False


def count_composite_nums(ones_count: int, zeros_count: int) -> int:

    def recur(num=1, remaining_ones=ones_count-1, remaining_zeros=zeros_count):
        if not remaining_ones and not remaining_zeros:
            return is_composite(num)
        else:
            count = 0
            if remaining_zeros:
                count += recur(2*num, remaining_ones, remaining_zeros-1)
            if remaining_ones:
                count += recur(2*num + 1, remaining_ones-1, remaining_zeros)
            return count

    return recur()


if __name__ == '__main__':
    A = 2
    B = 3
    print(count_composite_nums(A, B))
