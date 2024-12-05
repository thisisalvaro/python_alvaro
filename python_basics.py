print("Hola mundo")
''' hola gei 
'''
"""
esto es otro comentario
"""

# tipos de variables
print("Tipos de variabñes")
print(type(print))
print(type(1))
print(type(1.2))
print(type("hola"))
print(type(True))
print(type("hola" [0]))

'''variables'''
print("---Variables---")

name = "Borja"
print(type(name))

name=30
print(type(name))

print("forzar variables -- no sirve de nada xd")
age : int = 9
print(type(age))
age="Borja"
print(type(age))

print("Recoger valores por pantalla")
id = input("¿que id quieres añadir?")
print(id)

'''string '''
print("---String cosos---")

product_name = "manzanas"
quantity = 10
# En python no pueden concatenar un int con un string y para ello hay varias formas de cambiarlo
print("Ha comprado" + str(quantity) + " " + product_name)
print("Ha comprado {}{}".format(quantity,product_name) )
print("Ha comprado %d %s" %(quantity,product_name) )
print(f"Ha comprado {quantity} {product_name}")


print("String caracteres")
address = "calle de la fantasia n13 4ºD" 
print(address[0])
print(address[2:6])
print(address[2:])
print(address[:6])
print(address[-2])
print(address[::-1]) #al reves todo

print("String funciones")
print(address.upper())
print(address.capitalize())
print(address.count("t"))
print(address.isnumeric())
print(address.lower())
print(address.startswith("ca"))
print("Py" == "Py")
print("hola" > "hola")
print("x2" *2)