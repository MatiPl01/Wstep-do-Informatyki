# Fastest (1874x faster than Zadanie1 for 500 elements)
import random


class NewSequenceFound(Exception):
    pass


if __name__ == '__main__':
    N = int(input('> '))
    t = [random.randint(100, 999) for _ in range(N)]

    # t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
    # t = [1, 2, 3, 2, 1]

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
            while j_cp > 0 and i_cp < len(t)-1:
                i_cp += 1
                j_cp -= 1
                if t[i_cp] != t[j_cp]:
                    break
                length += 1
            if length > max_length:
                print(t[i:i+length], t[j-length+1:j+1], i, j)
                max_length = length

    print(max_length if max_length > 1 else 0)
