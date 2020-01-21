
import turtle
import time

my_turtle = turtle.Turtle()

def square():
    for i in range(10000):
        my_turtle.forward(i)
        time.sleep(0.00001)
        my_turtle.left(i)
        my_turtle.forward(i)
        time.sleep(0.00001)
        


square()