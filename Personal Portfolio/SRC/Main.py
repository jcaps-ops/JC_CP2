import tkinter as tk

root = tk.Tk()

root.title("Testing GUI")
root.configure(background="light blue")
root.minsize(900,300)
root.maxsize(1500,500)
root.geometry("1200x400+100+100")

root.count = 0

def add():
    root.count += 1
    if root.count == 5:
        root.count = 0
    updates()
    
def sub():
    root.count -= 1
    if root.count == -1:
        root.count = 4
    updates()

def updates():
    if root.count == 0:
        lbl["text"] = f"Hello Welcome to Jaxon castros coding portfolio\nHow to use it use the buttons to cycle between the diffrent projects"
    if root.count == 1:
        lbl["text"] = f"project 1\nHigh Score Tracker \nThis project is a gambling game that the user can play.At the end (either once you win and beat the game or you quit), it will save your score and also save your high score.\nIn this project I learned\n.How annoying bugfixing can be\n.How to fix and update code better\n.One problem was having to change the game form global varibles to regular ones"
    if root.count == 2:
        lbl["text"] = f"Project 2\nPet Simulator \nThis project is about a tomogachi like pet simulator where you take care of a creature.\n In this project I Learned the following.\n1.How to properly use some parts of classes\n 2. To use several functions to simplify\n the problem I faced was the complexity of the code to read"
    if root.count == 3:
        lbl["text"] = f"Project 3\n Horse Racing Simulator \n This project is where made a simple horse racing simulator. Where the horses racing using randomly generator skills and stats\n In this project I learned the following:\n1.How to use faker\n2.How to properly organize my code\n The problem was trying to learn how to use Faker"
    if root.count == 4:
        lbl["text"] = f"Project 4\nRPG Charater Manager\n This project was an upgrade of a pre existing project where I upgraded to include Faker and Charts\nIn this project I Learned the following.\n1.How to use MatPlotLib\n2. How to code to pre existing code\n The problem was trying to read the code"        
    

btn = tk.Button(root, text="--->", command=add)
btn.place(relx=.52, rely=0.4, anchor="n")
btn2 = tk.Button(root, text="<---", command=sub)
btn2.place(relx=.49, rely=0.4, anchor="n")

lbl = tk.Label(root, text="Hello Welcome to Jaxon castros coding portfolio\nHow to use it use the buttons to switch between the diffrent projects", bg="Light Blue", font=("Times new roman", 14, "bold"))
lbl.place(relx=.5, rely=0, anchor="n")
#lbl.grid(row= 1,column=0, columnspan=2)

close = tk.Button(root, text="Bye", command=root.destroy)
close.grid(row= 6,column=0)
root.mainloop()