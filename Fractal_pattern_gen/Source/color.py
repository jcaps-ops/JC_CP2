import turtle
def color_picker():
    coloring = True
    while coloring:
        ply_imp = input("What color do you want to use:")
        try:
            turtle.color(ply_imp)
            return(ply_imp)
        except:
            print("That is not a avalible color")

