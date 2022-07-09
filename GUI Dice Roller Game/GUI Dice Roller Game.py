# Python Tkinter GUI Dice Roller Guessing Game

# importing dependancies
from tkinter import *
from random import randint
from PIL import ImageTk, Image

# object creation for tkinter
game = Tk()
game.geometry("570x600+100+20")
game.resizable(False, False)
game.title("Python Tkinter GUI Dice Roller Guessing Game")



# function to load dieface image
def load_dieface_img(face):
    if (face == 1):
        photo_one = Image.open("E:\Documents\Projects\PyCharm\Practice Python\GUI Dice Roller Game\Dice - png\One.png")
        return photo_one
    elif (face == 2):
        photo_two = Image.open("E:\Documents\Projects\PyCharm\Practice Python\GUI Dice Roller Game\Dice - png\Two.png")
        return photo_two
    elif (face == 3):
        photo_three = Image.open(
            "E:\Documents\Projects\PyCharm\Practice Python\GUI Dice Roller Game\Dice - png\Three.png")
        return photo_three
    elif (face == 4):
        photo_four = Image.open(
            "E:\Documents\Projects\PyCharm\Practice Python\GUI Dice Roller Game\Dice - png\Four.png")
        return photo_four
    elif (face == 5):
        photo_five = Image.open(
            "E:\Documents\Projects\PyCharm\Practice Python\GUI Dice Roller Game\Dice - png\Five.png")
        return photo_five
    elif (face == 6):
        photo_six = Image.open("E:\Documents\Projects\PyCharm\Practice Python\GUI Dice Roller Game\Dice - png\Six.png")
        return photo_six
    return 0


# guess button action definition
def btn_guess_action():
    a = randint(1, 7)

    photo = load_dieface_img(a)
    photo_resize = photo.resize((300, 205), Image.ANTIALIAS)
    new_photo = ImageTk.PhotoImage(photo_resize)
    die_label = Label(image=new_photo)
    die_label.image = new_photo
    die_label.place(x=150, y=150)

    x = int(guessText.get("1.0", "end-1c"))

    if x == a:
        result = Label(game, height=1, width=40, font=("arial", 14), text="Guessed Correctly.")
        result.place(x=150, y=500)
    else:
        result = Label(game, height=1, width=40, font=("arial", 14), text="Guessed Wrong.")
        result.place(x=150, y=500)


# Declaring GUI Components
guessLabel = Label(game, height=1, width=30, font=("arial", 14), text="Guess a die face ").place(x=0, y=25)
resultLabel = Label(game, height=1, width=10, font=("arial", 14), text="RESULT: ").place(x=0, y=150)
guessText = Text(game, height=1, width=15, font=("arial", 14))
guessText.place(x=350, y=25)
guessBtn = Button(game, command=btn_guess_action, height=1, width=15, font=("arial", 14), text="ROLL!").place(x=200, y=80)

#running game
game.mainloop()
