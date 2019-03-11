# -*- coding: utf-8 -*-
from tkinter import *
import subprocess

#a tela foi dividida em dois frames, onde os botoes devem ser distribuidos
root = Tk()				
root.iconbitmap('bolt.ico')		
frame = Frame(root,width=100, height=100)  
frame.pack()
bottomframe = Frame(root,width=100, height=200)
bottomframe.pack( side = BOTTOM )

#====Frame Layout====#
frame.option_add('*Font', 'tahoma 20 bold')
frame.master.title('Simple Calculator')
frame.master.title('Simple Calculator')		#título da janela
frame.pack(expand = NO, fill = BOTH)

#display
#====Exibir Display====#
display = Entry(frame, bd = 5, justify='center', font="tahoma")
display.pack(padx=30, pady=20, side=LEFT)

#botoes
#====Limpar o Display====#
#lambda permite o uso de variaveis locais em outras partes do programa
clearButton = Button(bottomframe, text="C", font="tahoma", fg="blue", command = lambda: display.delete(0,"end")) 
clearButton.pack(padx=10, pady=0, side=RIGHT)

#====Exibir Resultado====# 
equalButton = Button(bottomframe, text="=", font="tahoma", command = lambda: avaliar_eq(display))
equalButton.pack(side=LEFT)

einButton = Button(bottomframe, text="1", font="tahoma", command = lambda: display.insert("end","1"))
einButton.pack(side=LEFT)
zweiButton = Button(bottomframe, text="2", font="tahoma", command = lambda: display.insert("end","2"))
zweiButton.pack(side=LEFT)
dreiButton = Button(bottomframe, text="3", font="tahoma", command = lambda: display.insert("end","3"))
dreiButton.pack(side=LEFT)


#====Executar um .bat====#
open_expButton = Button(bottomframe, text="rodar .bat", font="tahoma", command = lambda: subprocess.call(['open_explorer.bat']))
open_expButton.pack(side=LEFT)

 
def avaliar_eq(display):
	text=eval(display.get())
	display.delete(0,"end")
	display.insert(0,text)
	text=eval(display.get()) #interpreta o que esta escrito no display (eval()) e salva o resultado em uma variavel 
	display.delete(0,"end")  #limpa o display
	display.insert(0,text)   #insere no display o resultado obtido anteriormente

root.mainloop() 