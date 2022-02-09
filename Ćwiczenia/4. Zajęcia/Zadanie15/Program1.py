"""
Zadanie 15. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym kazda liczba zawiera co najmniej jedna cyfre
bedaca liczba pierwsza?
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


def get_num_digits(num: int) -> set:
    """Returns digits of the number."""
    digits = set()

    while num:
        num, digit = divmod(num, 10)
        digits.add(digit)

    return digits


def have_prime_digit_init() -> "'have_prime_digit' function":
    """Returns 'have_prime_digit' function."""
    prime_digits = {2, 3, 5, 7}

    def have_prime_digit(num: int) -> bool:
        """Checks if the number 'num' has at least one prime digit."""

        for digit in get_num_digits(num):
            if digit in prime_digits:
                return True
        return False

    return have_prime_digit


have_prime_digit = have_prime_digit_init()


def all_nums_have_prime_digit_in_row(matrix: 'a 2-dimensional list') -> bool:
    """Returns True if found a row in the matrix passed in which all of the numbers
    lying in this row have at least one prime digit."""
    for row in matrix:
        for val in row:
            if not have_prime_digit(val):  # If found one value that has no prime digit, move on to the next row
                break
        else:
            return True  # If loop above was finished without breaking the loop, that means we found the searched row
    return False  # If no matching row was found in the whole matrix, return False


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(all_nums_have_prime_digit_in_row(t))

'''
3
89 31 33 
25 6 82 
59 34 24

10
540 292 860 255 374 19 68 913 356 918 
871 720 987 738 498 497 969 212 59 604 
567 382 971 352 514 985 10 173 864 447 
66 636 682 250 585 560 973 463 14 272 
306 770 285 161 611 653 288 191 546 141 
310 182 186 145 987 301 387 792 233 426 
253 997 324 393 714 607 829 786 868 298 
808 169 688 786 933 286 142 690 653 989 
239 571 703 726 618 668 277 335 188 982 
210 979 527 317 611 794 905 791 401 705

10
595 650 892 812 303 573 234 30 280 486 
765 899 788 653 986 623 62 741 23 867 
66 886 802 163 888 719 148 57 848 989 
644 158 610 265 982 101 314 784 362 891 
156 812 150 363 712 130 633 843 566 30 
383 827 640 371 50 616 905 627 813 877 
669 207 483 45 35 54 478 707 939 626 
501 713 515 283 678 327 232 894 623 555 
199 435 881 744 661 206 188 472 542 967 
756 711 779 614 509 939 238 342 703 463
'''
