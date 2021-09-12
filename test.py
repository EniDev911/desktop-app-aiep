from tkinter import *


def validate_entry(text):
	return text.isalpha() 

w = Tk()
w.config(width=300, height=200)
w.title('Validate Entry')
e = Entry(validate='key', 
	validatecommand=(w.register(validate_entry), "%S"))
e.place(x=50, y=50, width=150)
w.mainloop()

