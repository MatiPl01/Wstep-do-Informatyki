"""
Zadanie 16. Wyrazy budowane sa z liter a..z. Dwa wyrazy ”waza” tyle samo jezeli: maja te sama liczbe samogłosek
oraz sumy kodów ascii liter z których sa zbudowane sa identyczne, na przykład "ula" ! 117, 108, 97
oraz "exe" ! 101, 120, 101. Prosze napisac funkcje wyraz(s1,s2), która sprawdza czy jest mozliwe zbudowanie
wyrazu z podzbioru liter zawartych w s2 wazacego tyle co wyraz s1. Dodatkowo funkcja powinna wypisac
znaleziony wyraz.
"""


def count_vowels_init() -> "'count_vowels' function":
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    def count_vowels(seq) -> int:
        count = 0
        for char in seq:
            if char in vowels:
                count += 1
        return count

    return count_vowels


def ascii_sum(seq) -> int:
    sum_ = 0
    for char in seq:
        sum_ += ord(char)
    return sum_


def have_equal_weight(seq1, seq2) -> bool:
    return count_vowels(seq1) == count_vowels(seq2) and ascii_sum(seq1) == ascii_sum(seq2)


def wyraz(s1, s2):

    def recur(idx=0, letters=''):
        if idx == len(s2):
            found_set = have_equal_weight(s1, letters)
            if found_set:
                print(letters)
            return found_set

        return recur(idx+1, letters) or recur(idx+1, letters + s2[idx])

    return recur()


count_vowels = count_vowels_init()

if __name__ == '__main__':
    string1, string2 = 'python', 'loveprogramming'
    print(wyraz(string1, string2))


'''
'ula', 'exe'
'auxfga', 'auaxghuytqjfnhicidjmklkjalaaua'
'''
