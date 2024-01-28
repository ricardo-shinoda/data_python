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


# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = 50
#     length = circumference / n
#     polygon(t, n, length)


# circle(bob, 200)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


circle(bob, 100)
