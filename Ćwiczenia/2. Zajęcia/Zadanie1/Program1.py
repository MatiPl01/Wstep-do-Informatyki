num = int(input('> '))

# Generate subsequent numbers from the Fibonacci sequence
f1, f2 = 1, 1
fibs = {f1, f2}  # I use set to make 'in' lookups faster - O(1)

while f2 <= num:
    quotient = num / f2
    if quotient in fibs:
        print('The specified number is a product of {0} and {1}: {0} * {1} = {2}'.format(
            int(quotient), f2, num
        ))
        break
    fibs.add(f1 + f2)
    f1, f2 = f2, f1 + f2
else:
    print(f"{num} isn't a product of two numbers from the Fibonacci sequence")
