#Funci�n sobre cargada
#for i in range(10):   
#for i in range(0,10):  
#for i in range(0,10,2):     
#    print(i)
 
#Python es un lenguaje de tipado din�mico (esto es, no se indica el tipo de dato de un objeto al declararlo).    
"""
class persona{

     String nombre;
     int edad;

     /* El constructor de la clase Usuario4 esta sobrecargado */
     persona( ){
        nombre = null;
        edad = 0;
        direccion = null;
     }

     persona(String nombre, int edad, String direccion){
        this.nombre = nombre;
        this.edad = edad;
        this.direccion = direccion;
     }


     void setNombre(String n){
        nombre = n;
     }

     String getNombre(){
        return nombre;
     }

     /* El metodo setEdad() est� sobrecargado */
     void setEdad(int e){
        edad = e;
     }

     void setEdad(float e){
        edad = (int)e;
     }

     int getEdad(){
        return edad;
     }
}

"""    

class person():
    
    def __init__(self,nombre,edad):
        self.name = nombre
        self.age=edad
        self.vidaFather=0
        self.vidaMother=0
        
    def promVida(self,vidaFather):#SOBRECARGAR UN MÉTODO 
        self.vidaFather=vidaFather
        vidaProm=(self.age + vidaFather)/2
        print("Tu vida será: ", vidaProm)
        
    def promVida2(self,vidaFather,vidaMother):
        self.vidaFather=vidaFather
        self.vidaMother=vidaMother
        vidaProm=(self.age + vidaFather + vidaMother)/3
        print("Tu vida será: ", vidaProm)    
        
person1=person("Alfonso",20)
person1.promVida2(40,20)
