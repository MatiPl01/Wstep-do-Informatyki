"""
Mateusz Łopaciński

Przy pomocy funkcji 'create_matrix' oraz 'fill_matrix' umożliwiam utworzenie tablicy
o wskazanych wymiarach oraz odpowiednio przekazywanych wartościach. Przykładowy input
zamieszczam na końciu programu.

Funkcja 'bin_list_to_decimal' przeprowadza iterację przez przekazaną tablicę 1-wymiarową,
konwertując reprezentowaną liczbę w systemie binarnym na system dziesiętny.

Funkcja 'distance' służy do wyznaczenia odległości między wierszem, w którym znajduje się
największa w systemie dziesiętnym liczba oraz tym, który zawiera liczbę najmniejszą. W ten
sposób uzyskujemy największą różnicę liczb.
W pętli konwertuję kolejne wiersze na system dziesiętny i sprawdzam, czy otrzymaliśmy liczbę
większą od wcześniejszej największej lub mniejszą od poprzedniej najmniejszej, aktualizując
wartości odpowiednich zmiennych, jeżeli warunki są spełnione.
Na koniec zwracam moduł (ponieważ odległość jest zawsze nieujemna) z różnicy indeksów wierszy,
dla których spełniony jest warunek największej różnicy liczb.
"""


def create_matrix(rows: int, columns: int, *, fill_with=0) -> '2-dimensional list':
    return [[fill_with]*columns for _ in range(rows)]


def fill_matrix(T: list):
    for i in range(len(T)):
        while True:
            row = input().split()
            if len(row) == len(T[i]):
                break
            print(f'Wrong number of values passed. Expected {len(T[i])}, got {len(row)}.')
            print('Please provide valid values count once again for the same row.')
        for j, val in enumerate(row):
            T[i][j] = int(val)


def bin_list_to_decimal(lst: list) -> int:
    pow_2 = 1
    decimal_num = 0
    for i in range(len(lst)-1, -1, -1):
        decimal_num += lst[i] * pow_2
        pow_2 *= 2
    return decimal_num


def distance(T):
    max_row_decimal = min_row_decimal = bin_list_to_decimal(T[0])
    max_row_idx = min_row_idx = 0

    for row_idx in range(1, len(T)):
        row_decimal = bin_list_to_decimal(T[row_idx])

        if row_decimal > max_row_decimal:
            max_row_decimal = row_decimal
            max_row_idx = row_idx
        elif row_decimal < min_row_decimal:
            min_row_decimal = row_decimal
            min_row_idx = row_idx

    return abs(max_row_idx - min_row_idx)


if __name__ == '__main__':
    N = int(input())
    T = create_matrix(N, N)
    fill_matrix(T)
    print(distance(T))


''' Example:
To copy and paste:
10
1 0 0 0 0 0 0 1 0 0
1 1 1 1 1 0 1 0 0 1 
0 1 0 1 1 0 0 0 0 1
0 0 0 1 1 0 0 1 1 1
1 1 1 1 0 1 0 0 0 0
0 0 0 1 1 1 0 1 1 1
1 1 0 1 0 1 0 0 0 0
1 0 1 1 1 0 0 0 1 0
1 1 0 1 0 1 1 1 0 1 
1 1 1 0 0 0 0 1 0 0

To decimal conversion:
1 0 0 0 0 0 0 1 0 0 -> 516
1 1 1 1 1 0 1 0 0 1 -> 1001 <- greatest number
0 1 0 1 1 0 0 0 0 1 -> 353
0 0 0 1 1 0 0 1 1 1 -> 103  <- lowest number
1 1 1 1 0 1 0 0 0 0 -> 976
0 0 0 1 1 1 0 1 1 1 -> 119
1 1 0 1 0 1 0 0 0 0 -> 848
1 0 1 1 1 0 0 0 1 0 -> 738
1 1 0 1 0 1 1 1 0 1 -> 861
1 1 1 0 0 0 0 1 0 0 -> 900
'''
