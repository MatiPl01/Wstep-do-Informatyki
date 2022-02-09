import random

if __name__ == '__main__':
    n = int(input('> '))

    for _ in range(100):  # A loop to show more cases
        t = [random.randint(1, 99) for _ in range(n)]
        max_inc_length = 0
        max_dec_length = 0
        r = None

        for i in range(len(t)-1):
            curr_r = t[i+1] - t[i]
            if curr_r != r:
                r = curr_r
                if r > 0:
                    inc_length = 2
                    dec_length = 0
                else:
                    inc_length = 0
                    dec_length = 2
            else:
                if curr_r > 0:
                    inc_length += 1
                    if inc_length > max_inc_length:
                        max_inc_length = inc_length
                else:
                    dec_length += 1
                    if dec_length > max_dec_length:
                        max_dec_length = dec_length

        print(max_inc_length - max_dec_length)
