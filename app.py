import random

valor=random.randint(0,100)
valoru=int(input("ingresa el numero: "))



while valor!=valoru:

    if valoru>valor:
        print("Fallaste! el numero ingresado es mayor")
        valoru=int(input("ingresa el numero: "))
    elif valoru<valor:
        print("Fallaste! el numero ingresado es menor")
        valoru=int(input("ingresa el numero: "))
    
if valor==valoru:
     
     print("encontraste el numero, era", valor)