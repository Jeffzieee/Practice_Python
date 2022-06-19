from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.geometry("570x600+100+20")
root.resizable(False,False)

def jeff_ClickListener():
        try:
                n1 = float(num1TextField.get("1.0", "end-1c"))
                n2 = float(num2TextField.get("1.0", "end-1c"))
                n3 = str(n1 + n2)
                result = Label(root, width=10, height=1, text=n3, font=("arial", 10)).place(x=210, y=40)
        except:
                print("EXCEPTION!")


num1TextField = Text(root, height = 1, width = 10)
num2TextField = Text(root, height = 1, width = 10)
num1TextField.pack()
num2TextField.pack()

num1Label = Label(root,width=10,height=1,text="1st Number",font=("arial",10)).place(x=0,y=0)
num2Label = Label(root,width=10,height=1,text="2nd Number",font=("arial",10)).place(x=0,y=20)
resultLabel = Label(root,width=10,height=1,text="Result",font=("arial",10)).place(x=0,y=40)

Button(root,command=jeff_ClickListener,text="SUM",width=5, height=1,font=("arial",10,"bold"),bd=1,fg="#fff",bg="#3697f5").place(x=200,y=100)

root.mainloop()