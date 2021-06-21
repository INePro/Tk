#-*- coding: cp1251 -*-#
import tkinter as tk
root = tk.Tk()
l1 = tk.Label()
e1 = tk.Entry()
def cheat():
    l1['text'] = 'red'
    e1.delete(0, tk.END)
    e1.insert(0, '#ff0000')
def cheat2():
    l1['text'] = "orange"
    e1.delete(0, tk.END)
    e1.insert(0, "#FF8000")
def cheat3():
    l1['text'] = "yellow"
    e1.delete(0, tk.END)
    e1.insert(0, "#ffff00")
def cheat4():
    l1['text'] = "green"
    e1.delete(0, tk.END)
    e1.insert(0, "#00ff00")
def cheat5():
    l1['text'] = "blue"
    e1.delete(0, tk.END)
    e1.insert(0, "#00bfff")
def cheat6():
    l1['text'] = "light blue"
    e1.delete(0, tk.END)
    e1.insert(0, "#0000ff")
def cheat7():
    l1['text'] = "purple"
    e1.delete(0, tk.END)
    e1.insert(0, '#800080')
l1.place(anchor='center')
l1.pack()
e1.pack()
but = tk.Button(width=100,command=cheat,  bg='#ff0000').pack()
but2 = tk.Button(width=100,command=cheat2, bg='#FF8000').pack()
but3 = tk.Button(width=100,command=cheat3, bg='#ffff00').pack()
but4 = tk.Button(width=100,command=cheat4, bg='#00ff00').pack()
but5 = tk.Button(width=100,command=cheat5, bg='#00bfff').pack()
but6 = tk.Button(width=100,command=cheat6, bg='#0000ff').pack()
but7 = tk.Button(width=100,command=cheat7, bg='#800080').pack()

root.mainloop()