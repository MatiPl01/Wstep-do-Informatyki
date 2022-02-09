"""
Zadanie 11. Dwie liczby naturalne sa „przyjaciółkami jezeli zbiory cyfr z których zbudowane sa liczby
sa identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
naturalnymi. Prosze napisac funkcje, która dla tablicy T zwraca ile elementów tablicy sasiaduje wyłacznie z
przyjaciółkami
"""

from functools import wraps


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


def memoized(fn):
    """A decorator function that is used to cache values returned by the decorated function."""
    cache = {}

    @wraps(fn)
    def inner(val):
        if val not in cache:
            cache[val] = fn(val)
        return cache[val]

    return inner


@memoized
def get_num_digits(num: int) -> set:
    """Returns a set of all number's digits. Every digit is stored at most once."""
    digits = set()
    while num:
        num, digit = divmod(num, 10)
        digits.add(digit)
    return digits


def numbers_have_the_same_digits(numbers: list) -> bool:
    """Checks if all numbers 'numbers' are build up of the same digits. If they do so,
    returns True else returns False."""
    if len(numbers) < 2:  # If we have nothing to compare, return False
        return False
    for i in range(1, len(numbers)):
        if get_num_digits(numbers[i]).symmetric_difference(get_num_digits(numbers[i-1])):
            return False
    return True


def count_numbers_having_friends(matrix: list) -> int:
    """Returns number of numbers that have all neighbours made up of the same digits as the currently
    checked number. As neighbours we concern: numbers lying in the same row that are one index right or
    one index left to the current number, numbers lying in the same column that are one row above or one
    row below current number."""
    friend_numbers_count = 0  # Counts numbers that have all neighbours friends

    def check_neighbours(nums_to_check, row_idx, col_idx):
        # If we are in the first column, do not check numbers on the left side
        if col_idx == 0:
            nums_to_check.append(matrix[row_idx][col_idx+1])
        # If we are in the last column, do not check numbers on the right side
        elif col_idx == len(matrix[row_idx])-1:
            nums_to_check.append(matrix[row_idx][col_idx-1])
        # If we are between the first and the last column, check numbers in the left and on the right side
        else:
            nums_to_check.append(matrix[row_idx][col_idx+1])
            nums_to_check.append(matrix[row_idx][col_idx-1])
        return numbers_have_the_same_digits(nums_to_check)

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):

            nums_to_check = [matrix[row_idx][col_idx]]
            # If we are in the first row, do not check numbers above
            if row_idx == 0:
                nums_to_check.append(matrix[row_idx+1][col_idx])
                found_number = check_neighbours(nums_to_check, row_idx, col_idx)
            # If we are in the last row, do not check numbers below
            elif row_idx == len(matrix)-1:
                nums_to_check.append(matrix[row_idx-1][col_idx])
                found_number = check_neighbours(nums_to_check, row_idx, col_idx)
            # If we are between the first and the last row, check numbers above and below
            else:
                nums_to_check.append(matrix[row_idx+1][col_idx])
                nums_to_check.append(matrix[row_idx-1][col_idx])
                found_number = check_neighbours(nums_to_check, row_idx, col_idx)

            if found_number:
                friend_numbers_count += 1

    return friend_numbers_count


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print('\n', count_numbers_having_friends(t))

'''
12
27 442 672 713 331 739 631 524 370 977 824 513 
672 112 649 234 85 453 80 299 734 349 955 607 
121 212 221 577 844 858 204 188 217 315 749 925 
458 211 330 743 661 725 523 140 290 716 885 315 
932 438 774 950 750 459 491 602 8 221 136 692 
977 114 833 266 853 999 366 515 488 542 362 78 
618 96 360 174 356 374 549 664 805 312 954 288 
688 537 126 544 748 495 945 594 305 41 427 908 
784 922 885 418 232 349 549 92 822 494 166 234 
924 890 43 832 150 303 123 849 355 586 197 613 
356 625 928 992 483 24 733 375 715 671 911 501 
699 218 904 199 123 52 482 514 947 5 939 714

20
42132121 4124212 143 341 2341 21 33 4124214 34322433 414 24 14 41231 314 21344 212241 3332243 141 3121142 414221 
31221 24 23 343 444422 423333 4221432 32444 23 333141 41321 24413213 214 312 123233 33411 23111 334321 3423142 13 
1144123 132 13111 4411 242323 41234 3411 243 42224 2423441 111132 42342 44441221 21 3413 31112 221131 11243232 34322 44 
231423 3342 1423 3334 3234324 22214 334 24414134 34 3124 12432413 4221212 24 12424213 12 32 3442433 314 43433423 41323 
4214 42 12133422 11 341 2244113 4311 41222444 13243 132 11 21 33313444 43343424 2433 4421121 41 2223133 34 2114243 
11323 3421 1223 3142 34224 344443 2234141 31 13 4433111 2144 3314 21234332 322243 1431 4123 2344443 224 2312 443313 
2422334 342143 332332 243313 2211 1313342 22131421 321 2343 221 123 2331244 23422 33414 23 132 32 1223 41 31 
3412 1342 4323311 44 332 331431 311 32331 33342 32114141 21332412 424311 12 24133 22 12423144 12 32134 122112 1112 
34 21332343 14 134 43341321 1241444 1313 11423332 221113 32 31214 113143 1324443 44 334 32234 144131 41 324234 124433 
11 44 24433121 3333 131 132333 1134 314 41123 1444 233 2141 224 343 2324424 21 41314 23423 222 3331 
32 44111 24211 121 21213442 2231322 4242 213411 31 13 13 4122223 34233 2211134 3433 31124321 41 1423424 41213 42 
12 344123 221422 334 341 44 412 22 1424334 423213 411124 2131 413411 13423332 2421324 31432 41224211 41114 1433134 13434441 
33 42 42222 43431 4442 3343 2141434 13 33312 412314 434324 31221 2321341 13 24331241 3333 43211443 4441421 34344232 21241231 
4344444 22321 123412 34124 31444 2412 232432 423442 3334412 31 23232 2234213 331123 13 121 14233413 14 3223214 32112422 14244 
34 13244231 14114 41421 3144214 432 3141 4143 13124 42311 42244 212 31121144 42 34424 42324334 22 43231 34341112 3441 
21 41132114 142414 23 222 423323 32 22 13 3341131 31 44 3433112 34322 413132 442323 11413421 34233 143343 4333314 
314413 43 231 44 142212 4143211 2443121 22144 1123113 12 2341331 342341 442121 3322423 32421 43 3244443 4112 423 21424 
132 332241 3441221 232212 2323423 23324 44124423 33 211212 4421 112133 4213 3131341 11234 33341 3222 44422 231 344141 33 
4442 11132443 324131 231142 4111423 12241341 4141 4244 2443 124 1324321 2123344 431242 4234434 4444 34 3132 24444422 4423213 143212 
231 42112 44412221 4414144 334 22214 41423 33322 244 423332 112 414 12331 42 21334 113444 24443414 114 1234242 2422133

25
2222 21 201 10 1000 1022 22222 2012 2022 12 22 200 2 12 2020 212 1112 222 22 212 112 2010 20 1210 2 
10 20121 212 20101 2100 10 12 2211 11200 10220 1211 12201 12 12200 211 0 200 11 1200 20 2121 10222 12 2 1201 
20100 20 1022 0 11 22010 222 101 222 11 12 2020 1121 10 112 22001 2 111 20011 21 21021 11110 102 20 2000 
12 10 12 22122 22210 112 12002 21 111 1020 22 22022 0 2 22 2 1111 20 1102 2102 22 12010 22 11012 20102 
20120 221 12 0 21 20 11 20 22 0 2 222 12 100 2110 1 10 200 0 2111 110 2202 2002 2012 1021 
10 201 221 100 2 2122 20 0 11 2101 111 1210 20 0 21211 1101 10000 2022 102 11 0 2202 12 22 2 
2111 21 12 20111 1 22 2102 2022 0 1 2002 101 112 22 22211 2000 11 1112 1211 101 1001 1 121 20 111 
222 10 11 1011 12 122 0 110 2001 10 2201 21211 2 21 10011 0 100 22 1221 102 202 202 2 1101 1002 
221 10 11212 210 10 101 11021 11 1020 10 10 102 22 2121 1111 2020 1222 21 22220 110 20112 22201 20 100 0 
11111 220 2 10 0 22 2202 111 1 1 1002 2020 121 110 101 222 222 21 120 0 220 21200 111 0 11210 
10002 2202 212 22 222 1010 12112 121 12 0 100 10 2012 200 1121 12 11 11 20212 11 12 2102 21 20 21 
11 11001 22022 21 1210 2 12 2210 21000 12 221 1012 120 100 222 20 122 22 1222 10221 0 2001 112 11112 22 
2 12211 2211 122 0 2020 220 101 110 22100 10212 10221 102 12 1100 12202 20012 10200 20 1 122 210 0 20101 0 
22111 0 2100 20 210 1002 11 110 100 212 1012 112 10 1012 22 1102 101 1210 211 2121 110 220 2 10 1122 
101 1000 1 12 2120 120 1 1210 102 2120 211 22 12 10 2101 202 11 121 22211 122 1200 222 10 10 21 
20 21 100 20 10 20 20 121 202 11002 22100 1 2010 21 120 10202 211 211 11222 111 20 1220 1211 11221 21121 
11 12102 12 21100 202 22 22202 102 1 1011 21002 210 21 120 120 1122 212 0 21 20 1 1110 2101 122 12222 
10 12 20 11 12 0 2 2001 2 10100 2101 22 1 10111 2211 211 11100 2011 10 22 100 0 21021 211 2211 
1001 21121 12000 1112 22202 1120 100 1 21 11010 1010 202 11212 120 22 1100 101 12101 10011 100 0 10 110 2002 20 
2101 22 11 200 210 2 12 10121 11 21 100 1022 1110 21211 212 101 2112 2122 102 1202 20 22122 1202 122 200 
1202 12 20111 12 10 12111 2222 21211 20 221 2011 102 22120 21 12021 12 120 10112 221 22210 20 102 2012 21221 20121 
222 10 21 21 1 2001 201 120 1200 1121 22202 12 10110 2101 1012 20022 200 1220 2020 2220 0 110 20021 20000 1010 
2 0 120 2201 201 1100 12 1222 20 1112 21 2022 202 22 22 122 1 11 220 20 0 12 22 121 1001 
112 10122 10 12212 101 22 1120 12 12 0 21211 20 200 1 2 1211 20 2220 1 112 112 2 1210 111 2121 
1122 2100 2121 1202 2 122 11 20221 21 2010 12 201 202 122 2022 1 10 11 11110 110 2101 10 22111 202 2
'''
