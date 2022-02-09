def longest_consistent_substring(seq):
    if not seq:
        return 0
    max_length = curr_length = 0
    prev_val = seq[0]
    for val in seq[1:]:
        if val > prev_val:
            curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
        else:
            curr_length = 0
        prev_val = val
    return max_length if not max_length else max_length+1


if __name__ == '__main__':
    # n = int(input('(number of elements) > '))
    # t = [int(input(f'{i+1}. value > ')) for i in range(n)]
    t = [int(v) for v in input('(values) > ').split()]
    print(longest_consistent_substring(t))

'''
12 5 20 23 10 13 14 5 9 18 22 16 24 23 15 9 21 24 25 6 19 22 17
'''
