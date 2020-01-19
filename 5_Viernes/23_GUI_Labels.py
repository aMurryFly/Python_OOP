from tkinter import *

pant=Tk()
frame1= Frame(pant)
frame1.pack()

#Pantalla=====================================

pantalla=Entry(frame1)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)#NO HACER SPOILER
pantalla.config(background="white", fg ="black", justify="right")
             
#FILA 1 ======================================
boton7 = Button(frame1, text="7", width=3)
boton7.grid(row = 2, column=1)    

boton8 = Button(frame1, text="8", width=3)
boton8.grid(row = 2, column=2)

boton9 = Button(frame1, text="9", width=3)
boton9.grid(row = 2, column=3) 

botonMul = Button(frame1, text="x", width=3)
botonMul.grid(row = 2, column=4)

#Instrucción -> colspan -> diseño web en Pythn columnspan
#Dar a entender que la pantalla queremos que ocupe varias columnas            

#FILA 2 ======================================
boton4 = Button(frame1, text="4", width=3)
boton4.grid(row = 3, column=1)    

boton5 = Button(frame1, text="5", width=3)
boton5.grid(row = 3, column=2)

boton6 = Button(frame1, text="6", width=3)
boton6.grid(row = 3, column=3) 

botonMen = Button(frame1, text="-", width=3)
botonMen.grid(row = 3, column=4)

#FILA 3 ======================================
boton1 = Button(frame1, text="1", width=3)
boton1.grid(row = 4, column=1)    

boton2 = Button(frame1, text="2", width=3)
boton2.grid(row = 4, column=2)

boton3 = Button(frame1, text="3", width=3)
boton3.grid(row = 4, column=3) 

botonMas = Button(frame1, text="+", width=3)
botonMas.grid(row = 4, column=4)

#FILA 3 ======================================
boton0 = Button(frame1, text="0", width=3)
boton0.grid(row = 5, column=1)    

botonPunto = Button(frame1, text=".", width=3)
botonPunto.grid(row = 5, column=2)

botonIgual = Button(frame1, text="=", width=3)
botonIgual.grid(row = 5, column=3) 

botonDivi = Button(frame1, text="/", width=3)
botonDivi.grid(row = 5, column=4)


pant.mainloop()








