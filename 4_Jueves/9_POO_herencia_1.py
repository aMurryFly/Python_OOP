class person():
    
    def __init__(self,nombre,edad,lugResi):
        self.name = nombre
        self.age=edad
        self.place=lugResi
        
    def datos(self):    
        print("Nombre: ", self.name, "\nEdad: ", self.age, "\nResidencia: ", self.place )


class employee(person):
    
    def __init__(self,salario,antiguedad):
        
        #super().__init__("Alfonso",21,"CDMX")#Pero estos son valores fijos (No debemos hacer esto)
        self.salario=salario
        self.antiguedad=antiguedad

     
        
#person1 = person("Alfonso",21,"CDMX")  
#person1.datos()     
        
  
#person1 = employee("Alfonso",21,"CDMX") #No funciona debido a la prioridad del constructor
person1 = employee(1500,13) #Mostar que incluso el otro constructor si funciona pero el método datos no
person1.datos()      
 
#Utilizar la función "super" <-PUNTUALIZAR (ir a linea 15)
'''
 
##SEGUNDA PARTE
class employee(person):
    
    def __init__(self,salario,antiguedad,nameEmpleado,ageEmpleado,resEmpleado):
        
        super().__init__(nameEmpleado,ageEmpleado,resEmpleado)#Constructor padre
        self.salario=salario
        self.antiguedad=antiguedad 
    
    #Sobreescribir el método datos
    def datos(self):
        super().datos()
        #Agregamos lo del employee
        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad )
        

person1 = employee(1500,13,"Alfonso",21,"CDMX") 
person1.datos()

#PRINCIPIO DE SUSTITUCIÓN

#-> es un o una -> un EMPLEADO es siempre una PERSONA
#               -> una PERSONA no siempre es una PERSONA

# isinstance() - Función para comprobar este principio (Devuelve false o true)

print(isinstance(person1,employee))#Pensar sobre todo ya hay muchas herencias (person1,person))



person2 = person("Alfonso",21,"CDMX") 
person2.datos()
print(isinstance(person2,employee))#Pensar sobre todo ya hay muchas herencias (person1,person))
'''       