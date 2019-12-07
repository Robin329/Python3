#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:48:05 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""
import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)

#l = tk.Label(root, text='OMG! this is TK!', bg = 'green', font = ('Arial', 12), width=15, height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        vat.set('')

b = tk.Button(window, text='hit me', width=15,
              height=2, command=hit_me)

b.pack()

window.mainloop()