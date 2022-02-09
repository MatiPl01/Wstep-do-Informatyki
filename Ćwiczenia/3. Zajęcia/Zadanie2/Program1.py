# If count of appropriate digits doesn't matter
# e.g. 125 and 1111122255555555 will be considered as numbers made up of the same digits
if __name__ == '__main__':
    a = input('> ')
    b = input('> ')
    print(not set(a).symmetric_difference(set(b)))
