import random
maquina=random.string("priedra","papel","tijera")
eleccion=input("Ingresa tu eleccion: ")


            
if eleccion==maquina: 
    print("empate. Eleccion maquina:", maquina)  

elif eleccion=="tijera" and maquina=="papel":
        print("ganas. Eleccion maquina:", maquina)  
        
elif eleccion=="tijera" and maquina=="piedra":
        print("pierdes. Eleccion maquina:", maquina)  
        
elif eleccion=="papel" and maquina=="piedra":
        print("ganas. Eleccion maquina:", maquina) 

elif eleccion=="papel" and maquina=="tijera":
        print("pierdes. Eleccion maquina:", maquina)
        
elif eleccion=="piedra" and maquina=="tijera":
        print("ganas. Eleccion maquina:", maquina) 
        
elif eleccion=="piedra" and maquina=="papel":
        print("pierdes. Eleccion maquina:", maquina)    
    
else:
    ("opción invalida")
        
