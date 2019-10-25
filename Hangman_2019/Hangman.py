# :::::::::::::::::::::::::::::IMPORTS:::::::::::::::::::::::::::::

import tkinter as tk
import random as rnd
from time import sleep

# :::::::::::::::::::::::::::::UNTERPROGRAMME::::::::::::::::::::::

def check(ndex1):
    global guess
    global tries
    global rc
    global tb
    ind = True
    count = 0
    for c in guess:
        if btn_list[ndex1]["text"] == c.upper():
            count += 1
            ind = False
            rc += 1
            print(btn_list[ndex1]["text"]," Ist Richtig, Super!")
            lc[count-1] = (btn_list[ndex1]["text"]+ "  ")
            tb = "".join(lc)
            label1.config(text=tb)
        else:
            count += 1
            tries -= 1
    tries += count-1
    if tries == 0:
        print("Du hast leider keine Versuche übrig. Das Wort war: ", guess)
        exit()
    elif ind == True:
        print(btn_list[ndex1]["text"], " Ist Falsch, Schade.")       
        print("Du hast ", tries ," Versuche übrig.")
        tl2 = "Versuche: \n" + str(tries)
        label2.config(text=tl2)
        btn_list[ndex1].config(state="disabled", background="red")
    else:
        btn_list[ndex1].config(state="disabled", background="lightgreen")
    if rc == len(guess):
        print("Du hast das Wort erraten, Glückwunsch!")
        print("Das Wort war: ", guess)
        for i in range(26):
            btn_list[i].config(state="disabled")
        label3 = tk.Label(root, bg="bisque", text="Herzlichen Glückwunsch!",font="1")
        label3.grid(row=0, sticky="e", padx="110")

def buttons():
    row = 0 
    col = 1  
    for ndex, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        btn_list.append(tk.Button(frame2, text=char, width="3", height="2", bg="lightblue", activebackground="lightblue", command=lambda ndex1=ndex: check(ndex1)))  # Using a function in tkinter as lambda
        btn_list[-1].grid(row=row, column =col)
        if col <= 12:
            col += 1
        else:
            col = 1
            row += 1

# :::::::::::::::::::::::::::::HAUPTPROGRAMME::::::::::::::::::::::

root = tk.Tk() # Creating the window
root.title("HANGMAN")
root.geometry("800x800")

btn_list = []

quote = "Wenn du das lesen kannst läuft etwas falsch ..."
outp = tk.Canvas(root, width="400", height="50")
outp.grid(row=2, column=0, sticky="e", pady=10)
outp.config(cursor="arrow")
outp.create_text(200,25, text=quote, tags="text", font=("",20),activefill="mediumseagreen")



word_file = "dat/deutsch.txt"                   # File with about 660 words 
words = open(word_file).read().splitlines()     

#words = ["Katze","Haus","Hase","Affe","Panzer","Igel","Taste","Buch","Wort","Schwein","Tesla","NASA", "Kuchen", "Quanten","Eisen","Kohle","Merkel"]        That was our word list before the big file

guess = words[rnd.randint(0,len(words)-1)]



guess = guess.replace("Ä", "Ae")     
guess = guess.replace("Ö", "Oe")   
guess = guess.replace("Ü", "Ue") 
guess = guess.replace("ß", "ss")
guess = guess.replace("ä", "ae")
guess = guess.replace("ü", "ue")
guess = guess.replace("ö", "oe")

tries = 14
lc = []
rc = 0
for i in range(len(guess)):
    lc.append("_   ")
tb = "".join(lc)

tl2 = "Versuche: \n" + str(tries)
  

frame1 = tk.Frame(root, width="600", height="600")                                                  #Positioning
frame2 = tk.Frame(root, bg="grey", width="200")                                                     #buttons

label1 = tk.Label(root, text=tb, bg="lightblue", width="57", height="2", relief="groove")           #shows the word
label2 = tk.Label(root, text=tl2, bg="lightblue", width="10", height="3", relief="groove")          #tries counter

button1 = tk.Button(root, text="EXIT", bg="lightblue", width="9", height="2", command=root.destroy)

frame1.grid(row=0, sticky="e")                                                  
frame2.grid(row=1, sticky="e")

button1.grid(row=1, column="2", sticky="e", padx="50")

label1.grid(row=2, sticky="e", )
label2.grid(row=1, sticky="w", padx="75")

# :::::::::::::::::::::::::::::FUNCTIONS:::::::::::::::::::::::::::

buttons()


root.resizable(False, False)
root.mainloop()
