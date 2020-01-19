from tkinter import *

pant1= Tk()#Preguntarles 7u7r
pant1.title("Hola Mundo")
pant1.resizable(True,True)#Ancho - width y largo - height
pant1.iconbitmap("favicon.ico")
pant1.geometry("650x315")
pant1.config(bg="Blue")


'''
#Frame -> Cuadro interno -> Ir de linea a linea
frame1 = Frame()

#frame1.pack()
#frame1.pack(side="bottom")#side="left" #side="bottom"
#frame1.pack(side="right", anchor="")#Anchor -> puntos cardinales en inglés
'''
#TclError: ambiguous anchor "": must be n, ne, e, se, s, sw, w, nw, or center


'''
frame1.pack(fill="y")#redimensiona en x pero no en y
#frame1.pack(fill="y",expand="True")
#frame1.pack(fill="both",expand="True")#HABLAR DE LA RESPONSIVIDAD

frame1.config(bg="red")
frame1.config(width="650", height="350")#Mencionar que es importante hacer este
pant1.geometry("850x400")#-> Nuevo tamaño
#Mencionar los parametros de pack()

'''
#SEGUNDA PARTE
pant1.geometry("850x400")#NOTA SUBIR ESTA LINEA EN LA SECCIÓN

frame1 = Frame()
frame1.pack()
frame1.config(bg="red")
frame1.config(width="650", height="350")
#BORDE
frame1.config(bd=35)#tamaño de borde
frame1.config(relief="groove")
frame1.config(cursor="hand2")#="pirate"

##MOSTRAR QUE ESTOS ÚLTIMOS CONFIG EN LA PANTALLA O RAIZ

#pant1.config(bd=35)#tamaño de borde
#pant1.config(relief="groove")
#pant1.config(cursor="pirate")#="pirate"
#Preguntar por qué el mainloop() no se usa en pant1


pant1.mainloop()#Al final para sacar toda la raíz 

