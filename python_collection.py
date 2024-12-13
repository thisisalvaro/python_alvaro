#Todas heredas de iterable


#Lista (mutable , ordenado y permite duplicados)

my_list = [0,1,2,3,"hola",True, 1.2]
print(type(my_list)) #es un tipo de dato
my_list.append(5)
print(my_list)
#.pop() lo elimina y te lo devuelve 
x= my_list.pop()
print(my_list)
print(x)
#eliminamos uno en concreto
my_list.pop(1)
print(my_list)


#definimos de otra manera
my_other_list =list()
my_other_list.append(1)
print(my_other_list)

#funcion clave del sistema que podemos utilizar en este caso en las listas
print(len(my_list))


#Accesos
print(list[0])
print(list[-1]) #del reves no empieza en 
print(my_list.count("hola"))

#insert-> inserta en una posicion pero no rempleza el valor sino que lo pone entre medias de
my_list.insert(2,"adios")
print(my_list)

#cambiar datos
my_list[0] = 5

#eliminar
my_list.remove("hola") #-> eliminame el primer elemento hola
del my_list[0] #elimname la posicion 0

#Tuplas no puedes modificar ni agregar ni insertar ni nadaa 
print("TUPLAS")
my_tuple = (1,2,3,4,"hola",True,1.2)
my_tuple= tuple()

#para poder modificarla hay que pasarla a una lista
my_list= list(my_tuple)


#Sets -> no esta ordenado se va desordenando todo el rato . sirve para poder añadir informacion pero que no va a estar repetida -> No se añaden repetidos
print("")
my_set = {1,2,3,4} #si no ponemos nada entre las llaves dice que es un diccionario xdddd
my_other_set =set()
print(type(my_other_list))

#no repetible
my_set.add(6)
my_set.add(6)
my_set.add(6)
print(my_set)

#Dictionary -> es mutable
my_dicctionary = {"name" : "Alvaro" , "age" :30 ,"its_student": Flase}

print(type(my_dicctionary))
#como acceder -> pues por el id como en los hashmap baby
print(my_dicctionary["name"]) #no se puede acceder por posicion bb
print("name" in my_dicctionary) #si esa clave esta en el diccionado devuelve false
my_dicctionary["name"] = "Pepe"

#diferentes formas de acceder (listas)
print(my_dicctionary.keys)
print(my_dicctionary.values)
