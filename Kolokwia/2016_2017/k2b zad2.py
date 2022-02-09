import random


def random_matrix(rows, cols, min_num, max_num):
    return [[random.randint(min_num, max_num) for _ in range(cols)] for _ in range(rows)]


def remove_towers(board, towers_rows):
    # Preprocess data (save column indices of towers in each row)
    towers_dict = {}
    towers_in_row_count = {}
    rows_without_towers = set(range(len(board)))
    cols_without_towers = set()  # We know that initially in every column there is one tower

    for col_idx, row_idx in enumerate(towers_rows):
        towers_dict[col_idx] = row_idx
        towers_in_row_count.setdefault(row_idx, 0)
        towers_in_row_count[row_idx] += 1
        if row_idx in rows_without_towers:
            rows_without_towers.remove(row_idx)

    # A helper function to check the sum of fields that are in check by the current tower
    def sum_fields_in_check(row, col):
        sum_ = 0
        # If there is no tower in a row, we are sure that this field is in check by the current tower
        # as there are no more towers in the same column
        for row_idx in rows_without_towers:
            sum_ += board[row_idx][col]

        # If there is no other tower in the same row, we have to add values from the remaining columns
        # of this row where are no towers
        if towers_in_row_count[row] == 1:  # Our current tower is the only one
            for col_idx in cols_without_towers:
                sum_ += board[row][col_idx]
        else:
            # If we remove the current tower, field that wasn't counted to the sum will be now counted
            # As it will get checked by another tower from this row
            sum_ -= board[row][col]

        return sum_

    # A helper function that removes a tower that has fields of the greatest sum in check
    def remove_tower():
        max_sum = -1  # or float('-inf') for negative integers
        max_sum_row = None
        max_sum_col = None

        for col_idx, row_idx in towers_dict.items():
            sum_ = sum_fields_in_check(row_idx, col_idx)
            if sum_ > max_sum:
                max_sum = sum_
                max_sum_row, max_sum_col = row_idx, col_idx

        if max_sum_row:
            towers_dict.pop(max_sum_col)
            rows_without_towers.add(max_sum_row)
            cols_without_towers.add(max_sum_col)
            towers_in_row_count[max_sum_row] -= 1
            # print(max_sum_row, max_sum_col, max_sum)

        return max_sum_col

    return [remove_tower() for _ in range(2)]


if __name__ == '__main__':
    w = [1, 5, 2, 3, 2, 1]
    random.seed(5)
    t = random_matrix(len(w), len(w), 0, 100)
    print(*t, sep='\n')
    print(remove_towers(t, w))
