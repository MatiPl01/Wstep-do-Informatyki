# The best solution

def count_possible_placements(board_size: int):
    taken_columns = [False] * board_size
    taken_diagonal1 = [False] * (2*board_size-1)
    taken_diagonal2 = [False] * (2*board_size-1)

    def recur(row_idx=0):
        if row_idx == board_size:
            return 1

        count = 0
        for col_idx in range(board_size):
            if not (taken_columns[col_idx] or taken_diagonal1[row_idx + col_idx] or taken_diagonal2[row_idx - col_idx]):
                taken_columns[col_idx] = taken_diagonal1[row_idx + col_idx] = taken_diagonal2[row_idx - col_idx] = True
                count += recur(row_idx+1)
                taken_columns[col_idx] = taken_diagonal1[row_idx + col_idx] = taken_diagonal2[row_idx - col_idx] = False

        return count

    return recur()


if __name__ == '__main__':
    print(count_possible_placements(12))
