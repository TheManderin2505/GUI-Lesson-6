from tkinter import *
import tkinter.font as font


root = Tk()
root.geometry("500x350")
root.title("rock paper scisors game")

frm1 = Frame(root)
frm2= Frame(root)

lbl1 = Label(root, text = " Rock Paper Scisors Game",font= font.Font(size = 15),fg = "grey")
lbl1.pack(pady=20)



root.mainloop()