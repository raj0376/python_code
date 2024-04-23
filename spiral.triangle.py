import turtle
forw = 1
lol = turtle.Turtle()
lol.speed(10)
lol.color("BLUE")
while True:
    lol.forward(forw)
    lol.left(120)
    lol.left(1)
    forw+=1
turtle.done()
