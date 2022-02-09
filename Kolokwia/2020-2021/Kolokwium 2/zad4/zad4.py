"""
Mateusz Łopaciński

Wewnątrz funkcji divide(N) zadeklarowałem funkcję rekurencyjną o nazwie recur.
Funkcja ta pobiera w postaci argumentów informację o reszcie (rest), czyli pozostałej
części liczby N (do podziału na fragmenty), obecnym fragmencie (zmienna curr_num) oraz
wszystkich dotychczas utworzonych fragmentach dla danego wywołania (zmienna split).
Pomocnicza zmienna mul pozwala na prawidłowe dodawanie kolejnej cyfry na początek
tworzonej liczby curr_num.

Rekurencja zostaje przerwana w momencie, w którym nie została żadna cyfra w początkowej
liczbie do podziału (dołaczenia w postaci fragmentu do krotki podziałów).
Sprawdzony zostaje wtedy warunek, czy wzięliśmy ostatnio utworzony fragment do ciągu
(jeżeli nie, to należy zwrócić wartość False). Kolejny warunek to liczba kawałków będąca
liczbą pierwszą, a następnie sprawdzany jest warunek, czy każdy fragment jest liczbą pierwszą.
Jeżeli powyższe warunki zachodzą, utworzony został prawidłowy ciąg fragmentów przekazanej
funkcji divide liczby i zwracana jest wartość True, przeciwnie - False i rekurencja kontunuuje
sprawdzanie do momentu sprawdzenia wszystkich przypadków lub natrafienia na wartość True.
"""
from math import sqrt


def is_prime(num: int) -> bool:
    if num in {2, 3}:
        return True
    if not num % 2 or not num % 3 or num < 2:
        return False

    for div in range(5, int(sqrt(num))+1, 6):
        if not num % div or not num % (div + 2):
            return False
    return True


def divide(N):

    def recur(rest=N, curr_num=0, split=(), mul=1):
        if not rest:
            # res = not curr_num and is_prime(len(split)) and all(is_prime(num) for num in split)
            # if res:
            #     print(print(split))
            #     return True
            # else:
            #     return False
            return not curr_num and is_prime(len(split)) and all(is_prime(num) for num in split)

        rest, dgt = divmod(rest, 10)
        curr_num += mul * dgt

        return recur(rest, 0, split + (curr_num,), 1)\
            or recur(rest, curr_num, split, mul*10)

    return recur()


if __name__ == '__main__':
    print(divide(273))  # True, podział 2|7|3
    print(divide(22222))  # True, podział 2|2|2|2|2
    print(divide(23672))  # True, podział 23|67|2
    print(divide(2222))  # False
    print(divide(21722))  # False
