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


class Camioneta(Vehiculos):
    
    def cargar(self,cargar):
        self.cargado=cargar
        
        if(self.cargado):
            return "Está cargada"
        else:
            return "No está cargada"
        

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Sobre una rueda"
        
    #Sobre escribir un método -> imprimir     
    def imprimir(self):
        print("Marca: ", self.marca, "\nModelo", self.modelo)
        print("En marcha: ", self.enmarcha, "\nAcelerando:", self.acelera)#Mostrar que no tiene sentido agregar el caballito
        print("Frenando: ", self.frena)
        print(self.hcaballito)

#Otra clase
class VElectricos(Vehiculos):#Mencionarles acerca del constructor vacío y declarado
    
        def __init__(self,marca,modelo):
            super().__init__(marca,modelo)
            self.autonomia=100
            self.cargado=False
        
        def cargarEnergia(self):
            self.cargado=True
    
    
class BicicletaElectrica(VElectricos,Vehiculos):
    pass

#Tercer objeto
bici1=BicicletaElectrica("Marca","Modelo")
bici1.imprimir()


