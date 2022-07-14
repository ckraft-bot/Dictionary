import json
from difflib import get_close_matches as g

file = r"path\CH_Internet_Slang_Dictionary.json"
data = json.load(open (file))
keys  =  data.keys()

def meaning():

    w = e1_value.get()

    if w in data:
        for i, j in enumerate(data[w]):
            t1.insert(END,str(i)+' '+j+'\n')
    elif w.upper() in data:
        for i, j in enumerate(data[w.upper()]):
            t1.insert(END,str(i)+' '+j+'\n')
    elif w.title() in data:
        for i, j in enumerate(data[w.title()]):
            t1.insert(END,str(i)+' '+j+'\n')
    else:
        list = g(w,keys,n = 1,cutoff = 0.8)
        if len(list) == 0:
            t1.insert(END,"Sorry, no word found!")
        else:
            real = list[0]
            answer = tkinter.messagebox.askquestion("Word Suggestion", "Is your word "+real+"?")
            
            if answer == "yes":
                for i, j in enumerate(data[real]):
                    t1.insert(END,str(i)+' '+j+'\n')
            #elif x == "yes":
                #for i, j in enumerate(data[real]):
                    #t1.insert(END,str(i)+' '+j+'\n')
            else:
                t1.insert(END,"Hmmm... can't seem to find anything, check your input word again.")


def meaning2():
    t1.delete(1.0,END)
    e1.delete(0,END)

    meaning

from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
root = Tk()
root.title("Chinese Internet Slang Application by CKRAFT-BOT")

# widgets

header = Label(root, text = "Chinese Internet Slang Dictionary", bg = "cornflowerblue", fg = "white")
header.pack(fill = X)

label1 = Label(root, text = "Enter your word or acronym:")
label1.pack()

# Create an object of tkinter ImageTk
visual =  r"path\Slang.jpg"
img = ImageTk.PhotoImage(Image.open(visual))
label3 = Label(root, image  =  img)
label3.pack()

e1_value = StringVar()
e1 = Entry(root, textvariable = e1_value)
e1.pack()

button = Button(root, text = "Define", command = meaning, bg = "lightsteelblue", fg = "black")
button.pack()

t1 = Text(root)
t1.pack(fill = X)

label2 = Label(root, text = "Clear the screen by clicking the button below")
label2.pack()



button2 = Button(root,text = "Define another word!", command = meaning2, bg = "lightsteelblue", fg = "black")
button2.pack()


root.mainloop()