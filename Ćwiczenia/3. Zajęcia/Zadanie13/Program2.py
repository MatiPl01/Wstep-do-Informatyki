# Slightly faster (1,65x faster than Zadanie1 for 500 elements (good for longer sequences))
import random


class NewSequenceFound(Exception):
    pass


if __name__ == '__main__':
    N = int(input('> '))
    t = [random.randint(100, 999) for _ in range(N)]

    # t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
    # t = [1, 2, 3, 2, 1]

    max_length = 1
    for length in range(max_length+1, len(t)+1):
        try:
            # Iterate from left to right over a range of possible beginning indices of a substring of a proper length
            for i in range(len(t)-length+1):
                # Iterate from right to left to asses whether a reversed substring is found
                for j in range(len(t)-1, i+length-2, -1):
                    # print('length', length, 'i', i, 'j', j)
                    for _ in range(length):
                        if t[i] != t[j]:
                            break
                        i += 1
                        j -= 1
                    else:
                        max_length = length
                        # Go back to the main loop after new longest substring is found
                        raise NewSequenceFound()
        except:
            # print('found', length)
            continue

    print(max_length if max_length > 1 else 0)
