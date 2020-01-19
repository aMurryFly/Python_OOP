class Vehiculos():
    
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True
            
    def frenar(self):
        self.frena=True
        
    def imprimir(self):
        print("Marca: ", self.marca, "\nModelo", self.modelo)
        print("En marcha: ", self.enmarcha, "\nAcelerando:", self.acelera)
        print("Frenando: ", self.frena)
        
#Clase hija
class Moto(Vehiculos):
    pass#Para mientras        

##INSTANCIAS 
moto1= Moto("Nissan", "Versa")
moto1.imprimir()       
        
        
            
