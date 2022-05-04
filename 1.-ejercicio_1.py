#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%
#Escribe un programa que comience leyendo el número de barras vendidas que no son del día
#Después tu programa debe mostrar el precio habitual de una barra de pan
#el descuento que se le hace por no ser fresca y el coste final total.


barrasvendidasañejas = int(input("Ingrese el numero de barras vendidas que no son del dia:"))
print("El precio habitual de una barra de pan es de 3.49€")
print("las barras de pan del dia anterior tiene un descuento de 60%")
barrasvendidasañejascondescuento =str (barrasvendidasañejas * 0.60)
print("el coste final € " + barrasvendidasañejascondescuento + " Euros")


