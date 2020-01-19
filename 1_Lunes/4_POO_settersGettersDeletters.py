

class Empleado:
    def __init__(self,first,last):
        self.first = first
        self.last= last
        self.email= first + '.' + last + '@email.com'#Quitar al agregar la propiedad - property#Agregar 2°
    
    '''@property    
    def email(self):
         return '{}.{}@email.com'.format(self.first,self.last)'''
     
    #@property    
    def fullname(self):
         return '{}{}'.format(self.first,self.last)
      
        
#Instancias

emp1 = Empleado('John', 'Smith')
#emp1.first = 'Jim'#Agregar 2°

print(emp1.first)         
print(emp1.email)
#print(emp1.email())
print(emp1.fullname())
#print(emp1.fullname) 

"""


###SECOND PART    
class Empleado:
    
    def __init__(self,first,last):
        self.first = first
        self.last= last
    
    @property    
    def email(self):
         return '{}.{}@email.com'.format(self.first,self.last)
     
    @property   # -> Getter 
    def fullname(self):
         return '{}{}'.format(self.first,self.last)     
     
    @fullname.setter    
    def fullname(self,name):
         first, last = name.split(' ')
         self.first = first
         self.last= last
         
    @fullname.deleter    
    def fullname(self):
         print("It was deleted!")
         self.first = None
         self.last= None     
         
emp1 = Empleado('John', 'Smith')

emp1.fullname = 'Alfonso Murrieta'        
         
print(emp1.first)         
print(emp1.email)
print(emp1.fullname)
 
#Forma de llamarlo 
del emp1.fullname

"""

         
        
        