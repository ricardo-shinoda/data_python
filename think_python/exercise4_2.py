import turtle
bob = turtle.Turtle()


def polygon(t, n, length):
    angle = int(360 / n)
    for i in range(n):
        t.fd(length)
        t.lt(angle)


polygon(bob, 70, 70)
