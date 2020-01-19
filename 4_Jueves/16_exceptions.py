import math 

def calRoot(num1):
    if num1 <0:
        raise ValueError("El número no puede ser negativo aquí") 
    else:
        return math.sqrt(num1)

#Menu
        
op1=int(input("Ingrese valor: ")) 
print(calRoot(op1)) 

print("Espero llegar aquí :(")    

#AQUÍ PODEMOS VER COMO USAR EL TRY Y EXCEPT OTRA VEZ
try:
    print(calRoot(op1)) 
except ValueError as ErrorDeValorNegativo:#Sirve sobre todo para no confundir
    print(ErrorDeValorNegativo)


print("Espero llegar aquí :(") 

#MOSTRAR EL LINK DE DOCUMENTATION

#https://docs.python.org/3/tutorial/errors.html


