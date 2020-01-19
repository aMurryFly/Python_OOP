class perro():
    
    nombre = 'solovino'
    raza = 'cruza'
    edad = 5
    color = 'Negro'
    
    def setnombre(self):
        self.nombre = input("Ingresa el nombre de tu perro: ")
        
    def getnombre(self):#Getter o método que obtiene propiedad
        return self.nombre    
    
    def crecio(self):
        x = int(input("Cuántos años creció?: "))
        if(x >= 0 and x <= 15):
            self.edad  += x
        else:
            print("No te pases")

    def imprimirDatos(self):
        print("Nombre: ", self.nombre,"Raza: ", self.raza , "Edad: ",self.edad ,  "Color: ", self.color)
    
perro1 = perro()
perro1.setnombre()
perro1.crecio()
perro1.imprimirDatos()