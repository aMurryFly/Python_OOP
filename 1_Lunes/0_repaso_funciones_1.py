def suma1Var(var1, var2):
    print("El resultado es: ", var1+ var2)

def suma2Var(var1, var2):
    resultado=var1+ var2
    return resultado

def sumaArre(numbers):
    result=0
    for number in numbers:
        result += number
    print(result)    
    
#Parte del main o sólo declaración
    
num1=float(input("Ingrese valor: "))
num2=float(input("Ingrese valor: "))
suma1Var(num1,num2)

resul=suma2Var(num1,num2)
print(resul)
  
#Arreglo 
sumaArre([4,5])
  