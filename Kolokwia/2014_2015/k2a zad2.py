def count_vowels_init():
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    def count_vowels(string):
        count = 0
        for char in string:
            count += char in vowels
        return count

    return count_vowels


count_vowels = count_vowels_init()


def sum_ascii_codes(string):
    sum_ = 0
    for char in string:
        sum_ += ord(char)
    return sum_


def have_the_same_weight(string1, string2):
    return sum_ascii_codes(string1) == sum_ascii_codes(string2)\
        and count_vowels(string1) == count_vowels(string2)


def wyraz(s1, s2):

    def recur(idx=0, word=''):
        if idx == len(s2):
            if have_the_same_weight(word, s1):
                print(word)
                return True
            return False

        return recur(idx+1, word + s2[idx]) or recur(idx+1, word)

    return recur()


if __name__ == '__main__':
    s1 = 'python'
    s2 = 'loveprogramming'
    print(wyraz(s1, s2))
