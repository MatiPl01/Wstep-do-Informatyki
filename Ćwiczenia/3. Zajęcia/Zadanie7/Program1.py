import random

if __name__ == '__main__':
    n = int(input('> '))
    t = [random.randint(1, 1000) for _ in range(n)]

    for num in t:
        # num_cp = num
        while num > 0:
            num, digit = divmod(num, 10)
            # print(num_cp, digit)
            if digit % 2 == 0:
                break
        else:
            # print(num_cp)
            print(True)
            break
    else:
        print(False)
