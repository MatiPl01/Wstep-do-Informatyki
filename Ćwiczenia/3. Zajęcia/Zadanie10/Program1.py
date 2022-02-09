def longest_consistent_arithmetic_substring(seq):
    if len(seq) < 2:
        return 0
    max_length = curr_length = 2
    r = seq[1] - seq[0]
    for i in range(2, len(seq)):
        curr_r = seq[i] - seq[i-1]
        if curr_r == r:
            curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
        else:
            r = curr_r
            curr_length = 2
    return max_length


if __name__ == '__main__':
    try:
        # n = int(input('(number of elements) > '))
        # t = [int(input(f'{i+1}. value > ')) for i in range(n)]
        t = [int(v) for v in input('(values) > ').split()]
    except ValueError:
        print('An error while processing input has occurred')
        exit()

    print(longest_consistent_arithmetic_substring(t))

'''
-1 3 411 2 34 12 3 412 3 6 9 12 15 19 123 412 31 2 334 12 3
'''
