def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2


def divide (num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError: #catch en otros lenguajes
        print("Abogado verdad ?")
        return "Operación errónea" 
	
try:       
    op1=(int(input("Introduce el primer número: ")))
    op2=(int(input("Introduce el segundo número: ")))
except ValueError:
    print("Valors ingresados incorrectamente")

'''
while True: # Uso de ciclos infinitos
    try:       
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))
        break#rompemos el ciclo con esto (forzamos)
    
    except ValueError:
        print("Valors ingresados incorrectamente. \nIngreselos otra vez\n")
'''

##Flujo del programa no tendrá los datos necesario
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