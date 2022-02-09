# This algorithm doesn't use rounding
a, b, n = (int(input(f'{var_name} > ')) for var_name in 'abn')

# I use list and then join elements to string because appending an element
# to a list is O(1) operation but string concatenation is O(n)
result = []
is_floating_point = True

while a > 0 and n > -1:
    n -= 1

    if a < b:
        if is_floating_point:
            result.append('.')
            is_floating_point = False
        a *= 10

    digit, a = divmod(a, b)  # The same as: digit = a // b; a = a % b
    result.append(str(digit))


print(''.join(result))
