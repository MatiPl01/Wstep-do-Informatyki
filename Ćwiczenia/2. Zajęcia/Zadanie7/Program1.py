num = int(input('> '))

a_n = n = 1
while a_n <= num:
    a_n = n * n + n + 1
    if num % a_n:
        print(True)
        break
    n += 1
else:
    print(False)
