num = int(input('> '))

a_n = 2
while a_n <= num:
    if num % a_n == 0:
        print(True)
        break
    a_n = 3 * a_n + 1
else:
    print(False)
