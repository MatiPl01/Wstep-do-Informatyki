a_n = 0
a_n_next = 1
b_n = 2

while int(input('> ')) == a_n:
    print(b_n)
    b_n = b_n + 2 * a_n_next
    a_n, a_n_next = a_n_next, a_n_next - b_n * a_n
