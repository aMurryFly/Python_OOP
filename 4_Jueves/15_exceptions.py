def evalEdad(edad):
    if edad < 0:
        #raise TypeError("Valor no válido")
        #Es un tipo de exception (Mensaje propio)
               
        #Estamos especificando que tipo de error es
        #raise ZeroDivisionError("Valor no válido")
                
        raise ErrorPropio("Valor no válido")#<- esto es una clase D:

        #Podemos definir nuestros propios errores pero también nos manda
        #->NameError: name 'ErrorPropio' is not defined
    
    if edad <20:
        return "Parvulito*"
    elif edad <40:
        return "Eres joven"
    elif edad < 65:
        return "Damn man, :("
    elif edad < 100:
        return "Chabelo D: ?"

print(evalEdad(-18))#(evalEdad(-18))

#Especificar que realmente lo que quiero es mostrarles otro caso común

