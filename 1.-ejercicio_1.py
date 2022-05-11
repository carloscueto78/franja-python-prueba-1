#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%
#Escribe un programa que comience leyendo el número de barras vendidas que no son del día
#Después tu programa debe mostrar el precio habitual de una barra de pan
#el descuento que se le hace por no ser fresca y el coste final total.


barrasvendidasañejas = int(input("Ingrese el numero de barras vendidas que no son del dia:"))
precio = 3.49
descuento = 0.6
descuento_porcentual = 0.6 * 100
coste = barrasvendidasañejas * precio * (1 - descuento)
print("precio de barra de pan: " + str(precio))
print("descuento de barra de pan no frescas: " + str(descuento_porcentual))
print("Coste final: " + str(round(coste, 2)))





