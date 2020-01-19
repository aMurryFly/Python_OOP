class carro():
    ##PROPIEDADES
    largo=250
    ancho=120
    ruedas=4
    enmarcha=False
    
    ##MÉTODOS
    def arrancar(self):
        ##pass##MOSTRAR QUE HACE PASS
        self.enmarcha=True
    
    def estado(self):
        if(self.enmarcha):
            return "El carro is en marcha"
        else:
            return "El carro is detenido"
  
##DECLARACIÓN O INSTANCIA 
carro1 = carro() 

print(carro1.largo)       
print("El carro 1 tiene ",carro1.ruedas," ruedas")
carro1.arrancar()
print(carro1.estado())


carro2 = carro() 
print(carro2.largo)       
print("El carro 2 tiene ",carro2.ruedas," ruedas")
print(carro2.estado())
    
    
    
