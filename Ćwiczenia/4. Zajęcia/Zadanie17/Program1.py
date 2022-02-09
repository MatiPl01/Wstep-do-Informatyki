"""
Zadanie 17. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje która
zwraca wiersz i kolumne dowolnego elementu, dla którego suma otaczajacych go elementów jest najwieksza.
"""

def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    """Creates a 2-dimensional list of specified number of rows and columns."""
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    """Fills matrix with values provided by the user."""
    for i in range(len(matrix)):
        while True:
            row = input(f'{i + 1}. row > ').split()
            if len(row) == len(matrix[i]):
                break
            print('Wrong number of values specified. Please try again.')
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def number_surrounded_by_values_of_greatest_sum_coordinates(matrix: list) -> (int, int):
    """Returns coordinates of the number that is surrounded by the values summing up
    to the greatest possible value."""
    max_sum = 0
    max_sum_coordinates = (0, 0)

    for num_row_idx in range(1, len(matrix)-1):
        for num_col_idx in range(1, len(matrix[num_row_idx])-1):
            curr_sum = 0
            for row_idx in range(num_row_idx-1, num_row_idx+2):
                for col_idx in range(num_col_idx-1, num_col_idx+2):
                    if (row_idx, col_idx) != (num_row_idx, num_col_idx):
                        curr_sum += matrix[row_idx][col_idx]
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_sum_coordinates = (num_row_idx, num_col_idx)

    return max_sum_coordinates


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(number_surrounded_by_values_of_greatest_sum_coordinates(t))

'''
10
893 974 647 587 661 785 46 319 191 922 
876 518 430 650 424 739 639 745 534 280 
101 615 400 374 250 873 315 191 939 111 
981 678 973 322 292 254 453 837 395 963 
944 439 510 940 65 806 494 596 553 542 
597 219 454 887 942 530 652 477 764 784 
481 700 6 698 213 668 978 601 661 500 
560 760 869 695 376 573 791 426 834 563 
104 805 194 14 916 624 432 390 266 988 
559 653 595 891 950 231 773 449 334 194
'''
