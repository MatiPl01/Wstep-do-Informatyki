num = input('> ')

if len(num) > 9:
    print(False)
else:
    print(str(len(num)) in num)
