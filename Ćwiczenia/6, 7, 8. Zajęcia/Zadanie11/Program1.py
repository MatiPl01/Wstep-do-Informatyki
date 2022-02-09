import random


def random_list(length: int, min_num: int, max_num: int) -> list:
    return [random.randint(min_num, max_num) for _ in range(length)]


def count_matching_numbers(seq, count: int, product: int) -> int:
    if not 0 < count <= len(seq):
        return -1

    def recur(idx=0, curr_product=1, nums_multiplied=0):
        if curr_product == product and nums_multiplied == count:
            return 1
        if nums_multiplied > count or idx == len(seq):
            return 0

        return recur(idx+1, curr_product * seq[idx], nums_multiplied+1) + recur(idx+1, curr_product, nums_multiplied)

    return recur()


if __name__ == '__main__':
    # T = random_list(20, 0, 30)
    T = [2, 0, 3, 4, 5]
    print(T)
    print(count_matching_numbers(T, 3, 0))
