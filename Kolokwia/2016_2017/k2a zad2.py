def create_matrix(rows: int, columns: int, *, fill_with=0):
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    for i in range(len(matrix)):
        while True:
            row = input().split()
            if len(row) == len(matrix[i]):
                break
            print('Wrong number of values specified. Please try again.')
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def place_towers_init(matrix: list):
    row_sums = {}  # Store calculated sums to improve performance
    col_sums = {}

    taken_fields = set()  # Store information about already taken fields
    taken_rows = set()
    taken_cols = set()

    # A helper function to calculate sums
    def row_col_sum(row_idx, col_idx):
        # Get sum of values in a row
        if row_idx in taken_rows:  # Set row_sum to 0 if the row is already taken
            row_sum = 0
        else:
            if row_idx in row_sums:  # Return cached sum of a row if exists
                row_sum = row_sums[row_idx]
            else:
                row_sum = 0
                for i in range(len(matrix[row_idx])):
                    row_sum += matrix[row_idx][i]
                row_sums[row_idx] = row_sum          # Store calculated sum of all elements in a row
            row_sum -= matrix[row_idx][col_idx]      # Subtract value of the current element from this sum

        # Get sum of values in a column
        if col_idx in taken_cols:  # Set col_sum to 0 if the row is already taken
            col_sum = 0
        else:
            if col_idx in col_sums:  # Return cached sum of a column if exists
                col_sum = col_sums[col_idx]
            else:
                col_sum = 0
                for i in range(len(matrix)):
                    col_sum += matrix[i][col_idx]
                col_sums[col_idx] = col_sum          # Store calculated sum of all elements in a column
            col_sum -= matrix[row_idx][col_idx]  # Subtract value of the current element from this sum

        return row_sum + col_sum

    # Another helper function that subtracts proper values from sums of rows and columns
    def update_row_col_sums(row_idx, col_idx):
        # Subtract a value from taken column by new tower from sums of values in rows
        for i in range(len(matrix)):
            row_sums[i] -= matrix[i][col_idx]
        # Subtract a value from taken row by new tower from sums of values in columns
        for i in range(len(matrix[row_idx])):
            col_sums[i] -= matrix[row_idx][i]

    def place_tower() -> tuple:
        max_sum = 0
        max_sum_row_idx = None
        max_sum_col_idx = None
        for row_idx in range(len(matrix)):
            for col_idx in range(len(matrix[row_idx])):
                if (row_idx, col_idx) in taken_fields:
                    continue
                curr_sum = row_col_sum(row_idx, col_idx)
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_sum_row_idx = row_idx
                    max_sum_col_idx = col_idx

        coordinates = (max_sum_row_idx, max_sum_col_idx)
        if max_sum_row_idx is not None and max_sum_col_idx is not None:
            taken_rows.add(max_sum_row_idx)
            taken_cols.add(max_sum_col_idx)
            taken_fields.add(coordinates)
            update_row_col_sums(max_sum_row_idx, max_sum_col_idx)

        return coordinates

    return place_tower


if __name__ == '__main__':
    towers_count = 2
    n = int(input())
    t = create_matrix(n, n)
    fill_matrix(t)
    place_tower = place_towers_init(t)
    towers_coordinates = [place_tower() for _ in range(towers_count)]
    print(towers_coordinates)


"""
5
123 32 565 33 67
123 214 1 141 34
4134 13 134 17 215
264 75 252 522 324
52351 431 5412 151 31

8
3401 4730 6274 2690 4190 9357 8352 6153 
9591 3065 6173 8377 4954 4763 6560 6909 
5833 6908 4364 7906 3508 3123 1260 6808 
293 6692 1275 1529 9400 5276 9673 4904 
8053 401 5745 7632 2230 8207 3426 3152 
8396 5855 7938 2648 3034 8843 4911 7065 
726 4145 6565 239 7685 2770 6758 1602 
2858 1985 9341 1166 6437 49 8924 3547
"""
