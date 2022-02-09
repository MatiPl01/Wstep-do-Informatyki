def input_sequence() -> list:
    res = []
    while True:
        val = int(input())
        if val == 0:
            break
        res.append(val)
    return res


# def get_nth_greatest_value(n: int, seq: 'an iterable') -> int:
#     saved_values_indices = set()
#     nth_max_value = -1
#     seq = list(set(seq))
#
#     for _ in range(n):
#         curr_max_idx = 0
#         curr_max_val = -1
#
#         for idx, val in enumerate(seq):
#             if idx not in saved_values_indices and val > curr_max_val:
#                 curr_max_val = val
#                 curr_max_idx = idx
#
#         # Store an index of the currently greatest value to skip it next time
#         saved_values_indices.add(curr_max_idx)
#         nth_max_value = curr_max_val
#
#     return nth_max_value

def get_nth_greatest_value(n: int, seq: 'an iterable') -> int:
    return sorted(set(seq), reverse=True)[n-1]


if __name__ == '__main__':
    t = input_sequence()
    print(get_nth_greatest_value(10, t))


'''
1
2
3
2
3
4
5
6
7
8
9
9
11
12
13
0
'''