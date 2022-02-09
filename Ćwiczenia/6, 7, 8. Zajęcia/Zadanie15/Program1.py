def can_be_placed(col_idx: int, taken_cols) -> bool:
    for i in range(len(taken_cols)):
        d_x = abs(i - len(taken_cols))
        d_y = abs(taken_cols[i] - col_idx)
        if taken_cols[i] == col_idx or d_x == d_y:
            return False
    return True


def count_possible_placements(board_size: int):
    taken_columns = []

    def recur():
        if len(taken_columns) == board_size:
            return 1

        count = 0
        for col_idx in range(board_size):
            if can_be_placed(col_idx, taken_columns):
                taken_columns.append(col_idx)
                count += recur()
                taken_columns.pop()

        return count

    return recur()


if __name__ == '__main__':
    print(count_possible_placements(10))
