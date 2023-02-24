import turtle

# Create a turtle screen
screen = turtle.Screen()

# Set the screen size and background color
screen.setup(600, 600)
screen.bgcolor("skyblue")

# Create a turtle for drawing the house
house = turtle.Turtle()

# Set the turtle speed and width
house.speed(0)
house.width(3)

# Define the house size and position
house_size = 100
house_x = -house_size / 2
house_y = -house_size / 2

# Draw the house base
house.penup()
house.goto(house_x, house_y)
house.pendown()
for i in range(4):
    house.forward(house_size)
    house.left(90)

# Draw the roof
house.penup()
house.goto(house_x, house_y + house_size)
house.pendown()
house.goto(house_x + house_size / 2, house_y + house_size * 1.5)
house.goto(house_x + house_size, house_y + house_size)

# Draw the windows
window_size = house_size / 5
window_y = house_y + house_size / 4
window_gap = house_size / 6
for i in range(2):
    window_x = house_x + house_size / 4 + i * (house_size / 2)
    for j in range(2):
        house.penup()
        house.goto(window_x + j * (window_size + window_gap), window_y)
        house.pendown()
        for k in range(4):
            house.forward(window_size)
            house.left(90)

# Draw the door
door_size = house_size / 5
door_x = house_x + house_size / 2 - door_size / 2
door_y = house_y
house.penup()
house.goto(door_x, door_y)
house.pendown()
for i in range(2):
    house.forward(door_size)
    house.right(90)
    house.forward(door_size / 2)
    house.right(90)

# Draw the chimney
chimney_size = house_size / 10
chimney_x = house_x + house_size / 4
chimney_y = house_y + house_size * 3 / 4
house.penup()
house.goto(chimney_x, chimney_y)
house.pendown()
house.forward(chimney_size)
house.right(90)
house.forward(chimney_size)
house.right(90)
house.forward(chimney_size)
house.right(90)
house.forward(chimney_size / 2)
house.right(90)
house.forward(chimney_size / 2)
house.right(90)
house.forward(chimney_size / 2)
house.right(90)

# Draw the text
text_x = house_x + house_size / 2
text_y = house_y - 20
house.penup()
house.goto(text_x, text_y)
house.pendown()
house.write("My House (100m²)", align="center", font=("Arial", 12, "bold"))

# Hide the turtle
house.hideturtle()

# Keep the screen open until closed by user
turtle.done()
