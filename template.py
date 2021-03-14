from tkinter import *
from tkinter import ttk
from tkinter.ttk import Label, Style
import tkinter.font as tkFont

import time

import LIST as lang
import roles


def myClick():
	answer = ans1.get("1.0", END)
	print(answer)
	if 'Enter Your name' in answer:
		return
	else:
		hello = 'Hello, ' + answer
		#myLabel = Label(root, text=hello)
		#myLabel.place(x=270, y=120)
		ans2.config(state="normal")
		ans2.delete("1.0", END)
		ans2.insert(INSERT, hello)


def click():
	answer = ans1.get("1.0", END)
	src = combobox1.get()
	dst = combobox2.get()
	temp = ''
	#print(src, dst)

	if src == '':
		src = "Auto"

	if dst == '':
		dst = "Auto"

	result, org, arr = roles.translate(answer, src, dst)
	global description, process

	if org == None:
		pass
	elif src == 'Auto':
		

		description.destroy()
		process.destroy()

		temp = org + " → " + arr
		description = Label(root, text=temp, justify='center')
		description.grid(row=4, column=1)

		temp = org + "\nis\ndetected"
		process = Label(root, text=temp, justify='center')
		process.grid(row=5, column=1)
	else:
		description.destroy()

		temp = org + " → " + arr
		description = Label(root, text=temp, justify='center')
		description.grid(row=4, column=1)

	ans2.config(state='normal')
	ans2.delete("1.0", END)
	ans2.insert("1.0", result)
	ans2.config(state='disabled')

                                         


root = Tk()
root.geometry("590x390")
root.title('GooPAPA: Translator')


style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )


#msgbox = Tk()
#msgbox.geometry("400x400")

title_style = ttk.Style(root)
title_style.configure("Title.Label", font=('Arial', 25))
Label(root, text="GooPAPA: Translator", style="Title.Label").grid(row=0, columnspan=3)

combobox1 = ttk.Combobox(root, values = lang.LANGUAGES)
combobox1.grid(row=1, column=0, padx=10, pady=10)

combobox2 = ttk.Combobox(root, values = lang.LANGUAGES)
combobox2.grid(row=1, column=2, padx=10, pady=10)

entry_style = ttk.Style(root)
entry_style.configure("Entry.Msg", font=("Courier", 15, "italic"))


ans1 = Text(root, borderwidth=3, width=20, height=10, font=("서울남산체", 15, "italic"))
#ans1.place(x=20, y=70)
ans1.grid(row = 2, column=0, padx=10, pady=10, rowspan=5)
ans1.insert("1.0", "Enter Your name")
#ans1 = tkFont.Font(family='Courier', size=15, slant='italic')
#ans1.grid(row=0, column=0)
#ans1.pack()

ans2 = Text(root, borderwidth=3, width=20, height=10, font=("서울남산체", 15, "italic"))
#ans2.place(x=420, y=70)
ans2.insert("1.0", "Result")
ans2.config(state="disabled")
ans2.grid(row=2, column=2, padx=10, pady=10, rowspan=5)
#ans2.pack()
#ans = Entry(root, width=50, height=100, bg='red', fg='white')

myButton = ttk.Button(root, text="Translate", style="C.TButton", command=click)
#myButton.place(x=270, y=70)
myButton.grid(row=3, column=1)
#myButton = Button(root, text="Click!!", style="C.TButton", command=myClick, fg="white", bg="black")
#myButton.pack()

"""

Implement HERE!!!

"""


root.mainloop()





"""
def loading():
	for i in range(1, 6):
		txt = "Loading" + "."*i
		inform2 = Label(root, text=txt).grid(row=9, column=0, padx=10, sticky='sw')
		time.sleep(1)

loading()
"""


#https://digiconfactory.tistory.com/141
