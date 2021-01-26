#1. Import the turtle module
#2. Create a turtle to control.
#3. Draw around using the turtle methods.
#4. Run turtle.done().
import turtle
wn = turtle.Screen()
wn.bgcolor('light green')
wn.title("My Window")
s = turtle.Turtle()

for i in range(5):
    s.forward(50)
    s.right(144)


turtle.done()
