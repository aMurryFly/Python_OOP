import threading 
import time
'''
def holaMundo():
    print("Hola Mundo")

if __name__ == '__main__':
    thread = threading.Thread(target=holaMundo)#Ejecutar sin iniciarlo
    thread.start()

'''
'''
#Parametros del constructor de Thread
def holaMundo(nombre):
    print("Hola Mundo "+nombre)

if __name__ == '__main__':
    thread = threading.Thread(target=holaMundo, args=("Alfonso", ))#Ejecutar sin iniciarlo
    thread.start()


'''
#2) Parametros del constructor de Thread
def holaMundo(nombre):
    print("Hola Mundo "+nombre)
    time.sleep(5)


if __name__ == '__main__':#Hilo principal
    thread = threading.Thread(target=holaMundo, args=("Alfonso", ))#Ejecutar sin iniciarlo
    thread.start()#Se hacen al mismo tiempo el principal y el otro
    #Por eso se imprimen al mismo tiempo los dos
    
    #thread.join()
    #Le dice al hilo principal que se detenga hasta que este hilo termine
    print("\nHola mundo desde el hilo principal")

