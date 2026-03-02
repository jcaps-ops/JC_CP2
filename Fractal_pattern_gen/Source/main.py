import turtle
from triangle import sierpinski
from color import color_picker

def main():
   count = input("How much do you want it to reacure:")
   count = int(count)
   col_pil = color_picker()
   turtle.color(col_pil)
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,count)
   myWin.exitonclick()

main()