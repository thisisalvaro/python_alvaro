# Errores 

# SyntaxError
#   print hola
# IndentationError
# NameError
    #name="hola"
    #print(nm)
# TypeError
# IndexError
# KeyError
# ValueError
# AttributeError
# IOError
# OSError
# LookupError


    #Exceptions
my_dict ={"name":"Alvaro","age":30}

try:
    print(my_dict["name"])
except KeyError as e:
    print("Key not found",e)
else :
    print("No error")
finally:
    print("finally")
