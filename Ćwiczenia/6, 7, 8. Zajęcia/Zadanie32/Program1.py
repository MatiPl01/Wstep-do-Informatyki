import random


def random_nums(count: int, min_num: int, max_num: int) -> list:
    return [random.randint(min_num, max_num) for _ in range(count)]


def func(seq, cardinality: int) -> bool:

    def recur(idx=-1, set1_sum=0, set2_sum=0, remaining_count=cardinality):
        if not remaining_count:
            return set1_sum == set2_sum
        if idx == len(seq)-1:
            return False

        idx += 1
        num = seq[idx]
        return recur(idx, set1_sum, set2_sum, remaining_count)\
            or recur(idx, set1_sum + num, set2_sum, remaining_count-1)\
            or recur(idx, set1_sum, set2_sum + num, remaining_count-1)

    return recur()


if __name__ == '__main__':
    # random.seed(0)
    T = random_nums(100, 0, 1000)
    k = 10
    print(func(T, k))


# def func(seq, cardinality: int) -> tuple:
#
#     def recur(idx=-1, set1_sum=0, set2_sum=0, set1=(), set2=(), remaining_count=cardinality):
#         if not remaining_count and set1_sum == set2_sum:
#             return set1, set2
#         if idx == len(seq)-1:
#             return False
#
#         idx += 1
#         num = seq[idx]
#         return recur(idx, set1_sum, set2_sum, set1, set2, remaining_count)\
#             or recur(idx, set1_sum + num, set2_sum, set1 + (num,), set2, remaining_count-1)\
#             or recur(idx, set1_sum, set2_sum + num, set1, set2 + (num,), remaining_count-1)
#
#     return recur()
