import tkinter as tk

root = tk.Tk()

root.title("Testing GUI")
root.configure(background="light blue")
root.minsize(250,250)
root.maxsize(1500,1500)
root.geometry("300x300+100+100")

start = tk.Label(root, text="This is the first Gui Prodcut", font=("Times New Roman", 30, "bold")).grid(row= 0,column=0, columnspan=2)
#start.config(fg="Dark Blue", background="Light Blue")

#tk.Label(root, text="This is a label").grid(row= 1,column=0).pack()

#Making a counter
root.count = 0

def add():
    root.count += 1
    lbl['text'] = str(root.count)
def sub():
    root.count -= 1
    lbl['text'] = str(root.count)

btn = tk.Button(root, text="Add 1", command=add)
btn.grid(row= 4,column=0)
btn2 = tk.Button(root, text="subtract 1", command=sub)
btn2.grid(row= 4,column=1)

lbl = tk.Label(root, text="0")
lbl.grid(row= 5,column=0, columnspan=2)

close = tk.Button(root, text="Bye", command=root.destroy)
close.grid(row= 6,column=0)
root.mainloop()