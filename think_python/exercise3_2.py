def do_twice(f, arg):
    f(arg)
    f(arg)


def print_twice(arg):
    print(arg)
    print(arg)


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

# Testando do_twice com print_spam


def print_spam():
    print('spam')


print("Chamando do_twice com print_spam:")
do_twice(print_spam, "spam")

# Testando do_twice com print_twice e 'spam' como argumento
print("\nChamando do_twice com print_twice:")
do_twice(print_twice, "spam")

# Chamando do_four com print_twice e 'spam' como argumento
print("\nChamando do_four com print_twice:")
do_four(print_twice, "spam")
