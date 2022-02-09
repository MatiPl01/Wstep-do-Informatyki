def range_set(end_num: int) -> set:
    return set(range(end_num))


def count_possible_placements(board_size: int):
    free_columns = range_set(board_size)
    free_diagonal1 = range_set(2*board_size)
    free_diagonal2 = free_diagonal1.copy()

    def recur(row_idx=0):
        if row_idx == board_size:
            return 1

        count = 0
        for col_idx in free_columns.copy():
            diagonal1_idx = row_idx + col_idx
            diagonal2_idx = board_size + row_idx - col_idx

            if diagonal1_idx in free_diagonal1 and diagonal2_idx in free_diagonal2:
                free_columns.remove(col_idx)
                free_diagonal1.remove(diagonal1_idx)
                free_diagonal2.remove(diagonal2_idx)

                count += recur(row_idx+1)
                free_columns.add(col_idx)
                free_diagonal1.add(diagonal1_idx)
                free_diagonal2.add(diagonal2_idx)

        return count

    return recur()


if __name__ == '__main__':
    print(count_possible_placements(12))
