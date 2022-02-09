def check_if_queens_checkmate(num_rows, num_cols, coords):
    taken_rows = [0]*num_rows
    taken_cols = [0]*num_cols
    taken_tl_br_diagonal = [0]*(num_cols + num_rows)
    taken_tr_bl_diagonal = [0]*(num_cols + num_rows)

    for r, c in coords:
        if taken_rows[r] or taken_cols[c] or taken_tl_br_diagonal[r+c] or taken_tr_bl_diagonal[r-c]:
            return True  # Return True if found a queen that is in check
        else:
            taken_rows[r] = taken_cols[c] = taken_tl_br_diagonal[r+c] = taken_tr_bl_diagonal[r-c] = 1

    return False


if __name__ == '__main__':
    # t = [(0, 0), (1, 2), (2, 4), (4, 1)]
    t = [(0, 0), (1, 2), (2, 3), (4, 1)]
    N = 100
    print(check_if_queens_checkmate(N, N, t))
