from functools import reduce

def sum(value1:int,value2):
    return value1+value2

print(sum(1,2))
#print(sum("hola",2)) #el tipado debil es muy xd

#lambda
substract = lambda value1 ,value2 : value1-value2
multiply_2= lambda value1 : value1*2

my_list = [1,2,3,4,5]
print(list(map(multiply_2 , my_list))) #map es un metodo que recibe una funcion y un lista y devuelve un nuevo lista con los resultados de la funcion
                                        #con map a la funcion no le pasas el parametro que quieres que devuelva sino que map lo pasa por si
print(list(filter(lambda value1 : value1 % 2==0, my_list))) #filter es un metodo que recibe una funcion y un lista y devuelve un nuevo lista con los elementos que cumplen la condicion
print(reduce(lambda value1 , value2 : value1 + value2 , my_list)) # reduce es un metodo que recibe una funcion y un lista y devuelve un solo valor



#classes
class Person:
    def __init__(self,name,age):
        self._name = name  #el _ delante de name es una variable protected
        self.age = age
        self.__phone_number = 123456789 #__phone_number es una variable privada
        #no hay visibilidad de variable pero con eso podemos decirle al desarrollador que variables no se pueden acceder directamente
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_info(self):
        return f"Name: {self.name} Age: {self.age}"

#Herencia
class contacto :
    def __init__(self,name,age):
        self.namecontact = name
        self.agexontact = age
  

class Student(Person , contacto): #para decir que herede de Person tenemos que poner entre parentesis la clases
    def __init__(self,name,age):
        super().__init__(name,age)
        self.school = "MIT"

my_student = Student("Alvaro",30)
print(my_student.get_info())
print(my_student.get_name())
print(my_student.get_age())
print(my_student.phone_number)
print(my_student.school)
