"""
Zadanie 18. Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Prosze napisac funkcje, która
wyszuka spójny podciag elementów lezacy poziomo lub pionowo o najwiekszej sumie. Maksymalna długosc
podciagu moze wynosic 10 elementów. Do funkcji nalezy przekazac tablice T, funkcja powinna zwrócic sume
maksymalnego podciagu.
"""
# Brute force solution

from colorama import Fore, Style
import time
import os


def show_colorized_matrix(matrix, start_coords, curr_coords, max_length, curr_sum, max_sum, direction, *, sleep=.2):
    print_val = lambda color, val: print(f'{getattr(Fore, color.upper())}{val}{Style.RESET_ALL}', end=' ')

    # Find greatest-length value
    max_val_length = 0
    for row in matrix:
        for val in row:
            length = len(str(val))
            if length > max_val_length:
                max_val_length = length

    # Print colorized matrix
    os.system('cls')

    print(f'Checked direction: {direction}')
    print(f'Max sum found {max_sum}')
    print(f'Currently found sum {curr_sum}\n')

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            val = str(matrix[row_idx][col_idx]).ljust(max_val_length)
            if (row_idx, col_idx) == curr_coords:
                print_val('red', val)     # Currently added value to the current sum
            elif row_idx == start_coords[0] and start_coords[1] <= col_idx < curr_coords[1] \
                    or col_idx == start_coords[1] and start_coords[0] <= row_idx < curr_coords[0]:
                print_val('green', val)   # Values that have been added to the current sum
            elif direction is 'horizontal' and row_idx == start_coords[0] and curr_coords[1] <= col_idx < start_coords[1] + max_length \
                    or direction is 'vertical' and col_idx == start_coords[1] and curr_coords[0] <= row_idx < start_coords[0] + max_length:
                print_val('yellow', val)  # Values that will be added to the current sum
            else:
                print(val, end=' ')
        print()

    time.sleep(sleep)


def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    """Creates a 2-dimensional list of a specified number of rows and columns"""
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(matrix: list):
    """Fills matrix with values provided by the user"""
    for i in range(len(matrix)):
        while True:
            row = input(f'{i + 1}. row > ').split()
            if len(row) == len(matrix[i]):
                break
            print('Wrong number of values specified. Please try again.')
        for j, val in enumerate(row):
            matrix[i][j] = int(val)


def max_sum_common_subsequence(matrix: list, max_length: int = 10) -> int:
    """Returns sum of the longest consistent substring that has the greatest sum
    and is no longer than 'max_length'"""
    max_sum = 0

    # Search in rows
    for row_idx in range(len(matrix)):
        for i in range(len(matrix[row_idx])):  # Index of the sequence's beginning
            curr_sum = 0
            for j in range(i, min(i + max_length, len(matrix[row_idx]))):  # Currently summed value's index
                curr_sum += matrix[row_idx][j]

                show_colorized_matrix(matrix, (row_idx, i), (row_idx, j), max_length, curr_sum, max_sum, 'horizontal')

                if curr_sum > max_sum:
                    max_sum = curr_sum

    # Search in columns
    for col_idx in range(len(matrix[0])):
        for i in range(len(matrix)):  # Index of the sequence's beginning
            curr_sum = 0
            for j in range(i, min(i + max_length, len(matrix))):  # Currently summed value's index
                curr_sum += matrix[j][col_idx]

                show_colorized_matrix(matrix, (i, col_idx), (j, col_idx), max_length, curr_sum, max_sum, 'vertical')

                if curr_sum > max_sum:
                    max_sum = curr_sum

    return max_sum


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(max_sum_common_subsequence(t))


'''
5
-591 -415 858 806 500 
-104 717 -726 -702 -546 
642 -392 264 746 -546 
-591 -282 353 -480 -156 
37 -574 -674 -686 610

8
-5283 4717 7128 -4117 -401 5827 -9437 5368 
-3824 -2381 4837 8793 -5461 -5692 9764 -9160 
4004 -8741 9510 -2244 1594 -2382 -5237 -1078 
3406 4958 6494 7099 -9512 -1951 4502 6235 
-3490 -5090 -9158 -1173 3700 -4941 1433 -7068 
7357 7895 3419 5380 7849 -4828 -4154 6317 
5614 3700 7264 2072 -6661 -9268 -6601 -3824 
5852 9998 -4008 -717 -5655 -979 1733 -2917

20
-2172 -1736 3168 -3203 -762 -6351 1632 9252 -263 7143 6917 6100 717 -4558 7550 8111 -7634 -5042 9562 -2243 
-4735 -903 4898 5455 -4039 -3463 -1183 -4023 -8710 4810 -8920 -8053 5152 8112 -6737 -7052 4192 -1153 4099 -5286 
-804 3253 -3630 -7462 -23 4629 -9804 8048 1886 -4460 6690 -9185 4644 -4040 -3910 7117 -3531 7973 7007 4659 
-5901 -5995 885 -6350 2032 -9227 -4532 8219 180 -3792 -8344 8957 -3994 9183 9684 -569 5408 7543 -4160 9160 
-7668 -4410 7782 -5840 -249 -7596 -5610 -6517 -7096 -7795 -1514 -787 -9867 1678 5115 -817 9555 -6099 -546 7932 
-9476 8602 -4281 -1076 -2709 -1082 3904 4565 -2295 3656 -878 -6873 1880 -9701 9071 -1083 -3772 2164 -8005 -3834 
1830 -5264 -9805 6958 7470 7431 7612 -4519 9786 6264 834 -501 1506 1221 -4393 4834 4233 -7580 -9106 2583 
5690 -9923 2487 7639 3000 -6763 3706 -238 -753 9941 -6822 1139 -694 454 4188 -9503 6663 -8335 -3924 8259 
-3273 -6411 8103 9450 -4552 -7853 3079 -4334 8215 9251 -7378 4840 7031 7100 -8085 -821 -8520 -5908 7904 -552 
-9746 -2695 -892 2010 1024 2991 -6111 1577 -8828 -6462 8083 7785 749 -2876 -2250 9233 3486 458 7472 1849 
-8058 -3689 -838 8413 5219 9392 -726 -6580 -6479 5198 -2717 7160 339 -4208 -7156 8296 2772 7511 -7891 4854 
-8532 4797 4242 -2451 -9383 2503 630 -7007 1776 -5703 3825 3721 -7747 4272 5914 3877 1597 5514 -9340 621 
-1250 -2575 4813 5253 -399 9847 8141 -9990 8248 -3823 5805 4373 7949 -4084 -6714 1179 8520 6450 -5065 4636 
5408 -7470 -1585 -9468 6815 2287 -376 9035 -1512 -6004 -4935 9200 -7942 -4491 -8980 3176 8410 5865 -745 7826 
7621 5064 -4981 336 -1116 -3069 8163 8989 -4541 -6043 7567 3531 -7502 -8370 7932 647 7874 299 -5545 6002 
-9284 5795 -7675 -4192 4423 5991 2985 -8175 -4048 -1713 522 -9342 9234 7429 -7377 -3156 -6543 -1957 -9715 6412 
1056 2487 3584 -3900 -2944 3778 9826 -8802 -327 3159 -5076 -6814 962 2059 3556 1958 3980 5076 6964 -8638 
-7645 -8417 -4622 3130 -8565 5210 9179 -7210 4903 -5255 7138 -3729 3133 8277 527 2995 -9501 3326 -9605 -725 
-304 -9313 6661 3209 7348 -9348 -9329 1227 -6547 -6886 -3819 -3158 -6332 -5812 3894 1812 -6750 -582 -6996 949 
2619 -6522 -5914 49 9047 6488 4370 2479 -8110 -1267 4053 1124 -5116 -4220 2501 -5918 -9863 7794 6805 -6214
'''
