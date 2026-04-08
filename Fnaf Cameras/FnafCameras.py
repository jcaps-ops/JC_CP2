import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk

root.title("Testing GUI")
root.configure(background="light blue")
root.minsize(900,300)
root.maxsize(1500,500)
root.geometry("1200x400+100+100")

root.count = 0
image = PhotoImage(file="gfg.png")
btn = tk.Button(root, )
btn.place(relx=.52, rely=0.4, anchor="n")