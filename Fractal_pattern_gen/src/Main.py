import turtle

Turtle_count = input("How many times do you want to do it")
Turtle_count = int(Turtle_count)
length = 300
for x in range(1,Turtle_count):
    for y in range(0,3):
        for z in range (0,3):
            turtle.forward(length)
            turtle.right(120)
        turtle.forward(length/2)
        length = length/2
    turtle.forward(length)

turtle.done()