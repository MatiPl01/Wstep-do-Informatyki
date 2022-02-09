def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    for i in range(len(matrix)):
        while True:
            row = input().split()
            if len(row) == len(matrix[i]):
                break
            print(f"Expected {len(matrix[i])} values, got {len(row)}.")
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def rewrite_singletons(source_matrix: [[int]], target_list: list):
    """Rewrites singleton values from 'source_matrix' to 'target_matrix' in an increasing order.
    Note that all rows in 2-dimensional 'source_matrix' list must be sorted in an increasing
    order as well."""
    # Store information about values that appear more than once in the 'source_matrix'
    checked_values = set()
    excluded_values = set()
    for row_idx in range(len(source_matrix)):
        for col_idx in range(len(source_matrix[row_idx])):
            val = source_matrix[row_idx][col_idx]
            if val in checked_values:
                excluded_values.add(val)
            else:
                checked_values.add(val)
    del checked_values

    # Trace position of pointers in each row of 'source_matrix' to move appropriate values
    pointers = dict.fromkeys(range(len(source_matrix)), 0)

    rewritten_elements = 0

    while pointers:
        lowest_val = lowest_val_row_idx = None
        pointers_to_remove = []

        # Look for the lowest value and store all its occurrences (whe repeated)
        for row_idx in pointers.keys():
            while source_matrix[row_idx][pointers[row_idx]] in excluded_values:
                pointers[row_idx] += 1
                if pointers[row_idx] >= len(source_matrix[row_idx]):
                    pointers_to_remove.append(row_idx)
                    break
            else:
                curr_val = source_matrix[row_idx][pointers[row_idx]]
                if not lowest_val or curr_val < lowest_val:
                    lowest_val = curr_val
                    lowest_val_row_idx = row_idx

        # Save lowest value found in the target list
        target_list[rewritten_elements] = lowest_val
        rewritten_elements += 1
        pointers[lowest_val_row_idx] += 1
        if pointers[lowest_val_row_idx] >= len(source_matrix[lowest_val_row_idx]):
            pointers_to_remove.append(lowest_val_row_idx)

        # Remove useless pointers
        for pointer in pointers_to_remove:
            pointers.pop(pointer)


if __name__ == '__main__':
    N = int(input())
    t1 = create_matrix(N, N)
    t2 = create_matrix(1, N * N)[0]
    fill_matrix(t1)
    print(t2)
    rewrite_singletons(t1, t2)
    print(t2)

'''
10
2 22 40 68 77 77 86 92 94 100
47 48 49 52 67 68 79 85 90 100
2 23 24 28 52 90 91 95 100 100
2 5 14 28 47 48 50 56 70 71
1 7 9 18 21 32 33 62 63 90
34 52 56 57 68 80 85 86 96 100
2 8 17 38 39 39 43 43 66 89
13 21 26 49 53 59 90 93 96 99
2 6 13 15 34 64 70 72 72 91
32 40 50 63 69 70 75 75 79 91
'''
