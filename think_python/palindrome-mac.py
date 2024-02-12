def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]
    # return len(word) // 2


def letter_middle(word):
    return word[2:-2]


def is_palindrome(name):
    result = middle(name)
    letter = letter_middle(name)
    f = first(name)
    l = last(name)
    lenght = len(name)
    print('The middle result for', name, ' is: ', result)
    if lenght % 2 == 0 and f == l:
        print('This could be a palindrome yep!')
        new_r = middle(result)
        print('New result if: ', new_r)
    else:
        print("This can't be a palindrome, sorry...")


# is_palindrome('ricardor')


def test(m):
    result = middle(m)
    f = first(m)
    l = last(m)
    length = len(m)
    print(result)
    print(f)
    print(l)
    print('The length of m is: ', length)
    if length % 2 == 0 and f == l:
        print('This could be a palindrome, YES!')
    else:
        print('this is not a palindrome, NOPE!')


# test('lucas')


def test2(m):
    result = middle(m)
    f = first(m)
    l = last(m)
    length = len(m)
    print(result)
    print(f)
    print(l)
    print('The length of m is: ', length)
    for i in range(length):
        print(i)
        if length % 2 == 0 and f == l:
            print('This could be a palindrome, YES!')
        else:
            print('this is not a palindrome, NOPE!')


test2('lucas')
