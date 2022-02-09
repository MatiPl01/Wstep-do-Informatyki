from math import sqrt
from functools import wraps


class PathFound(Exception):
    """An Exception used to indicate that a path from the beginning of a sequence
    to the last index is found."""
    pass


def memoized(fn):
    """A decorator function that is used to cache values returned by the decorated
    function. Uses memoized values when possible to decrease function's execution time."""
    cache = {}

    @wraps(fn)
    def inner(arg):
        if arg not in cache:
            # print(f'Calculating fn({arg})')
            cache[arg] = fn(arg)
        return cache[arg]

    return inner


@memoized
def factors(num: int) -> set:
    """Calculates prime factors of a given number excluding repetitions of the same factor."""
    for div in range(2, int(sqrt(num))+2):
        if num % div == 0:
            return {div, *factors(num//div)}
    else:
        return {num} if num > 1 else {}


num_traversals = 0


def traverse(k: int, lst: 'any iterable', *, visited=set()):
    """Traverses through the iterable until the last index is reached.
    Raises PathFound() exception to stop recursion when reached the end of a sequence.
    """
    global num_traversals
    num_traversals += 1

    for n in factors(lst[k]):
        next_idx = n + k
        if next_idx == len(lst)-1:
            print(f'Last jump: ({lst[k]}) {k} -> {k + n} ({lst[k + n]})')
            raise PathFound()
        if next_idx not in visited and next_idx < len(lst):
            visited.add(next_idx)
            print(f'({lst[k]}) {k} -> {k + n} ({lst[k + n]})\tVisited {len(visited)} elements.')
            traverse(next_idx, lst, visited=visited)


def can_reach_end(start_idx: int, lst: 'any iterable') -> bool:
    """Assesses whether it is possible to reach the last index of an iterable."""
    try:
        traverse(start_idx, lst)
    except PathFound:
        return True
    return False


if __name__ == '__main__':
    n = int(input('(number of elements) > '))
    t = [int(input(f'{i+1}. value > ')) for i in range(n)]

    t = [int(v) for v in input('(values) > ').split()]
