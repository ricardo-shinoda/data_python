def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[2:-2]


def length(word):
    '''Thinking on work with the lentgh and divide by half and then use it with
    the functions already using on this file'''
    comprimento = len(word)
    div = int(comprimento / 2)
    print(comprimento)
    print(div)


letra = length('duas')

word = 'ricardoshinoda'
result_middle = middle(word)
result_fist = first(word)
result_last = last(word)
print('First: ', result_fist)
print('Middle: ', result_middle)
print('Last: ', result_last)


def is_palidrome(name):
    print('The name is: ', name)


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
