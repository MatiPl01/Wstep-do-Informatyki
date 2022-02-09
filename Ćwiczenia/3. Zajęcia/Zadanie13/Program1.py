# Quite slow solution
import random


class NewSequenceFound(Exception):
    pass


if __name__ == '__main__':
    N = int(input('> '))
    t = [random.randint(100, 999) for _ in range(N)]

    # t = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
    # t = [1, 2, 3, 2, 1]

    max_length = 0
    for length in range(2, len(t)+1):
        # print(length)
        try:
            for i in range(len(t)-length+1):
                seq = t[i:i+length]

                for j in range(i, len(t)-length+1):
                    begin_idx = j-1 if j >= 1 else None
                    reversed_seq = t[j+length-1:begin_idx:-1]

                    if seq == reversed_seq:
                        max_length = length
                        raise NewSequenceFound()
        except NewSequenceFound:
            continue

    print(max_length)
