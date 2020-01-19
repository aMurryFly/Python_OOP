class avion():
  
    #Constructor 
    def __init__(self):
        self.__alas=2
        self.__ruedas=3
        self.__volar=False
    
    
    ##MÉTODOS
    def arrancar(self,arrancamos):
        self.__volar=arrancamos
        if (self.__volar):
            chequeo= self.checkingState()
            #chequeo= self.__checkingState()
        
        if(self.__volar and chequeo):#Se toma por default que sea verdadero
            return "it's flying"
        elif(self.__volar and chequeo == False):
            return "Something wrong, warning"
        else:
            return "it is n't flying"
    
    def datos(self):
        print("El airplane tiene", self.__ruedas, "ruedas.")
        print("El airplane tiene", self.__alas, " alas.")
        
        
        #Método no encapsulado -> se llama desde donde sea 
    def checkingState(self):#AGREGAR DESPUÉS LA LINEA EN ARRANCAR
        
    #def __checkingState(self):#Método ya encapsulado, cambiarlo en donde se llama   
        print("Realizando Checking")
        self.combustible="ok"
        self.puerta="close"
        
        if(self.combustible =="ok" and self.puerta == "close"):
            return True
        else: 
            return False
        
  
##DECLARACIÓN O INSTANCIA 
avion1 = avion() 
print(avion1.arrancar(True))
avion1.datos()
#print(avion1.checkingState())#MOstrar que se puede llamar desde afuera de la clase 

print("____________________")
avion2 = avion() 
print(avion2.arrancar(False))
avion2.datos()
#print(avion2.checkingState())#MOstrar que se puede llamar desde afuera de la clase 


#MOSTRAR CUANDO EN CHECKINGSTATE combustible "mal"

