import turtle

Turtle_count = input("How many times do you want to do it")
Turtle_count = int(Turtle_count)
Triple_div_count = 0
Count = 0
turtle.teleport(-200,0)

for y in range(0,3):
    length = 300
    Triple_div_count += 1
    temp_Count = 0
    if Triple_div_count == 2:
            turtle.penup()
            turtle.goto(sec_pos)
            turtle.pendown()
    if Triple_div_count == 3:
            turtle.penup()
            turtle.goto(tri_pos)
            turtle.pendown()
    Triple_div_count_2 = 0
    for x in range(0,Turtle_count):
        Triple_div_count_2 += 1
        temp_Count += 1
        """
        if Triple_div_count_2 == 2:
            turtle.penup()
            turtle.goto(temp_sec_pos)
            turtle.pendown()
            turtle.backward(length)
        if Triple_div_count_2 == 3:
            turtle.penup()
            turtle.goto(temp_tri_pos)
            turtle.pendown()
            turtle.backward(length)
        """
        for z in range (0,3):
                Count += 1
                turtle.forward(length)
                turtle.left(120)
                if Count == 1:
                    sec_pos = turtle.pos()
                if Count == 2:
                    tri_pos = turtle.pos()
                #if temp_Count == 1:
                    #temp_sec_pos = turtle.pos()
                #if temp_Count == 2:
                    #temp_tri_pos = turtle.pos()
        length = length/2
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(-120)
        turtle.forward(length)
        turtle.left(-120)
        turtle.forward(length)
        turtle.left(120)
        
    

turtle.done()