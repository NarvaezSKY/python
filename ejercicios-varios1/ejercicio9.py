# vegetariana=
# pimenton y tofu

# no vegetariana=
# peperoni, jamon y salmon

# mozarella y tomate siempre

pizza=input("elige tu pizza: ")

if pizza=="vegetariana":
    ingrediente=input("elige el ingrediente extra, pueden ser pimenton o tofu: ")

elif pizza=="no vegetariana":
    ingrediente=input("elige el ingrediente extra, pueden ser peperoni, jamon o salmon: ")

else:
    print("que")


print("tu pizza es ", pizza, " y lleva los ingredientes mozarella, tomate y ", ingrediente)