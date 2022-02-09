def gcd(a, b):
    return a if not b else gcd(b, a%b)


def are_relative_primes(a, b):
    return gcd(abs(a), abs(b)) == 1


def split_number_into_relative_primes(num):
    result = []

    def recur(remaining, num1=0, num2=0, mul1=1, mul2=1):
        if not remaining:
            if are_relative_primes(num1, num2):
                result.append((num1, num2))
        else:
            remaining, dgt = divmod(remaining, 10)  # Take the last digit of the remaining number's part
            recur(remaining, mul1*dgt + num1, num2, mul1*10, mul2)  # Add a digit to the num1
            recur(remaining, num1, mul2*dgt + num2, mul1, mul2*10)  # or to the num2

    recur(num)

    print(result)

    return len(result)


if __name__ == '__main__':
    # I assume that e.g. (1523, 2) and (2, 1523) are different as A is different from B
    print(split_number_into_relative_primes(21523))
