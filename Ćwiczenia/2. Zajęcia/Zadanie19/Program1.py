class InfiniteDecimalPoint(Exception):
    pass


a = int(input('> '))
b = int(input('> '))

fixed_point, a = divmod(a, b)
floating_point_digits = []
checked_divmod_pairs = []

try:
    while a:
        a *= 10
        pair = divmod(a, b)
        digit, a = pair

        # Check if a floating point is infinite
        for i in range(len(checked_divmod_pairs)-1, -1, -1):
            if pair == checked_divmod_pairs[i]:
                floating_point_digits.insert(i, '(')
                floating_point_digits.append(')')
                raise InfiniteDecimalPoint()

        checked_divmod_pairs.append(pair)
        floating_point_digits.append(str(digit))
except InfiniteDecimalPoint:
    pass

print(f'{fixed_point}.{"".join(floating_point_digits)}')
