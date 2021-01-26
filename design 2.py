from turtle import *
wn = Screen()
wn.bgcolor("black")
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
speed(50)
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)
