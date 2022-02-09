from math import sqrt


num = int(input('> '))
lower_factor = greater_factor = int(sqrt(num))

while True:
    product = lower_factor * greater_factor
    if product == num:
        print(f'{lower_factor} * {greater_factor} = {num}')
        break
    if product < num:
        greater_factor += 1
    else:
        lower_factor -= 1
