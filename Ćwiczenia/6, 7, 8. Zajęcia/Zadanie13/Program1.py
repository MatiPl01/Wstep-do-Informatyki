def func(num: int) -> list:
    results = []
    current = []

    def recur(n=num, k=1):
        nonlocal current
        if n == 0:
            results.append(current.copy())
        else:
            for j in range(k, n+1):
                current.append(j)
                recur(n - j, j)
                current.pop()
    recur()

    return results


if __name__ == '__main__':
    print(func(4))
