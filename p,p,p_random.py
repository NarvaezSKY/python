import random
maquina=random.randint(1,3)
if maquina == 1:
    maquina="piedra"
if maquina == 2:
    maquina="papel"
if maquina == 3:
    maquina="tijera"

opcion=int(input("ingresa tu eleccion: (1. Piedra - 2. Papel - 3. Tijera)"))

if opcion == 1 and maquina ==1:
        print("empate")
elif opcion == 2 and maquina ==2:
        print("empate")
elif opcion == 3 and maquina ==3:
        print("empate")
elif opcion==1  


        
