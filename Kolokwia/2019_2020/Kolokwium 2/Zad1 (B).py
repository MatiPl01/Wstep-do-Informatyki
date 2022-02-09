from math import ceil


def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    for i in range(len(matrix)):
        while True:
            row = input(f'{i + 1}. row > ').split()
            if len(row) == len(matrix[i]):
                break
            print('Wrong number of values specified. Please try again.')
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def count_base_7_even_digits(num: int) -> int:
    count = 0
    while num:
        num, digit = divmod(num, 7)
        count += not digit % 2
    return count


def convert_matrix(matrix: list) -> list:
    return [[count_base_7_even_digits(n) for n in row] for row in matrix]


def check_condition(matrix1: list, matrix2: list, min_percent=100) -> bool:
    if len(matrix1) > len(matrix2) or len(matrix1[0]) > len(matrix2[0]) or not 0 < min_percent <= 100:
        return False

    m1_conv = convert_matrix(matrix1)
    m2_conv = convert_matrix(matrix2)
    searched_count = ceil(min_percent/100 * len(matrix1) * len(matrix1[0]))

    for start_row_idx in range(len(matrix2)-len(matrix1)+1):
        for start_col_idx in range(len(matrix2[0])-len(matrix1[0])+1):

            count = 0
            # Check values in both matrices
            for row_idx in range(len(matrix1)):
                for col_idx in range(len(matrix1[row_idx])):

                    if m1_conv[row_idx][col_idx] == m2_conv[row_idx][col_idx]:
                        count += 1
                        if count >= searched_count:
                            return True
    return False


if __name__ == '__main__':
    MAX1 = int(input('(MAX1) > '))
    tab1 = create_matrix(MAX1, MAX1)
    fill_matrix(tab1)
    MAX2 = int(input('(MAX2) > '))
    tab2 = create_matrix(MAX2, MAX2)
    fill_matrix(tab2)
    print(check_condition(tab1, tab2, 33))

'''
4
233 8 223 41 
154 346 301 59 
404 338 458 209 
18 215 153 379
10 
901 309 593 633 710 178 834 874 51 901 
762 505 310 538 960 226 971 897 844 920
620 757 986 576 956 341 24 329 228 823 
472 938 777 806 336 296 761 148 268 151
131 186 77 630 527 599 199 680 771 428 
414 252 88 810 771 449 202 617 442 827 
156 640 361 517 372 951 348 606 135 201 
517 192 607 19 722 982 987 181 603 554 
208 135 973 385 338 351 214 261 121 2 
422 63 241 857 419 740 920 370 931 239 

3
10901 92070 90919
60373 67311 33559
29113 99748 65613
8
10901 92070 90919 22546 9721 80154 1353 87467 
60373 67311 33559 74858 50059 66532 55253 68755
29113 99748 65613 83931 15616 86126 10789 33651
31592 6869 12510 51768 15318 34451 51465 11135
73406 7674 89739 6022 82602 64656 56 49356
35484 71882 25218 53688 87649 61314 99231 46965
48341 14420 3430 96551 43362 18809 99200 91453
68350 98223 60320 3863 47769 23372 92398 61357
'''
