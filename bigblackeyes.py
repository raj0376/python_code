import turtle
t = turtle.Turtle()
t.speed(0)
move = 1
for i in range(360):
    t.pendown()
    t.right(move)
    t.forward(180)
    t.right(30)
    t.forward(60)
    t.left(30)
    t.forward(30)
    t.penup()
    t.home()
    move = move+1
    
screen.exitonclick()

