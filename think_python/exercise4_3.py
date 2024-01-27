import math
import turtle

bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# square(bob, 300)


def polygon(t, n, length):
    angle = int(360 / n)
    # print(angle)
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# polygon(bob, n=7, length=70)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)


# circle(bob, 200)


def arc(t, r, angle):
    polygon(t, 70, angle)


# circle(bob, 1000)
# arc(bob, 2, 360)
