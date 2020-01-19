 class carro():
    ##PROPIEDADES

    #largo=250
    #ancho=120
    #ruedas=4
    #enmarcha=False
    
    #2° ESTADO INICIAL -> comentar lo de arriba
        
    #Constructor 
    def __init__(self):
        self.largo=250
        self.ancho=120
        self.__ruedas=4
        self.enmarcha=False
    
    
    ##MÉTODOS
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        
        if(self.enmarcha):#Parte del True
            return "El carro is en marcha"
        else:
            return "El carro is detenido"
    
    def datos(self):#Método de impresión
        print("El coche tiene", self.__ruedas, "ruedas.")
        print("Un ancho de ", self.ancho)
        print("Un largo de ", self.largo)
  
##DECLARACIÓN O INSTANCIA 
carro1 = carro() 
print(carro1.arrancar(True))#AGREGAR EL PARAMETRO
carro1.datos()


#3° ESTADO INICIAL -> comentar lo de arriba
carro2 = carro() 
print(carro2.arrancar(True))
carro2.ruedas=2#HAY QUE ENCAPSULAR -> HACERLO PRIVADO O INACCESIBLE - Evidentemente ya no hace nada 
carro2.datos()


#REFLEXIÓN HACER DE MÉTODOS MODIFICADORES - SETTERS
