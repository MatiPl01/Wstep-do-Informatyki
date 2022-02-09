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


def is_multiple_of_natural_number_square(num: int) -> bool:
    n = 2

    while True:
        n_sq = n**2
        mul = 2

        if mul * n_sq > num:
            return False

        while mul * n_sq <= num:
            if mul * n_sq == num:
                return True
            mul += 1
        n += 1


def get_converted_matrix(matrix: list) -> list:
    new_matrix = []
    for row_idx in range(len(matrix)):
        row = []
        for col_idx in range(len(matrix[row_idx])):
            row.append(is_multiple_of_natural_number_square(matrix[row_idx][col_idx]))
        new_matrix.append(row)
    return new_matrix


def all_values_are_True(matrix: list, skipped_rows: 'iterable', skipped_columns: 'iterable') -> bool:
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            if row_idx in skipped_rows or col_idx in skipped_columns:
                continue
            if not matrix[row_idx][col_idx]:  # If at least one value is False, return False
                return False
    return True  # Else, return True


def check_condition(matrix: list) -> bool:
    if len(matrix) == 1 or len(matrix[0]) <= 2:
        return False

    converted_matrix = get_converted_matrix(matrix)

    for row_idx in range(len(matrix)):
        for col_1_idx in range(len(matrix[row_idx])):
            for col_2_idx in range(col_1_idx+1, len(matrix[row_idx])):

                if all_values_are_True(converted_matrix, {row_idx}, {col_1_idx, col_2_idx}):
                    print(row_idx, col_1_idx, col_2_idx)
                    return True
    return False


if __name__ == '__main__':
    N = int(input('(N) > '))
    t = create_matrix(N, N)
    fill_matrix(t)
    print(check_condition(t))


'''
10
576 25600 3125 1728 3362 17424 10580 200 11560 36784
15376 1458 19208 12544 2023 32256 2160 1573 5808 486
980 98 16731 7200 288 5103 8664 3364 12493 864
3132 17408 3267 126 17150 43143 5547 1587 44 2500
2116 2738 2448 507 7935 12288 21904 4800 2736 2400
11616 2304 4275 23321 12348 2160 441 23534 50 847
8640 162 12493 12696 1152 6615 37553 6936 12321 8214
31 81 1694 36 405 5887 34143 36784 2500 3584
2646 98 3757 11700 3610 117 8379 1440 3584 11560
1024 3249 12168 5400 40 6137 540 16807 1008 27378

20
5733 1008 18496 11520 1600 2304 75 2601 9216 13454 4864 2890 10580 18491 6300 17797 845 18491 1587 7350
10816 1445 7744 7396 4608 18252 3332 32256 34560 6250 1600 63 1445 1936 224 13824 2800 12150 5600 2475
3844 960 52 41472 8214 192 431341 980 24 15360 8712 7260 8092 28224 4410 27 6144 4212 3136 8228
1152 3375 160 36015 3600 19440 1800 4050 8748 2592 8820 4050 1936 18 13254 112 15876 12960 360 20535
11664 26896 17600 6776 486 8100 8836 27648 40817 1377 15876 3072 28899 29584 7744 324 25344 2704 2023 972
350 9792 1734 810 26325 1296 7488 4056 2548 325 6300 5046 35131 320 13552 1922 1216 5476 1690 1352
5819 3200 6727 24000 891 1250 3456 1200 6727 27 3380 540 17408 38416 192 20535 5120 171 23534 4608
600 8100 225 5547 216 24299 1152 810 21296 52 147 31939 338 90 12005 8064 23275 19440 2888 931
1900 2800 968 12250 1083 2700 726 36784 1440 543 19773 234 3150 10192 19200 324 14400 29584 654 3042
350 2016 8748 11520 6480 1296 19200 15876 20808 2028 425 5476 1024 16337 6936 24000 5184 1575 4802 10206
23276 6137 56 288 2736 9000 22815 48 7497 8750 14896 2352 8788 216 39168 338 288 2940 2048 1815
324 3332 9477 40204 5400 7396 6498 5760 7744 31939 5600 17328 216 5103 14406 20250 8000 2888 13500 234
15059 16428 144 26011 972 12615 10140 2156 2304 304 2645 4050 5046 29040 2000 7260 1440 4050 12348 900
1331 6536 15463 1083 5625 9800 13122 7436 38088 22815 567 507 11664 28577 1620 24548 23275 11767 3825 8624
4000 25857 16810 2025 12996 3920 15925 1872 11250 4375 7436 16184 2700 18225 68 17328 1152 7600 1125 363
17672 45 5491 5625 7938 9248 7200 845 108 4800 5054 12716 7569 18772 4864 12960 16641 19166 6400 3825
4050 635 24696 13872 25886 3174 304 6936 17424 2187 108 35131 6084 3388 10240 5760 2028 17424 1134 13068
4335 60 39762 1500 15360 384 16200 2160 16184 180 15138 7840 20736 475 24336 6498 10935 8748 20216 15028
475 18 2592 272 13122 2700 3042 425 4375 14157 400 4096 28 13475 4096 1014 4693 432 4608 9216
15246 5600 96 12150 1014 3468 28812 3179 3564 26508 26896 9900 12288 1083 13475 27200 2916 4400 9216 3528
'''
