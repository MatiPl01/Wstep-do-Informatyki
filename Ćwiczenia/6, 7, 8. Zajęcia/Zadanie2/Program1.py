from math import sqrt
import random


def weight(n: int) -> int:
    factors_count = 0

    if not n % 2:
        n //= 2
        factors_count += 1
        while not n % 2:
            n //= 2

    div = 3
    while n > 1 and div <= int(sqrt(n)):
        if not n % div:
            factors_count += 1
            while not n % div:
                n //= div
        div += 2

    if n > 1:
        factors_count += 1

    return factors_count


def can_distribute_numbers(seq) -> bool:

    def distribute(num_idx=0, w1=0, w2=0, w3=0):
        if num_idx == len(seq):
            return w1 == w2 == w3

        num_weight = weight(seq[num_idx])
        num_idx += 1

        return distribute(num_idx, w1 + num_weight, w2, w3)\
            or distribute(num_idx, w1, w2 + num_weight, w3)\
            or distribute(num_idx, w1, w2, w3 + num_weight)

    return distribute()


# def distribute_numbers(seq) -> tuple:
#
#     def distribute(num_idx=0, set1=set(), w1=0, set2=set(), w2=0, set3=set(), w3=0):
#         if num_idx == len(seq):
#             if w1 == w2 == w3:
#                 return set1, set2, set3
#             else:
#                 return None
#
#         num = seq[num_idx]
#         num_weight = weight(num)
#         num_idx += 1
#
#         return distribute(num_idx, set(set1).union({num}), w1 + num_weight, set2, w2, set3, w3)\
#             or distribute(num_idx, set1, w1, set(set2).union({num}), w2 + num_weight, set3, w3)\
#             or distribute(num_idx, set1, w1, set2, w2, set(set3).union({num}), w3 + num_weight)
#
#     return distribute()


if __name__ == '__main__':
    random.seed(0)
    t = [random.randint(0, 1000) for _ in range(20)]
    print(t)
    print(can_distribute_numbers(t))
