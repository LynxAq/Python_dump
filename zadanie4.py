import turtle

squares = 10 # Choose how many squares
scale = 20 # Chose the scale of the squares

t = turtle.Turtle()
for i in range(squares+1):
    for y in range(4):
        t.pendown()
        t.forward(scale*i)
        t.right(90)
    t.penup()
    t.setpos(t.xcor()-scale/2,t.ycor()+scale/2)

turtle.done()
