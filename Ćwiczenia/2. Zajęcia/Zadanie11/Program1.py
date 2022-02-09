num = input('> ')

for i in range(len(num)-1):
    if num[i+1] <= num[i]:  # We don't have to convert number to the integer because ASCII numbers are in the right order
        print(False)
        break
else:
    print(True)
