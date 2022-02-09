"""
Zadanie 16. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Prosze napisac funkcje która
odpowiada na pytanie, czy w tablicy kazdy wiersz zawiera co najmniej jedna liczba złozona wyłacznie z cyfr
bedacych liczbami pierwszymi?
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


def all_digits_are_primes_init() -> "'all_digits_are_primes' function":
    """Returns 'all_digits_are_primes' function."""
    prime_digits = {2, 3, 5, 7}

    def all_digits_are_primes(num: int) -> bool:
        """Checks if the number 'num' has at least one prime digit."""

        for digit in get_num_digits(num):
            if digit not in prime_digits:
                return False
        return True

    return all_digits_are_primes


all_digits_are_primes = all_digits_are_primes_init()


def number_having_all_prime_digits_in_every_row(matrix: 'a 2-dimensional list') -> bool:
    """Returns True if found a number that is made up of all prime digits in every row
    of the matrix."""
    for row in matrix:
        for val in row:
            if all_digits_are_primes(val):  # Move on to the next row if a matching number was found
                break
        else:
            return False  # Return False if no matching value was found in teh row, therefore, loop hasn't been broken
    return True  # Return True if all rows had at least one number that is made up of prime digits


if __name__ == '__main__':
    n = int(input('(n) > '))
    t = create_matrix(n, n)
    fill_matrix(t)
    print(number_having_all_prime_digits_in_every_row(t))

'''
3
89 31 33 
25 6 82 
59 34 24

10
783 633 25 399 549 159 691 172 526 961 
681 819 533 936 885 927 4 412 274 727 
644 478 431 928 930 941 452 866 232 407 
984 575 413 457 816 716 209 799 462 490 
723 564 45 856 759 109 753 555 243 825 
131 638 602 158 876 865 989 338 175 735 
940 647 594 57 653 974 160 603 924 356 
373 704 736 487 199 680 668 591 904 963 
127 253 768 449 285 991 922 249 648 154 
540 332 61 230 685 887 850 929 812 956
'''
