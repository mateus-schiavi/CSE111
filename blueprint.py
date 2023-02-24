import turtle

# create turtle object
t = turtle.Turtle()

# draw outer circle
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# draw inner circle
t.penup()
t.goto(0, -50)
t.pendown()
t.circle(50)

# draw four buttons
for i in range(4):
    t.penup()
    t.goto(50 * (i - 1), 0)
    t.pendown()
    t.dot(20)

# draw center button
t.penup()
t.goto(0, 0)
t.pendown()
t.dot(40)

# hide turtle
t.hideturtle()

# keep window open
turtle.done()
