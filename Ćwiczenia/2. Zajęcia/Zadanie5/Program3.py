import math


def zad5(num: int, div: int):
    ans = 0

    for mask in range(1, 1 << (int(math.log10(num)) + 1)):
        single_bit = 1
        tmp_num = num
        pow10 = 1
        generated_num = 0
        while tmp_num:
            if single_bit & mask:
                generated_num += pow10*(tmp_num % 10)
                pow10 *= 10

            tmp_num //= 10
            single_bit *= 2  # bit<<1

        if generated_num % div == 0:
            ans += 1
            print(generated_num)

        mask += 1

    return ans


if __name__ == "__main__":
    print(zad5(int(input('> ')), 7))
