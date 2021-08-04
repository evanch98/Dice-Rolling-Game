# Import necessary modules
from tkinter import *
from tkinter import ttk
import random, time

# Creating Window
root = Tk()
root.geometry('250x150')
root.resizable(0, 0)
root['bg'] = "#B3E5FC"
root.title('Dice Rolling')

# Lable and Photo
Label(root, text='DICE ROLLING GAME', bg='#B3E5FC', font='arial 10 bold').pack()
Label(root, text='Player', font='arial 10', bg='#B3E5FC').place(x=5, y=30)
Label(root, text='Computer', font='arial 10',bg='#B3E5FC').place(x=5, y=70)
photo = PhotoImage(file='dice.png')
Label(root, image=photo).place(x=15, y=100)

# Rolling Dice
def dice():
    Nums = [1, 2, 3, 4, 5, 6]
    playerDice = random.choice(Nums)
    computerDice = random.choice(Nums)

    time.sleep(1)   # Time for dice to hit the ground XP

    # Display Player's Dice Number
    playerResult.delete(0, END)
    playerResult.insert(0, str(playerDice))
    # Display Computer's Dice Number
    computerResult.delete(0, END)
    computerResult.insert(0, str(computerDice))

# Creating Entry Widget for Player's Dice Number
playerResult = Entry(root)
playerResult.place(x=75, y= 30)

# Creating Entry Widger for Computer's Dice Number
computerResult = Entry(root)
computerResult.place(x=75, y=70)

# Button to Roll the Dice
ttk.Button(root, text='Roll', command=dice).place(x=90, y=110)

# Mainloop
root.mainloop()
