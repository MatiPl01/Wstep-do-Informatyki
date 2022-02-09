import random
from math import sqrt
from functools import wraps


def memoized(fn):
    """A decorator function that is used to cache values returned by the decorated
    function. Uses memoized values when possible to decrease function's execution time."""
    cache = {}

    @wraps(fn)
    def inner(arg):
        if arg not in cache:
            print(f'Calculating fn({arg})')
            cache[arg] = fn(arg)
        return cache[arg]

    return inner


@memoized
def factors(num: int) -> tuple:
    """Calculates prime factors of a given number including repetitions of the same factor."""
    for div in range(2, int(sqrt(num))+2):
        if num % div == 0:
            return div, *factors(num//div)
    else:
        return (num,) if num > 1 else ()


if __name__ == '__main__':
    n = int(input('(number of elements) > '))
    # t = [int(input(f'{i+1}{["st", "nd", "rd", "th"][min(i, 3)]} element > ')) for i in range(n)]
    # t = [int(n) for n in input('> ').split()]
    t = [random.randint(1, 999) for _ in range(n)]
    # t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]

    curr_length = max_length = 0
    curr_mul_factors = set()

    curr_seq = longest_seq = []

    for num in t:
        curr_num_factors = factors(num)
        for factor in curr_num_factors:
            if factor not in curr_mul_factors:
                curr_mul_factors.add(factor)
            else:
                curr_length = 0
                curr_mul_factors = set()
                curr_seq = []
                break
        else:
            curr_length += 1
            curr_seq.append(num)
            if curr_length > max_length:
                max_length = curr_length
                longest_seq = curr_seq

    print(max_length)
    print(longest_seq)
