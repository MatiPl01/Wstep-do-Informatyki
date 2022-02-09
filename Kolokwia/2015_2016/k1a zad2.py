def func(seq: 'sequence of numbers') -> int:
    if len(seq) < 2:
        return 0

    max_inc_length = curr_inc_length = 2
    max_dec_length = curr_dec_length = 2
    for i in range(1, len(seq)-1):
        if seq[i-1] + seq[i+1] == 2 * seq[i] != 0:
            if seq[i+1] - seq[i] > 0:
                curr_inc_length += 1
                if curr_inc_length > max_inc_length:
                    max_inc_length = curr_inc_length
            else:
                curr_dec_length += 1
                if curr_dec_length > max_dec_length:
                    max_dec_length = curr_dec_length
        else:
            curr_inc_length = curr_dec_length = 2

    return max_inc_length - max_dec_length


if __name__ == '__main__':
    print(func([6, 9, 4, 8, 4, 8, 5, 3, 6, 4, 2, 5, 9, 6, 3, 1, 8, 10, 10, 1, 7, 3, 3, 8, 3]))
