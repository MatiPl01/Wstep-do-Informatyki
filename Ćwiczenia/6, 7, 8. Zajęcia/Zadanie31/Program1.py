from math import sqrt
from functools import reduce
import operator


def prime_divisors(num: int) -> list:
    divisors = []

    if num == 0:
        return divisors

    if not num % 2:
        num //= 2
        divisors.append(2)
        while not num % 2:
            num //= 2

    div = 3
    while num > 1 and div <= int(sqrt(num)):
        if not num % div:
            divisors.append(div)
            while not num % div:
                num //= div
        div += 2

    if num > 1:
        divisors.append(num)

    return divisors


def product(nums):
    return reduce(operator.mul, nums)


def prime_divisors_subset_products_sum(num: int) -> int:
    if num < 0:
        raise ValueError('Cannot calculate prime divisors of a negative number')
    if not isinstance(num, int):
        raise TypeError(f"Expected 'int', got {str(type(2))[7:-1]}")

    divisors = prime_divisors(num)

    def recur(idx=-1, points=()):
        if idx == len(divisors)-1:
            return product(points) if points else 0

        idx += 1
        return recur(idx, points) + recur(idx, points + (divisors[idx],))

    return recur()


if __name__ == '__main__':
    n = 60
    print(prime_divisors_subset_products_sum(n))
