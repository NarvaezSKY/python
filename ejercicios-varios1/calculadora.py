activo=1
while activo==1:
    condicional=int(input('ingresa la operacion. 1. Suma 2. Resta 3.Multiplicación 4.En tu culo mi aparato ajskdajsd: '))

    if condicional==1:
        valor1=int(input("ingresa el valor 1: "))
        valor2=int(input("ingresa el valor 2: "))

        valor3=valor1+valor2
        print(valor3)

    elif (condicional==2):
        valor1=int(input("ingresa el valor 1: "))
        valor2=int(input("ingresa el valor 2: "))

        valor3=valor1-valor2
        print(valor3)

    elif (condicional==3):
        valor1=int(input("ingresa el valor 1: "))
        valor2=int(input("ingresa el valor 2: "))

        valor3=valor1*valor2
        print(valor3)

    elif (condicional==4):
        valor1=int(input("ingresa el valor 1: "))
        valor2=int(input("ingresa el valor 2: "))

        valor3=valor1/valor2
        print(valor3)

    else:
        print("sexo")

