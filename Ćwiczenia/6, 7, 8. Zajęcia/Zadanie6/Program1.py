def min_size_matching_subset_sum(seq) -> int:
    min_values_count = len(seq)+1
    min_count_sum = 0

    def recur(idx=0, sum_values=0, sum_indices=0, values_count=0):
        nonlocal min_values_count, min_count_sum

        if values_count < min_values_count and min_values_count > 1:

            if values_count and sum_indices == sum_values:
                min_values_count = values_count
                min_count_sum = sum_values

            elif idx < len(seq):
                recur(idx+1, sum_values + seq[idx], sum_indices + idx, values_count+1)
                recur(idx+1, sum_values, sum_indices, values_count)

    recur()

    return min_count_sum if min_values_count <= len(seq) else None


# def min_size_matching_subsets(seq) -> list:
#     min_values_count = len(seq)+1
#     min_count_subsets = []
#
#     def recur(idx=0, sum_values=0, sum_indices=0, values={}):
#         nonlocal min_values_count, min_count_subsets
#
#         if len(values) <= min_values_count and min_values_count >= 1:
#
#             if values and sum_indices == sum_values:
#                 if len(values) < min_values_count:
#                     min_values_count = len(values)
#                     min_count_subsets = [values]
#                 else:
#                     min_count_subsets.append(values)
#
#             elif idx < len(seq):
#                 recur(idx+1, sum_values + seq[idx], sum_indices + idx, {**values, idx: seq[idx]})
#                 recur(idx+1, sum_values, sum_indices, values)
#
#     recur()
#
#     return min_count_subsets if min_values_count <= len(seq) else {}


if __name__ == '__main__':
    T = [1, 7, 3, 5, 11, 2]
    print(min_size_matching_subset_sum(T))  # There are two possible solutions (8 and 10) so the task is slightly wrong
