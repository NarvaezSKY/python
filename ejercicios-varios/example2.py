numero=int(input("ingresa el numero"))

condicion=numero%1
condicion2=numero%numero

if condicion == 0 or condicion2 == 0:
    print("el numero ", numero, "es primo")

else:
    print("el numero no es primo")

