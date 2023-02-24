import turtle

# set up the turtle screen
screen = turtle.Screen()
screen.setup(width=500, height=500)

# create a turtle to draw with
t = turtle.Turtle()

# set the turtle's speed and color
t.speed(0)
t.color("green", "yellow")

# draw the head
t.begin_fill()
t.circle(80)
t.end_fill()

# draw the eyes
t.penup()
t.goto(-30, 60)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(30, 60)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# draw the mouth
t.penup()
t.goto(-60, 0)
t.pendown()
t.right(60)
t.circle(70, 120)

# draw the body
t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
t.circle(100)
t.end_fill()

# draw the legs
t.penup()
t.goto(-70, -180)
t.pendown()
t.right(20)
t.forward(70)
t.right(90)
t.forward(20)
t.penup()
t.goto(70, -180)
t.pendown()
t.left(40)
t.forward(70)
t.left(90)
t.forward(20)

# draw the tail
t.penup()
t.goto(70, -280)
t.pendown()
t.right(120)
t.forward(100)

# hide the turtle
t.hideturtle()

# keep the turtle window open
turtle.done()
