nota1=float(input("nota1: "))
nota2=float(input("nota2: "))
nota3=float(input("nota3: "))

calificacion=(nota1+nota2+nota3)
notafinal=calificacion/3
print (notafinal)

# print(calificacion)
if notafinal <3.0:
    final="no pasaste"  
elif notafinal >= 3.0 and calificacion <= 4.5:
    final="aprobado"
elif notafinal >=4.6 and calificacion <=5.0:
    final="excelente"
elif notafinal>5.0:
    final="invalido"
else:
    final="que"

print("tu nota fue: ", final)