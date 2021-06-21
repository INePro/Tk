from tkinter import *

root = Tk()
root.geometry("1000x1000")
root.title("hs")

Entry_1 = Entry(root)
Entry_1.grid(row = 0, column = 0)

Entry_2 = Entry(root)
Entry_2.grid(row = 0, column = 1)

def plus():
	one_chisl = Entry_1.get()
	two_chisl = Entry_2.get()
	if one_chisl.isdigit():
		if two_chisl.isdigit():
			result = float(one_chisl) + float(two_chisl)
			Label_res['text'] = result
		else:
			Label_res['text'] = 'Error'
	else:
		Label_res['text'] = 'Error'

def minus():
	one_chisl = Entry_1.get()
	two_chisl = Entry_2.get()
	if one_chisl.isdigit():
		if two_chisl.isdigit():
			result = float(one_chisl) - float(two_chisl)
			Label_res['text'] = result
		else:
			Label_res['text'] = 'Error'
	else:
		Label_res['text'] = 'Error'

def multioly():
	one_chisl = Entry_1.get()
	two_chisl = Entry_2.get()
	if one_chisl.isdigit():
		if two_chisl.isdigit():
			result = float(one_chisl) * float(two_chisl)
			Label_res['text'] = result
		else:
			Label_res['text'] = 'Error'
	else:
		Label_res['text'] = 'Error'
def diveded():
	one_chisl = Entry_1.get()
	two_chisl = Entry_2.get()
	if(float(one_chisl) == 0):
		Label_res['text'] = 'Error'
	else:
		if one_chisl.isdigit():
			if two_chisl.isdigit():
				result = float(one_chisl) / float(two_chisl)
				Label_res['text'] = result
			else:
				Label_res['text'] = 'Error'
		else:
			Label_res['text'] = 'Error'

B1 = Button(root, text = '+', width=16, height=3, command = plus)
B1.grid(row = 1, column = 0)

B2 = Button(root, text = '-', width=16, height=3, command = minus)
B2.grid(row = 1, column = 1)

B3 = Button(root, text = '*', width=16, height=3, command = multioly)
B3.grid(row = 2, column = 0)

B4 = Button(root, text = '/', width=16, height=3, command = diveded)
B4.grid(row = 2, column = 1)

Label_res = Label(root, text = '')
Label_res.grid(row = 1, column = 2)

root.mainloop()