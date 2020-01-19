import threading # Antes se llama thread
import time
import datetime


#POSTERIORMENTE DEFINIR QUE HACE CADA FUNCIÓN
def consultar(id_persona):
    time.sleep(2)
    return 
    
def guardar(id_persona, data):
    time.sleep(5)
    return
    
'''   
tiempo_ini = datetime.datetime.now()
#Declaración de un hilo

#Nombre, el objetivo y los parametros -> el parámetro es una tupla
t1 = threading.Thread(name="hilo_1", target=consultar,args=(1,))
t2 = threading.Thread(name="hilo_2", target=guardar,args=(1,"let's go"))

t1.start()
t2.start()

tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido: " + str(tiempo_fin.second - tiempo_ini.second))

'''


'''
#1 - EJEMPLIFICAR CON LO SIGUIENTE PARA EXPLICAR EL 0 

tiempo_ini = datetime.datetime.now()
tiempo_fin = datetime.datetime.now()

consultar(1)
guardar(1,"Qué pasó ?")
print("Tiempo transcurrido: " + str(tiempo_fin.second - tiempo_ini.second))

#2 - COMENTAR LOS CONSULTAR Y GUARDAR

#HILO PRINCIPAL -> HILOS SECUNDARIOS

'''   
tiempo_ini = datetime.datetime.now()
#Declaración de un hilo

#Nombre, el objetivo y los parametros -> el parámetro es una tupla
t1 = threading.Thread(name="hilo_1", target=consultar,args=(1,))
t2 = threading.Thread(name="hilo_2", target=guardar,args=(1,"let's go"))

t1.start()
t2.start()

#Paralelizamos ambos procesos y es por ello que ya no es dependiente del hilo principal
t1.join()
t2.join()

tiempo_fin = datetime.datetime.now()

print("Tiempo transcurrido: " + str(tiempo_fin.second - tiempo_ini.second))

    





