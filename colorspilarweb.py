#Prorgram to design COLORSPIRAL WEB.
import turtle
colors=['red', 'yellow', 'green', 'pink', 'orange', 'purple']
t=turtle.pen()
turtle.bgcolor("black")

for x in range(500):
    t.pen(colors(x%6))
    t.width(x/100+1)
    t.forward(x)#pointer of that turtle triangle if backwardit will make from edge of removed no draw.
    t.left(50)#Rotate the turtle with an angle less angle more circle like structure.
