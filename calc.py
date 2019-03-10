# -*- coding: utf-8 -*-
from tkinter import *

#a tela foi dividida em dois frames, onde os botoes devem ser distribuidos
root = Tk()							
frame = Frame(root)  
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

#====Frame Layout====#
frame.option_add('*Font', 'tahoma 20 bold')
frame.master.title('Simple Calculator')		#título da janela
frame.pack(expand = NO, fill = BOTH)

#====Exibir Display====#
display = Entry(frame, bd = 5, justify='right', font="tahoma")
display.pack(side = LEFT)

#====Limpar o Display====#
#lambda permite o uso de variaveis locais em outras partes do programa
clearButton = Button(frame, text="C", font="tahoma", fg="blue", command = lambda: display.delete(0,"end")) 
clearButton.pack(side=LEFT)

#====Exibir Resultado====# 
equalButton = Button(bottomframe, text="=", font="tahoma", command = lambda: avaliar_eq(display))
equalButton.pack(side=LEFT)


def avaliar_eq(display):
	text=eval(display.get()) #interpreta o que esta escrito no display (eval()) e salva o resultado em uma variavel 
	display.delete(0,"end")  #limpa o display
	display.insert(0,text)   #insere no display o resultado obtido anteriormente
	
root.mainloop()