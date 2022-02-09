# If count of appropriate digits matters
# e.g. 125 and 1111122255555555 will be considered as numbers made up of different digits
if __name__ == '__main__':
    a = input('> ')
    b = input('> ')

    if len(a) != len(b):
        print(False)
        exit()

    for dgt_a, dgt_b in zip(sorted(a), sorted(b)):
        if dgt_a != dgt_b:
            print(False)
            break
    else:
        print(True)
