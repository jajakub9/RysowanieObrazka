import turtle
turtle.bgcolor('blue')
#zolw 1
t = turtle.Turtle()
t.shape('turtle')
t.color('green')
t.pensize(300)
t.penup()
t.goto(-650,-400)
t.pendown()
t.forward(1300)
#zolw 2
t2 = turtle.Turtle()
t2.shape('turtle')
t2.color('red', 'red')
t2.penup()
t2.goto(-400,-250)
t2.pendown()
t2.begin_fill()
for i in range(0,6):
    t2.forward(250)
    t2.left(90)
t2.end_fill()
t2.begin_fill()
t2.backward(50)
for j in range(0,3):
    t2.forward(350)
    t2.right(120)
t2.end_fill()
#zolw 3
t3 = turtle.Turtle()
t3.shape('turtle')
t3.color('green', 'green')
t3.penup()
t3.goto(100,-250)
t3.pendown()
t3.begin_fill()
t3.forward(200)
t3.left(100)
t3.forward(400)
t3.left(160)
t3.forward(400)
t3.end_fill()
#zolw 4
t4 = turtle.Turtle()
t4.shape('turtle')
t4.color('yellow')
t4.penup()
t4.goto(400,400)
t4.pendown()
while True:
    t4.forward(100)
    t4.left(170)





turtle.exitonclick()