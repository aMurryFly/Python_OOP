from tkinter import *

pant1= Tk()
#Varible hasta arriba por orden y por el flujo

frame1 = Frame(pant1,width=1200, height=600)
frame1.pack()
    
myname=StringVar() 
entryName=Entry(frame1, textvariable=myname)

#entryName=Entry(frame1)
entryName.grid(row=0, column=1,padx=10 , pady=10)
entryName.config(fg="Red",justify="right")

LabelName = Label(frame1,text="Nombre: ")
LabelName.grid(row=0, column=0,sticky="e",padx=10 , pady=10)

entryApell=Entry(frame1)
entryApell.grid(row=1, column=1,padx=10 , pady=10) 
LabelApell = Label(frame1,text="Apellido: ")
LabelApell.grid(row=1, column=0, sticky="e",padx=10 , pady=10)

entryCasa=Entry(frame1)
entryCasa.grid(row=2, column=1,padx=10 , pady=10) 
LabelCasa = Label(frame1,text="Dirección (Casa): ")
LabelCasa.grid(row=2, column=0, sticky="e",padx=10 , pady=10)

entryPass=Entry(frame1)
entryPass.grid(row=3, column=1,padx=10 , pady=10) 
entryPass.config(show="*")
LabelPass = Label(frame1,text="Password: ")
LabelPass.grid(row=3, column=0, sticky="e",padx=10 , pady=10)

TextComen=Text(frame1,width= 16, height = 5)
TextComen.grid(row=4, column=1,padx=10 , pady=10) 


LabelComen = Label(frame1,text="Comentario: ")
LabelComen.grid(row=4, column=0, sticky="e",padx=10 , pady=10)

scroll=Scrollbar(frame1, command=TextComen.yview)#Por si sólo no sale
scroll.grid(row=4, column=2,sticky="nsew")
TextComen.config(yscrollcommand=scroll.set)


#FUNCIÓN y variables
def codigoBoton():
    myname.set("Alfonso") 

#BOTÓN
#botonEnvi = Button(pant1, text="Enviar")
botonEnvi = Button(pant1, text="Enviar", command=codigoBoton)
#LLamar a una función-> evento
botonEnvi.pack()





pant1.mainloop()