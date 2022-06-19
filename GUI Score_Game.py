#JEPHIN JOHN S6-CS2 Roll No 32
#Python Tkinter GUI Game

#importing dependancies
from tkinter import *
from random import randint

#declaring and initializing global variables
a=0
count = 3

#object creation for tkinter
game = Tk()
game.geometry("570x600+100+20")
game.resizable(False, False)
game.title("Jephin's Python Tkinter GUI Guessing Game")

#guessButton Function Definition
def btnGuessAction():
    global count
    global a
    if(count==3):
        a = randint(0, 11)

    if count<=3 and count>=1:
        x = int(guessText.get("1.0", "end-1c"))
        if x == a:
            result = Label(game, height=1, width=40, font=("arial", 14),text="Guessed Correctly with " + str(count) + " tries remaining.")
            result.place(x=150, y=150)
            count=3
        elif x < a:
            count -= 1
            result = Label(game, height=1, width=40, font=("arial", 14),text="Guessed Less." + str(count) + " tries remaining.")
            result.place(x=150, y=150)
        elif x > a:
            count-=1
            result = Label(game, height=1, width=40, font=("arial", 14),text="Guessed greater. " + str(count) + " tries remaining.")
            result.place(x=150, y=150)

    if (count == 0):
        count = 3
        result = Label(game, height=1, width=40, font=("arial", 14), text="You are out tries, Try Again! with new Number")
        result.place(x=150, y=150)

#Declaring GUI Components
guessLabel = Label(game, height=1, width=30, font=("arial", 14), text="Guess a number from 0 to 10: ").place(x=0, y=25)
resultLabel = Label(game, height=1, width=10, font=("arial", 14), text="RESULT: ").place(x=0, y=150)
guessText = Text(game, height=1, width=15,font=("arial",14))
guessText.place(x=350,y=25)
guessBtn = Button(game, command=btnGuessAction,height=1, width=15, font=("arial", 14), text="GUESS!").place(x=200, y=80)

game.mainloop()
