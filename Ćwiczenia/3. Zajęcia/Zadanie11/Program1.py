def longest_consistent_geometric_substring(seq):
    if len(seq) < 2:
        return 0
    max_length = curr_length = 0
    prev_q = None
    for i in range(len(seq)-1):
        try:
            if prev_q is None or seq[i] * prev_q != seq[i+1]:
                prev_q = seq[i+1] / seq[i]
                curr_length = 2
            else:
                curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
        except ZeroDivisionError:
            continue
    return max_length


if __name__ == '__main__':
    # n = int(input('(number of elements) > '))
    # t = [int(input(f'{i+1}. value > ')) for i in range(n)]
    t = [int(v) for v in input('(values) > ').split()]
    print(longest_consistent_geometric_substring(t))

'''
0 1
123 0
-5 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
9 123 12 -5 43 789 4 8 16 32 64 8 1 0 0 1 2 0 3 0 2 9 -43 1
'''
