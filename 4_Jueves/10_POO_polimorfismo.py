class Coche():
    
    def desplazamiento(self):
        print("Movimiento en 4 ruedas")
                
class Moto():
    
    def desplazamiento(self):
        print("Movimiento en 2 ruedas")        
        
class Tractor():
    
    def desplazamiento(self):
        print("Movimiento en 10 ruedas")

#Primera parte
"""
miVe1=Moto()
miVe1.desplazamiento()

miVe2=Coche()
miVe2.desplazamiento()

miVe3=Tractor()
miVe3.desplazamiento()
"""

#POLIMORFISMO -> generalizar
def desplazamientoVehiculo(vehiculo):#Función que recibe un objeto
    vehiculo.desplazamiento()#No sabemos que tipo de objeto

#Debido al polimorfismo, el objeto puede cambiar de forma dependiendo de forma


objPoli=Tractor()
desplazamientoVehiculo(objPoli)

#Poner caso de archivos de reproducción de música

