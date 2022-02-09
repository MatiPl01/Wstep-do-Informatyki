k = int(input('> '))

eps = 1e-5
x = 1
field = 0
while x < k:
    y = 1 / x
    field += eps * y
    x += eps

print(field)
