from time import perf_counter
from functools import wraps
import random

REPS = 1


def performance(reps=1000):
    """Measures a performance of the function execution"""
    def decorator(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            total_t = 0
            res = None
            for _ in range(reps):
                start_t = perf_counter()
                res = fn(*args, **kwargs)
                end_t = perf_counter()
                total_t += end_t - start_t
            print(f'Total execution time: {total_t}s')
            print(f'Number of repetitions: {reps}')
            print(f'Average function runtime: {total_t / reps}s')
            return res
        return inner
    return decorator


class NewSequenceFound(Exception):
    pass


@performance(REPS)
def slices_solution(t):
    max_length = 0
    for length in range(2, len(t) + 1):
        try:
            for i in range(len(t) - length + 1):
                seq = t[i:i + length]

                for j in range(i, len(t) - length + 1):
                    begin_idx = j - 1 if j >= 1 else None
                    reversed_seq = t[j+length-1:begin_idx:-1]

                    if seq == reversed_seq:
                        max_length = length
                        print('slices_solution', seq, reversed_seq, i, j+length-1)
                        raise NewSequenceFound()
        except NewSequenceFound:
            continue
    return max_length


@performance(REPS)
def looping_solution(t):
    max_length = 1
    for length in range(max_length + 1, len(t) + 1):
        try:
            # Iterate from left to right over a range of possible beginning indices of a substring of a proper length
            for i in range(len(t) - length + 1):
                # Iterate from right to left to asses whether a reversed substring is found
                for j in range(len(t) - 1, i + length - 2, -1):
                    i_cp, j_cp = i, j
                    for _ in range(length):
                        if t[i] != t[j]:
                            break
                        i += 1
                        j -= 1
                    else:
                        max_length = length
                        # Go back to the main loop after new longest substring is found
                        print('looping_solution', t[i_cp:i_cp+length], t[j_cp-length+1:j_cp+1], i_cp, j_cp)
                        raise NewSequenceFound()
        except:
            continue

    return max_length if max_length > 1 else 0


@performance(REPS)
def dictionary_solution(t):
    # Create dictionary holding indices of the same numbers
    helper_dict = {}
    for idx, val in enumerate(t):
        helper_dict.setdefault(val, [])
        helper_dict[val].append(idx)

    # Start searching for a reversed substring
    max_length = 0
    for i, curr_val in enumerate(t):
        for j in helper_dict[curr_val]:
            length = 1
            i_cp, j_cp = i, j
            while j_cp > 0 and i_cp < len(t) - 1:
                i_cp += 1
                j_cp -= 1
                if t[i_cp] != t[j_cp]:
                    break
                length += 1
            if length > max_length:
                print('dictionary_solution', t[i:i+length], t[j-length+1:j+1], i, j)
                max_length = length

    return max_length if max_length > 1 else 0


if __name__ == '__main__':
    N = int(input('> '))
    # random.seed(7)
    # N = 500
    t = [random.randint(100, 999) for _ in range(N)]
    # t = [2, 9, 3, 1, 7, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]

    # print(slices_solution(t))
    # print(looping_solution(t))
    print(dictionary_solution(t))
