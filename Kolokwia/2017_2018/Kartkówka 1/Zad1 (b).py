def generate_fibs(bound: int) -> list:
    fibs = [1, 1]
    while fibs[-1] < bound:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def get_next_matching_num(num: int) -> int:
    fibs = generate_fibs(num)
    while True:
        i, j = 0, 1
        curr_sum = fibs[0]
        num += 1

        if num > fibs[-1]:
            fibs.append(fibs[-1] + fibs[-2])

        while i < j < len(fibs):
            if curr_sum == num:
                break
            if curr_sum < num:
                curr_sum += fibs[j]
                j += 1
            else:
                curr_sum -= fibs[i]
                i += 1
        else:
            return num


if __name__ =='__main__':
    num = int(input('> '))
    print(get_next_matching_num(num))
