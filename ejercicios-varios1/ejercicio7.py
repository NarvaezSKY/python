# 2400

puntuacion=float(input("puntuacion"))

if puntuacion==0.0:
    print("sos inaceptable y ganas ", 2400)

elif puntuacion==0.4:
    print("sos aceptable y ganas ", 2400*puntuacion)

elif puntuacion>=0.6:
    print("sos meritorio y ganas ", 2400*puntuacion)