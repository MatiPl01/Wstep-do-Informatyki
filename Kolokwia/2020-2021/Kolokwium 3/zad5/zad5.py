"""
Mateusz Łopaciński

Przy pomocy funkcji trojki sprawdzam, czy istnieją trójki takie, że ich największy wspólny dzielnik
to 1 oraz odległość między dwoma kolejnymi elementami trójki jest równa 0 (są koło siebie) lub 1
(jest 1 element w tablicy T pomiędzy).
W Pętli sprawdzam wszystkie możliwości i zwracam wynik (liczbę trójek dla danej tablicy).
"""


def calc_gcd(a, b):
    return a if not b else calc_gcd(b, a % b)


def gcd(a, b):
    return calc_gcd(abs(a), abs(b))


def gcd_many_values(*nums):
    if len(nums) < 2:
        raise ValueError(f'Expected at least 2 values, got {len(nums)}')

    res = nums[0]
    i = 1
    while i < len(nums) and res != 1:
        res = gcd(res, nums[i])
        i += 1
    return res


def trojki(T):
    count = 0

    for i in range(len(T)-2):
        if gcd_many_values(T[i], T[i+1], T[i+2]) == 1:
            count += 1
    for i in range(len(T)-3):
        if gcd_many_values(T[i], T[i+1], T[i+3]) == 1:
            count += 1
        if gcd_many_values(T[i], T[i+2], T[i+3]) == 1:
            count += 1
    for i in range(len(T)-4):
        if gcd_many_values(T[i], T[i+2], T[i+4]) == 1:
            count += 1

    return count


if __name__ == '__main__':
    print(trojki([2, 4, 6, 7, 8, 10, 12]))  # 0 trójek
    print(trojki([2, 3, 4, 6, 7, 8, 10]))  # 1 trójka (3,4,7)
    print(trojki([2, 4, 3, 6, 5]))  # 2 trójki (2,3,5),(4,3,5)
    print(trojki([2, 3, 4, 5, 6, 8, 7]))  # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
