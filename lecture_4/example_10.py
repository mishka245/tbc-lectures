import turtle


turtle.speed(0)
turtle.up()
turtle.goto(-250, 0)
turtle.down()

# draw 180 point star
for i in range(180):
    turtle.forward(500)
    turtle.right(180)
    turtle.left(2)

turtle.done()
