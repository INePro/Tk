from tkinter import *

class Block:
    def __init__(self, master):
        self.e = Entry(master, width=20)
        self.b = Button(master, text='Sort')
        self.l = Label(master, bg='black', fg='white', width=20)
        self.b['command'] = self.strToSortlist
        self.e.pack()
        self.b.pack()
        self.l.pack()

    def strToSortlist(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l['text'] = ' '.join(s)


if __name__ == '__main__':
    root = Tk()

    first_block = Block(root)
    root.mainloop()

