# -*- coding: utf-8 -*-
from tkinter import *

#frames
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

#configurando layout do frame 
frame.option_add('*Font', 'tahoma 20 bold')
frame.master.title('Simple Calculator')
frame.pack(expand = NO, fill = BOTH)

#display
display = Entry(frame, bd = 5, justify='right', font="tahoma")
display.pack(side = LEFT)

#botoes
clearButton = Button(frame, text="C", font="tahoma", fg="blue", command = lambda: display.delete(0,"end"))
clearButton.pack(side=LEFT)

equalButton = Button(bottomframe, text="=", font="tahoma", command = lambda: avaliar_eq(display))
equalButton.pack(side=LEFT)

def avaliar_eq(display):
	text=eval(display.get())
	display.delete(0,"end")
	display.insert(0,text)
	
root.mainloop()