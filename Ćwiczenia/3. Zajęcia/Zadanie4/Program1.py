# Easy solution using built-ins
import decimal
from math import factorial


if __name__ == '__main__':
    prec = int(input('> '))

    with decimal.localcontext() as ctx:
        ctx.prec = prec+1

        e = 0
        i = 0
        limit = 10 ** prec
        while True:
            fact = factorial(i)
            if fact > limit:
                break
            e += decimal.Decimal(1) / fact
            i += 1
    print(e)
