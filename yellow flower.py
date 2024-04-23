import turtle
turtle.bgcolor("Black")
turtle.speed(0)
def drawshape(turtle,radius):
    turtle.circle(radius,extent=60)
    turtle.left(120)
    turtle.circle(radius,extent=60)

def drawflower():
    petal=turtle.Turtle()
    petal.color("Yellow")
    petal.speed(2)
    petal.pensize(4)
    no_of_petals=15
    radius=300
    for i in range(no_of_petals):
        drawshape(petal,radius)
        petal.left(360/no_of_petals)

drawflower()
turtle.done()
