def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

"""def divide(num1,num2):		
	return num1/num2
"""
def divide (num1,num2):
    try: # -> algo así como un if
        return num1/num2
    #-> algo así como un else
    except ZeroDivisionError: #catch en otros lenguajes
        print("Abogado verdad ?")
        return "Operación errónea" 
	#Y qué pasa si el error no fue de el tipo except que usamos ? D:
    #-> cae y muere directamente el programa

op1=(int(input("Introduce el primer número: ")))
op2=(int(input("Introduce el segundo número: ")))

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")

#Dividir entre 0 no es un problema o error de sintaxis o lógica 
#este tipo de error en tiempo de ejecución puede ser incluso externo    

#No sé está realizando esta linea
print("\nSoy una linea que quiere ser ejecutada :'v")
#IMAGINEMOS LINEAS VITALES DEL SISTEMA

'''
-> EXCEPCIONES

son errores que ocurrren durante la ejecución del programa

Traceback (most recent call last): -> Pila de llamas

    line 29
    line 11

exception del tipo:
    
ZeroDivisionError: division by zero    

##POR ÚLTIMO

Hacer ejemplo de meter un valor que no es entero en el input
ValueError: invalid literal for int() with base 10: 'das'
-> TODO LO METO EN UN MONTÓN DE TRY Y EXCEPT xd 

'''

