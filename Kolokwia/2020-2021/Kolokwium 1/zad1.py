"""
Mateusz Łopaciński

W pierwszej iteracji wyodrębniam kolejne ciągi tekstowe z tablicy.
W drugiej iteracji (przy pomocy zmiennej idx) poszukuję początkowego indeksu podciągu.
Sprawdzam, czy dla danego indeksy może istnieć wielokrotność podciągu.
Jeżeli tak, to sprawdzam, czy ciąg się powtarza, jeżeli nie, to sprawdzam kolejny indeks.
"""

def multi(T):
    max_length = 0

    for string in T:
        for idx in range(1, len(string)//2+1):
            if len(string) % idx == 0:
                for i in range(idx):
                    for j in range(idx+i, len(string), idx):
                        if string[i] != string[j]:
                            break  # Break if two values are different
                    else:
                        continue  # If not broken, continue searching
                    break  # If broken loop before, break outer loop
                else:
                    if len(string) > max_length:  # Update length if is greater
                        max_length = len(string)

    return max_length


if __name__ == '__main__':
    N = int(input())
    T = [input() for _ in range(N)]
    print(multi(T))
