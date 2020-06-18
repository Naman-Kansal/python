if __name__ == '__main__':
    s = 'qA2'
    alnum = 0
    alpha = 0
    digit = 0
    lower = 0
    upper = 0

    for letter in s:
        while letter:
            if letter.isalnum():
                alnum += 1
            if letter.isalpha():
                alpha += 1
            if letter.isdigit():
                digit += 1
            if letter.islower():
                lower += 1
            if letter.isupper():
                upper += 1

    for i in [alnum, alpha, digit, lower, upper]:
        if i > 0:
            print('True')
        else:
            print('False')
