import random
from pprint import pprint as pp


def random_matrix(rows: int, columns: int, min_num: int, max_num: int) -> [[int]]:
    return [[random.randint(min_num, max_num) for _ in range(rows)] for _ in range(columns)]


def search_subset(matrix, searched_sum) -> bool:
    if searched_sum < 0:
        return False

    def recur(row_idx=-1, curr_sum=0, remaining_cols=set(range(len(matrix[0])))):
        if row_idx == len(matrix)-1:
            # Check if current sum is the one desired and whether we have included any number in the subset
            return curr_sum == searched_sum and len(remaining_cols) != len(matrix[0])

        results = [recur(row_idx+1, curr_sum, remaining_cols)]
        for i in remaining_cols:
            results.append(recur(row_idx+1, curr_sum + matrix[row_idx][i], remaining_cols.difference({i})))

        return any(results)  # If any is True, return True

    return recur()


if __name__ == '__main__':
    sum_ = 500
    random.seed(0)
    t = random_matrix(8, 8, 0, 100)
    pp(t)
    print(search_subset(t, sum_))

    # res = get_all_subsets(t, sum_)
    # print(len(res), res)


# def get_all_subsets(matrix, searched_sum) -> list:
#     subsets = []
#
#     if searched_sum < 0:
#         return subsets
#
#     def recur(row_idx=-1, subset=[], remaining_cols=set(range(len(matrix[0])))):
#         if row_idx == len(matrix)-1:
#             # Check if current sum is the one desired and whether we have included any number in the subset
#             if sum(subset) == searched_sum and len(remaining_cols) != len(matrix[0]):
#                 subsets.append(subset)
#             return
#
#         results = [recur(row_idx+1, subset, remaining_cols)]
#         for i in remaining_cols:
#             results.append(recur(row_idx+1, subset + [matrix[row_idx][i]], remaining_cols.difference({i})))
#
#     recur()
#
#     return subsets
