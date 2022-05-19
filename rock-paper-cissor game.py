import tkinter as tk
# import tkinter library
ob=tk.Tk()
ob.title('Rock-Paper-Scissors')
# entry for display what we need on output
text=tk.Entry(ob,width=80,borderwidth=2)
text.grid(row=0,column=0,columnspan=3)

def player1():
    first=text.get()
    text.delete(0,tk.END)
    global u1
    u1 = first
    print(u1)
def player2():
    second=text.get()
    text.delete(0,tk.END)
    global u2
    u2=second
    print(u2)


def submit():
    if u1 == u2:
        text.insert(0,"It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            text.insert(0,"Rock wins!")
        else:
            text.insert(0,"Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            text.insert(0,"Scissors win!")
        else:
            text.insert(0,"Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            text.insert(0,"Paper wins!")
        else:
            text.insert(0,"Scissors win!")
    else:
        text.insert(0,"Invalid input! You have not entered rock, paper or scissors, try again.")

number1=tk.Button(ob,height=2,width=25,borderwidth=2,command=lambda:player1())
number1.grid(row=1,column=0,columnspan=1)
tk.Label(ob,text="Player1").grid(row=1,column=0)
number2=tk.Button(ob,height=2,width=25,borderwidth=2,command=lambda:player2())
number2.grid(row=1,column=1,columnspan=1)
tk.Label(ob,text="player2").grid(row=1,column=1)
number3=tk.Button(ob,height=2,width=25,borderwidth=2,command=lambda:submit())
number3.grid(row=1,column=2,columnspan=1)
tk.Label(ob,text="submit").grid(row=1,column=2)

ob.mainloop()