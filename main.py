# Import the Turtle Module
import turtle
# Import the Random Module
import random
# Import the Color List in RGB Format
from color_gen import color_rgb

# Set the Color Mode to 255
turtle.colormode(255)

# Create an Object from the Turtle Class
tim = turtle.Turtle()


for p in range(10):
    # For setting the Turtle Position
    tim.penup()
    tim.setpos(-230, -300+p*50)
    tim.pendown()
    for i in range(10):
        tim.dot(20, random.choice(color_rgb))
        tim.penup()
        tim.forward(50)
        tim.pendown()

# Screen Setting
screen = turtle.Screen()
screen.exitonclick()
