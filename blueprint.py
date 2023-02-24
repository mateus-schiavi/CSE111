import turtle

# set up the turtle window
turtle.setup(600, 600)
turtle.title("Digivice")

# create a turtle object
t = turtle.Turtle()

# set the pen size and color
t.pensize(5)
t.pencolor("black")

# draw the main digivice shape
t.penup()
t.goto(0, -150)
t.pendown()
t.circle(150)

# draw the inner circle
t.penup()
t.goto(0, -80)
t.pendown()
t.circle(80)

# draw the triangles
t.penup()
t.goto(-70, -30)
t.pendown()
t.fillcolor("gray")
t.begin_fill()
for i in range(3):
    t.forward(140)
    t.left(120)
t.end_fill()

t.penup()
t.goto(-60, -20)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for i in range(3):
    t.forward(120)
    t.left(120)
t.end_fill()

# draw the center circle
t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(25)
t.end_fill()

# hide the turtle object
t.hideturtle()

# keep the window open until manually closed
turtle.done()
