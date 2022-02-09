import random


def random_list(length: int, min_num: int, max_num: int) -> list:
    return [random.randint(min_num, max_num) for _ in range(length)]


def get_matching_numbers(seq, count: int, product: int) -> list:
    if not 0 < count <= len(seq):
        return []

    results = []

    def recur(idx=0, curr_product=1, nums_multiplied=0, nums=()):
        if curr_product == product and nums_multiplied == count:
            results.append(nums)

        elif nums_multiplied < count and idx < len(seq):
            recur(idx+1, curr_product * seq[idx], nums_multiplied+1, nums + (seq[idx],))
            recur(idx+1, curr_product, nums_multiplied, nums)

    recur()

    return results


if __name__ == '__main__':
    # T = random_list(20, 0, 30)
    T = [2, 0, 3, 4, 5]
    print(T)
    print(get_matching_numbers(T, 3, 0))
