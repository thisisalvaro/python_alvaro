#Conditions

#elif
flag=True
flag2=False

if flag:
    print("Flag is true")
elif flag:
    print("Flag2 is flase")
else: 
    print("Flag is flase")

print("match (switch) case")
match "Python":
    case "Python":
        print("Python es un lenguaje de programacion")
    case "Java":
        print("Java es un lenguaje de programacion")
    case "C++":
        print("C++ es un lenguaje de programacion")
    case _: #el _ es el default de java
        print("No se reconoce el lenguaje")


#Loops
    #for
for item in range(1,100):
    if item % 2 == 0: #si es par no se imprime lo siguiente
        continue
    if item ==9: #si es 9 que se salga del bucle
        break
    print(item)
else: #xd
    print("Loop is done")

    #while Loop
count = 0
while count <10 :
    print(count)
    count += 1