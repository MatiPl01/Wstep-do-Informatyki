if __name__ == '__main__':
    data = []

    # Get user input
    while True:
        num = int(input('> '))
        if num == 0:
            break
        data.append(num)

    print(sorted(data, reverse=True)[9])
