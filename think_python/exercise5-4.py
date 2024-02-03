def recurse(n, s):
    """
    This function will decrease the value assigned to n and using the same ammount, it will increase the same value to s
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        # print(n, s)


recurse(3, 0)
