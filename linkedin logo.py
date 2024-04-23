#Program to design linkedin logo using turtle.
import turtle as t
t.pensize(3)
t.bgcolor("black")
t.speed(0)
t.shape("turtle")
t.up()
t.goto(0,-200)
t.down()

###Large Circle
t.color("blue")
t.begin_fill()
t.circle(230)
t.end_fill()

###Creating draw function to create rectangular

#####Letter I
def draw(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.color("White")
    t.begin_fill()
    for i in range(2):
        t.lt(90)
        t.fd(150)
        t.lt(90)
        t.fd(50)
    t.end_fill()

###call the function.    
draw(-70,-60)

####small circle
t.up()
t.goto(-90,110)
t.down()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

########Letter N
draw(20,-60)

t.up()
t.goto(0,60)
t.down()
t.begin_fill()
t.circle(45,45)
for i in range(120):
    t.fd(1)
    t.rt(1)

t.rt(15)
t.fd(110)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(70)
t.circle(35,135)
t.rt(135)
t.fd(30)
t.end_fill()

t.ht()
t.done()
  