import random


def random_fill(lst, min_num, max_num):
    for i in range(len(lst)):
        lst[i] = random.randint(min_num, max_num)


# def greatest_n_elements_sum(n, lst):
#     temp_lst = lst.copy()
#     for i in range(n):
#         for j in range(i+1, len(temp_lst)):
#             if temp_lst[j] > temp_lst[i]:
#                 temp_lst[j], temp_lst[i] = temp_lst[i], temp_lst[j]
#
#     return sum(temp_lst[:n])


def greatest_n_elements_sum(n, lst):
    greatest_idx = 0
    taken = set()  # A set of taken elements' indices
    sum_ = 0

    for _ in range(n):
        greatest_val = 0
        for i in range(len(lst)):
            if i not in taken and lst[i] > greatest_val:
                greatest_val = lst[i]
                greatest_idx = i

        taken.add(greatest_idx)
        sum_ += greatest_val

    return sum_


if __name__ == '__main__':
    MAX = 100
    tab = [0]*MAX
    random_fill(tab, 0, 1000)
    print(greatest_n_elements_sum(10, tab))
