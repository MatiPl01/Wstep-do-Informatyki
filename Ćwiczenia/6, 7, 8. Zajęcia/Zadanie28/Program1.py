"""
Zadanie 28. Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Prosze napisac funkcje,
która zwraca informacje, czy jest mozliwy podział zbioru N liczb na trzy podzbiory, tak aby w kazdym
podzbiorze, łaczna liczba jedynek uzyta do zapisu elementów tego podzbioru w systemie dwójkowym była
jednakowa. Na przykład: [2, 3, 5, 7, 15] -> True, bo podzbiory {2,7} {3,5} {15} wymagaja uzycia 4 jedynek,
[5, 7, 15] -> False, podział nie istnieje.
"""


def count_bin_ones(num: int) -> int:
    count = 0

    while num:
        num, digit = divmod(num, 2)
        count += digit

    return count


def can_create_equal_bin_ones_subsets(seq) -> bool:
    ones_counts = [count_bin_ones(n) for n in seq]

    def recur(idx=-1, set1_ones=0, set2_ones=0, set3_ones=0):
        if idx == len(seq)-1:
            return set1_ones == set2_ones == set3_ones

        idx += 1
        next_num_ones = ones_counts[idx]
        return recur(idx, set1_ones + next_num_ones, set2_ones, set3_ones)\
            or recur(idx, set1_ones, set2_ones + next_num_ones, set3_ones)\
            or recur(idx, set1_ones, set2_ones, set3_ones + next_num_ones)\

    return recur()


# def get_equal_bin_ones_subsets(seq) -> (set, set, set):
#     ones_counts = [count_bin_ones(n) for n in seq]
#
#     def recur(idx=0, set1_ones=0, set2_ones=0, set3_ones=0, set1=set(), set2=set(), set3=set()):
#         if idx == len(seq):
#             if set1_ones == set2_ones == set3_ones:
#                 return set1, set2, set3
#             else:
#                 return None
#
#         next_num_ones = ones_counts[idx]
#         return recur(idx+1, set1_ones + next_num_ones, set2_ones, set3_ones, set1.union({seq[idx]}), set2, set3)\
#             or recur(idx+1, set1_ones, set2_ones + next_num_ones, set3_ones, set1, set2.union({seq[idx]}), set3)\
#             or recur(idx+1, set1_ones, set2_ones, set3_ones + next_num_ones, set1, set2, set3.union({seq[idx]}))\
#
#     return recur() or (set(), set(), set())


if __name__ == '__main__':
    # T = [23, 64, 8, 9, 31, 45, 44, 32, 63, 72, 47, 66, 99, 72, 21]
    T = [4, 22, 12, 5, 6, 12, 1, 8, 9, 3]
    print(can_create_equal_bin_ones_subsets(T))
