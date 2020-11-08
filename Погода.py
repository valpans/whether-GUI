# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:23:01 2020

@author: valpans
"""

import PIL
import tkinter as tk

def weather(entry):
    print('This is the entry:', entry)

root = tk.Tk()

root.title("Погода")

canvas = tk.Canvas(root, height = 500, width=600)
canvas.pack()

background_image = tk.PhotoImage(file='img.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = "#80c1ff", bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, text="Type region")
entry.insert(0,"Boston")
entry.place(relwidth=0.65, relheight=1 )

button = tk.Button(frame, text="Search", font=40, command= lambda: weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3,)

lower_frame = tk.Frame(root, bg = "#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame,)
label.place(relwidth=1, relheight=1)

root.mainloop()