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


def count_built_primes(num1: int, num2: int) -> int:
    count = 0

    def recur(rest1, rest2, built_num=0, mul=1):
        if not rest1 and not rest2 and is_prime(built_num):
            nonlocal count
            count += 1
        else:
            if rest1:
                rest1_new, digit1 = divmod(rest1, 10)  # Take the last digit of the rest1
                recur(rest1_new, rest2, mul * digit1 + built_num, mul * 10)
            if rest2:
                rest2_new, digit2 = divmod(rest2, 10)  # Take the last digit of the rest2
                recur(rest1, rest2_new, mul * digit2 + built_num, mul * 10)

    recur(num1, num2)

    return count


if __name__ == '__main__':
    a = 123
    b = 758
    print(count_built_primes(a, b))
