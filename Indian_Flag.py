import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.bgcolor("black")  # Background color

# Create a turtle to draw the flag
flag = turtle.Turtle()
flag.speed(3)

# Function to draw a rectangle
def draw_rectangle(color, width, height):
    flag.begin_fill()
    flag.color(color)
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()

# Adjust these values to make the flag bigger
width = 450  # Width of each stripe
height = 75  # Height of each stripe

# Draw the saffron rectangle
flag.penup()
flag.goto(-225, 225)
flag.pendown()
draw_rectangle('#FF9933', width, height)

# Draw the white rectangle
flag.goto(-225, 150)
draw_rectangle('white', width, height)

# Draw the green rectangle
flag.goto(-225, 75)
draw_rectangle('#138808', width, height)

# Draw the Ashoka Chakra (24-spoked wheel)
flag.penup()
flag.goto(0, 150)
flag.pendown()
flag.color("#000080")
flag.circle(-37.5)  # Adjusted radius for the bigger flag

# Draw the 24 spokes of the Ashoka Chakra
flag.penup()
flag.goto(0, 112.5)
flag.setheading(0)
flag.pendown()

for _ in range(24):
    flag.forward(37.5)
    flag.backward(37.5)
    flag.left(15)

# Hide the turtle and display the flag
flag.hideturtle()
turtle.done()
