def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    # return word[2:-2]
    return len(word) // 2


def length(word):
    '''Thinking on work with the lentgh and divide by half and then use it with
    the functions already using on this file'''
    comprimento = len(word)
    half = comprimento / 2
    print(comprimento)
    print(half)


# letra = length('ricardor')

word = 'ricardoshinodar'
result_middle = middle(word)
result_first = first(word)
result_last = last(word)
print('First: ', result_first)
print('Middle: ', result_middle)
print('Last: ', result_last)


def is_palidrome(f, l, m):
    if f == l:
        print('This could be a palindrome')
        print(m)
        comprimento = m
        while comprimento >= 2:
            r = middle(comprimento)
            comprimento = r
        print('This is the new middle: ', r)
    else:
        print('This is not a palindrome')
        print(m)


is_palidrome(result_first, result_last, result_middle)
is_palidrome('Ricardo')


def final_palidrome(name):
    resul = name
    while len(resul) >= 2:
        r = middle(resul)
        resul = r
        print('this is the resul: ', resul)
        if len(resul) == 3:
            print("This can't be a palingrome")


final_palidrome('Ricardo')
