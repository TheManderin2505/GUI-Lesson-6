from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.geometry("600x350")
root.title("rock paper scisors game")

player_score = 0
computer_score = 0

options = [('rock',0),('paper',1),('scissors',2)]

def player_win():
    global computer_score,player_score

    player_score = player_score + 1
    lbl2.config(text = "Player Won!",font = font.Font(size = 12),fg = "green")
    lbl5.config(text = "Player Score : "+ str(player_score))
    lbl6.config(text = " Computer Score : "+str(computer_score))

def computer_win():
    global computer_score,player_score

    computer_score = computer_score + 1
    lbl2.config(text = "Computer Won!",font = font.Font(size = 12),fg = "red")
    lbl5.config(text = "Player Score : "+str(player_score))
    lbl6.config(text = "Computer Score : "+ str(computer_score))

def tie():
    global computer_score,player_score

    lbl2.config(text = "Tie!",font = font.Font(size = 12),fg = "grey")
    lbl5.config(text = "Player Score : "+ str(player_score))
    lbl6.config(text = "Computer Score : " + str(computer_score))

def computer_choice():
    return random.choice(options)

def player_choice(player_input):
    global player_score, computer_score

    computer_input = computer_choice()
    lbl7.config(text = "You Selected : "+player_input[0])

    lbl8.config(text = "Computer Selected : "+computer_input[0])

    if player_input == computer_input:
        tie()
    
    #Player Choses Rock
    if(player_input[1] == 0):
        if(computer_input[1] == 1):
            computer_win()

        elif(computer_input[1] == 2):
            player_win()

    elif(player_input[1] == 1):
        if(computer_input[1] == 0):
            player_win()

        elif(computer_input[1] == 2):
           computer_win()

    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_win()

        elif(computer_input[1] == 1):
            player_win()



# U.I

lbl1 = Label(root, text = " Rock Paper Scisors Game",font= font.Font(size = 15),fg = "grey")
lbl1.pack(pady=20)

lbl2 = Label(root, text = "Lets Start The Game!",font = font.Font(size = 12),fg = "black")
lbl2.pack()

frame1 = Frame(root)
frame1.pack()

lbl3 =Label(frame1, text = "Your Options :",font = font.Font(size = 12),fg = "black")
lbl3.grid(row = 0, column= 0)

btn1 = Button(frame1, text = "Rock",bg = "grey",fg = "black",bd = 0, width = 15, command = lambda: player_choice(options[0]))
btn1.grid(row=1,column=1,padx=7,pady=7)

btn2 = Button(frame1, text = "Paper",bg = "white",fg = "black",bd = 0, width = 15, command = lambda: player_choice(options[1]))
btn2.grid(row=1,column=2,padx=7,pady= 7)

btn3=Button(frame1,text = "Scissors",bg = "light grey", fg = "black", bd = 0, width = 15, command = lambda: player_choice(options[2]))
btn3.grid(row=1,column=3,padx=7,pady= 7)

lbl4 = Label(frame1,text = "Score :",font = font.Font(size = 12), fg = "black")
lbl4.grid(row = 2, column=0,pady=20)

lbl5 = Label(frame1, text = "Your Score : ----",font = font.Font(size = 12), fg = "grey")
lbl5.grid(row=3,column=1)

lbl6 = Label(frame1, text = "Computer Score : ----",font = font.Font(size = 12), fg = "grey")
lbl6.grid(row = 3, column = 2)

lbl7 = Label(frame1, text = "You Selected : ----",font = font.Font(size = 12), fg = "grey")
lbl7.grid(row=4,column = 1)

lbl8 = Label(frame1, text = "Computer Selected : ----",font = font.Font(size = 12), fg = "grey")
lbl8.grid(row=4, column=2)

root.mainloop()