# Importing Libraries

import tkinter
from PIL import Image, ImageTk
import random


# Top-level widget which represents the main window of the application

root = tkinter.Tk()
root.geometry('400x450')
root.title('Dice Roll')


# Adding label into the frame

l0 = tkinter.Label(root, text = "")
l0.pack()


# Adding label with different font and formatting

l1 = tkinter.Label(root, text = "Random Dice Roll", fg = "black", font = "Helvetica 16 bold italic")
l1.pack()


# Images

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']


# Simulating the dice with random numbers between 1 to 6 and generating the image

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))


# Construct a label widget for the image

label1 = tkinter.Label(root, image = image1)
label1.image = image1


# Packing a widget in the parent widget 

label1.pack(expand = True)


# Function activated by button

def DiceRoll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image = image1)
    # keep a reference
    label1.image = image1


# Adding button and command will use DiceRoll function

button = tkinter.Button(root, text = 'Roll the Dice', fg = 'black', command = DiceRoll)


# Pack a widget in the parent widget

button.pack(expand = True)


# Call the mainloop of Tk

root.mainloop()


