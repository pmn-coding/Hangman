#from hdef import Hangman
from tkinter import *
from random import *

main = Tk()
main.title("HANGMAN")
main.configure(width="800", height="400")
main.geometry("800x800")

words = ["Katze","Haus","Hase","Affe","Panzer","Danke","Igel","Taste","Buchstabe","Wort"]




guess = words[randint(0,9)]


def check(event, y, w):
    for i in range(len(w)):
        if w in y:
            event.widget.config(state="disabled", background="lightgreen")
        else:
            event.widget.config(state="disabled", background="red")


def letter(x, gc, gr):
    global lbutton
    c = "lightblue"
    lbutton = Button(frame2, text = x, width="3", height="2", bg=c, activebackground="lightblue")
    lbutton.grid(row=gr,column=gc)
    return lbutton




main.resizable(FALSE,FALSE)
frame1 = Frame(main, width="600",height="600")
frame1.grid(row=0, sticky=E)
frame2 = Frame(main,bg="grey",width="200")
frame2.grid(row=1, sticky=E)

letter("A", 1, 0).bind("<ButtonRelease-1>", check)
letter("B", 2, 0).bind("<ButtonRelease-1>", check)
letter("C", 3, 0).bind("<ButtonRelease-1>", check)
letter("D", 4, 0).bind("<ButtonRelease-1>", check)
letter("E", 5, 0).bind("<ButtonRelease-1>", check)
letter("F", 6, 0).bind("<ButtonRelease-1>", check)
letter("G", 7, 0).bind("<ButtonRelease-1>", check)
letter("H", 8, 0).bind("<ButtonRelease-1>", check)
letter("I", 9, 0).bind("<ButtonRelease-1>", check)
letter("J", 10, 0).bind("<ButtonRelease-1>", check)
letter("K", 11, 0).bind("<ButtonRelease-1>", check)
letter("L", 12, 0).bind("<ButtonRelease-1>", check)
letter("M", 13, 0).bind("<ButtonRelease-1>", check)
letter("N", 1, 1).bind("<ButtonRelease-1>", check)
letter("O", 2, 1).bind("<ButtonRelease-1>", check)
letter("P", 3, 1).bind("<ButtonRelease-1>", check)
letter("Q", 4, 1).bind("<ButtonRelease-1>", check)
letter("R", 5, 1).bind("<ButtonRelease-1>", check)
letter("S", 6, 1).bind("<ButtonRelease-1>", check)
letter("T", 7, 1).bind("<ButtonRelease-1>", check)
letter("U", 8, 1).bind("<ButtonRelease-1>", check)
letter("V", 9, 1).bind("<ButtonRelease-1>", check)
letter("W", 10, 1).bind("<ButtonRelease-1>", check)
letter("X", 11, 1).bind("<ButtonRelease-1>", check)
letter("Y", 12, 1).bind("<ButtonRelease-1>", check)
letter("Z", 13, 1).bind("<ButtonRelease-1>", check)

main.mainloop()