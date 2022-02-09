"""
Zadanie 20. Dana jest tablica T[N][N] (reprezentujaca szachownice) wypełniona liczbami naturalnymi.
Prosze napisac funkcje która ustawia na szachownicy dwie wieze, tak aby suma liczb na „szachowanych”
przez wieze polach była najwieksza. Do funkcji nalezy przekazac tablice, funkcja powinna zwrócic połozenie
wiez. Uwaga - zakładamy, ze wieza szachuje cały wiersz i kolumne z wyłaczeniem pola na którym stoi.
"""

from colorama import Fore, Style
import time
import os


def print_colorized_matrix(
        matrix: list,
        checked_field: '2-element iterable representing coordinates of a checked field',
        taken_fields: 'iterable of coordinates (2-element iterables)' = set(),
        sleep: 'refresh interval' = .3):
    """Shows colorized output (a row and a column currently checked and rows and columns
    that are already taken"""

    print_val = lambda color, value: print(f'{getattr(Fore, color.upper())}{value}{Style.RESET_ALL}', end=' ')

    # Find number of greatest number of digits
    max_val_length = len(str(matrix[0][0]))
    for row in matrix:
        for val in row:
            val = str(val)
            if len(val) > max_val_length:
                max_val_length = len(val)

    # Create sets of taken rows and columns
    taken_rows = set()
    taken_columns = set()
    for row_idx, col_idx in taken_fields:
        taken_rows.add(row_idx)
        taken_columns.add(col_idx)

    # Print colorized matrix
    os.system('cls')
    checked_row, checked_column = checked_field
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            val = str(matrix[row_idx][col_idx]).ljust(max_val_length)
            if row_idx == checked_row and col_idx == checked_column:   # Currently checked field
                print_val('green', val)
            elif (row_idx, col_idx) in taken_fields:                   # Field on which a tower is placed
                print_val('red', val)
            elif row_idx in taken_rows or col_idx in taken_columns:    # A row or a column on which can tower move
                print_val('yellow', val)
            elif row_idx == checked_row or col_idx == checked_column:  # Row or column of the currently checked field
                print_val('blue', val)
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


def place_towers_init(matrix: list) -> "'place_towers' function":
    """"Returns function that places towers on the matrix represented by a board on the fields
        for which a sum of values in a column and values in a row (excluding a field on which
        a tower is being placed) is the greatest."""
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
        """Returns coordinates of a tower placed on the matrix board"""
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

                # print_colorized_matrix(matrix, (row_idx, col_idx), taken_fields, sleep=.1)

        coordinates = (max_sum_row_idx, max_sum_col_idx)
        if max_sum_row_idx is not None and max_sum_col_idx is not None:
            taken_rows.add(max_sum_row_idx)
            taken_cols.add(max_sum_col_idx)
            taken_fields.add(coordinates)
            update_row_col_sums(max_sum_row_idx, max_sum_col_idx)

        print_colorized_matrix(matrix, (-1, -1), taken_fields, sleep=.5)

        return coordinates

    return place_tower


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    place_tower = place_towers_init(t)
    towers_coordinates = [place_tower() for _ in range(4)]
    print(towers_coordinates)

'''
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

15
483 969 615 910 601 268 973 222 220 113 429 62 175 519 2 
205 701 367 597 187 730 74 685 597 77 998 395 902 35 731 
631 347 763 583 273 16 815 715 704 136 962 762 650 224 505 
367 699 670 811 584 40 682 409 707 336 73 370 639 37 976 
914 308 490 225 805 163 227 825 224 20 177 903 303 763 773 
687 803 116 734 346 399 11 639 556 110 927 62 911 145 884 
668 175 273 545 681 778 111 452 938 573 719 203 824 742 38 
381 333 847 985 157 311 954 756 428 567 967 288 712 836 933 
369 303 651 835 996 88 18 591 80 137 290 281 47 505 911 
221 416 367 975 628 435 405 568 430 258 991 318 348 562 188 
4 918 258 834 320 61 414 304 495 550 385 611 913 261 20 
812 548 349 929 955 763 522 602 563 179 871 534 960 818 657 
780 225 792 924 670 392 716 384 620 885 569 824 164 647 647 
298 262 435 837 185 605 174 905 927 299 456 847 998 118 714 
701 275 937 614 508 548 945 261 621 482 325 184 193 55 151

30
1803 849 5167 1415 9030 3618 9564 3674 5599 9816 1727 7025 2878 1016 4205 5183 9700 1482 7458 9705 6555 1545 2978 1736 1594 4420 9239 8944 1176 8166 
3861 4388 5171 5802 7043 440 1858 6718 1708 5103 5940 7771 5373 6173 9134 9190 4274 6985 8674 5728 1095 3315 8835 1772 8959 2109 6865 9468 8702 8800 
7088 4544 6375 5842 6510 7883 6694 6383 3499 7363 2384 5306 9184 8885 4989 4337 4387 1617 3691 5479 7029 4973 5106 1408 4640 8441 7026 9508 491 1384 
1373 8047 7099 7185 1894 142 2073 4771 911 5115 8057 1780 7488 3552 355 7332 1684 5854 5082 4914 6412 6415 9471 9409 8726 8305 8196 1251 5401 3831 
136 3527 9415 1826 8433 7370 5965 588 5891 5328 3175 1109 2885 1387 8695 8459 5795 6721 6878 1262 4099 3080 9403 2863 2454 9790 7235 3079 7576 8958 
4582 6572 9526 8920 5221 5911 9248 7642 4100 4009 6784 6949 48 6808 9361 5682 8338 8222 3037 3525 6465 2758 5047 5053 1985 2069 3985 2392 6404 1415 
7512 7424 7504 8091 7871 2236 3866 7041 5499 8741 7917 5706 5186 4526 8086 6415 2683 3384 8502 2284 4988 7703 8864 8917 2541 9276 7799 9846 9412 8800 
4168 9935 6412 2690 7376 4158 5222 6650 6565 5040 4769 9117 7243 5038 2093 2278 7095 7136 7409 5246 1575 2571 6141 8767 21 6724 7928 1794 798 3524 
7846 2010 6478 6269 7611 8941 3481 1666 4065 7996 6718 2521 5566 1345 5403 4889 7508 7401 6771 2873 9271 4754 5393 4266 3715 8351 586 8173 116 9288 
9521 6343 4324 3984 2549 7491 175 285 182 6564 5821 5558 2167 397 5045 549 2459 6255 5054 5244 2441 2136 1301 7484 39 8779 8810 6161 8694 5790 
3799 3269 6438 8878 9166 7131 372 5019 6172 4989 6044 9724 5974 2759 5367 649 1675 3458 6606 2639 7280 7974 789 5520 4163 2282 6041 1396 5249 3622 
5973 258 9206 5911 7044 7252 8005 9238 4458 6872 677 766 1391 2543 1331 4846 2834 4818 940 5823 5880 8112 9492 3607 7276 233 1673 7586 9928 850 
390 7787 5864 4601 152 6555 6841 4446 5417 2546 7772 2675 548 3525 7361 5965 2163 6513 1404 5026 6189 5344 6480 2857 899 1120 7008 1260 944 3128 
531 3329 889 9742 7844 4862 4954 7380 251 2062 8190 410 6765 3890 9320 9546 4261 5942 106 21 7890 1236 8197 6724 4403 5649 3798 8370 5042 9430 
473 4000 3746 9087 2573 3119 7797 4370 9949 3792 6317 2244 6367 7065 9197 7275 2682 1181 5559 7952 4043 9692 9734 501 5074 9472 3342 307 924 6629 
7872 2141 8804 7709 19 6166 3149 9026 2019 3651 9393 5142 6077 9381 4607 6951 1053 5696 8326 7773 4168 7712 9713 7162 3803 6932 1550 241 5142 1426 
8707 8963 3705 5203 2474 9977 6820 8854 7387 9762 9505 433 6108 9247 3077 8955 509 6522 920 9211 8063 9296 6454 2767 9751 6479 2304 8972 6859 7943 
818 6317 7114 7123 2378 6278 4657 1361 5202 5495 3978 3029 8237 2520 4377 6771 4302 6291 4091 6650 3383 5544 7962 6770 159 8329 9830 850 5650 416 
9452 3159 1268 6355 769 2070 382 1708 3418 4040 1260 6120 5583 386 9987 4609 960 9705 5618 4823 3267 4120 991 1521 1713 4884 7867 9270 7960 4587 
8669 569 4904 3292 6460 3796 8225 481 5106 4404 2653 1759 4678 9997 1876 1983 6033 9469 7604 2069 8188 503 7020 1628 6631 7811 5715 9046 5430 8875 
3437 3641 7508 7686 9135 9532 7812 1616 7559 3317 6008 9026 9126 6373 7375 1511 2092 8009 9574 1388 4582 2300 5669 8327 9891 6045 8 661 1314 9606 
5472 99 178 216 8105 5523 8157 8293 2571 3009 9195 659 1100 4974 3493 6910 8915 2606 1503 5089 4863 7159 6781 3610 1129 5501 4168 3155 1663 9617 
3774 9086 405 2470 7118 2348 4242 8857 3564 7421 5118 2041 7217 592 2298 839 938 6065 3928 9796 6590 352 2751 4624 8509 4324 1104 9657 5734 2885 
593 3147 2129 144 9840 3795 5956 5802 792 7541 2896 8493 8047 6374 3434 2915 1979 3320 6966 6222 4624 370 1079 2347 9609 3732 2224 5309 1142 2531 
6894 1839 4735 1550 845 9248 6725 6088 1791 947 7004 54 3559 8702 4163 2606 4036 1458 8840 565 9450 1716 8924 2520 5347 4581 4867 1164 8475 6099 
5440 3076 39 3376 963 6018 8745 8883 9435 5956 1138 4162 3676 612 4211 9561 4677 4375 4502 8599 6711 3656 3226 3549 2112 6262 9458 245 3329 2730 
4396 7930 1026 3528 4527 5390 4721 8933 8442 9527 1617 9387 2322 1146 2837 2255 5278 5516 4605 8376 6243 8202 7301 2263 9324 9371 4542 6098 1730 6272 
7904 8951 9735 5364 5196 1302 4331 9246 4313 7083 2055 8759 5652 520 4226 4826 4699 8272 2082 9283 5606 5094 6622 6174 9329 4336 759 6447 2136 4213 
4470 9977 1472 1515 105 324 1195 6594 3027 6405 5300 2137 3312 4331 7349 8207 1925 3663 3276 6837 4188 8006 2404 5968 8635 1210 7240 2003 8402 1278 
4524 1769 8867 2202 7402 65 727 3756 2995 4425 8332 9233 2980 5258 8570 6113 1445 8819 4126 7299 2950 2680 380 2686 3936 8787 4376 6814 9542 3608 
'''
