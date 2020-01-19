def divide():
    '''
    op1=float(input("Ingrese valor: "))
    op2=float(input("Ingrese valor: "))
    print("El valor es " + str(op1/op2))
    print("It's done")
    #puntualiza que lo que haremos es hacer exceptions de otra forma
    '''
    try:
        op1=float(input("Ingrese valor: "))
        op2=float(input("Ingrese valor: "))
        print("El valor es " + str(op1/op2))
    
    except ValueError:
        print("El valor introducido no es válido")
        
    except ZeroDivisionError:
        print("No se puede dividir entre 0 ")
    
    print("It's done")

    #QUÉ PASA SI HAY MUCHÍSIMAS EXCEPCIONES ? -> Forma genérica (No usar)
    
    #except:
    #   print("Something wrong has happened")
    
    #finally:#-> Usar sin el except
    #  print("It's done")

    
    
    '''
    Caso 1 -> se hace el try y además el finally
    Caso 2 -> no se hace el try , damos algún except y además el finally
    Caso 3 -> se tiene el try y además el finally
               -> se hace el try  e independiente de si está bien o no lo 
               que se hace entramos al finally 
               
    try siempre debe llevar ya sea un except o un finally           
    '''
divide()    
    




