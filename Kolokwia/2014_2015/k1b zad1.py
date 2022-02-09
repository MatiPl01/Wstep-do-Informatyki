def input_sequence() -> list:
    res = []
    while True:
        val = int(input())
        if val == 0:
            break
        res.append(val)
    return res


def get_range(idx: int, length: int) -> range:
    if idx < 2:
        return range(5)
    elif length-idx-1 < 2:
        return range(length-5, length)
    else:
        return range(idx-2, idx+3)


def get_mean(idx: int, seq) -> float:
    sum_ = 0
    for i in get_range(idx, len(seq)):
        sum_ += seq[i]
    return (sum_ - seq[idx]) / 4


def get_matching_nums(seq: list):
    res = []
    for i in range(len(seq)):
        if get_mean(i, seq) == seq[i]:
            res.append(seq[i])
    return res


if __name__ == '__main__':
    t = input_sequence()
    print(get_matching_nums(t))

'''
2
3
2
7
1
2
4
8
5
2
2
4
3
9
5
4
0
'''
