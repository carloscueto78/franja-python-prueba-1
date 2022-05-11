#Escribir un programa que le pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años
#muestre por pantalla el capital obtenido en la inversión redondeado a dos decimales.


invertir = float(input("Ingrese la cantidad a invertir:"))
interesporcentual = float(input("Ingrese el interes porcentual anual:"))
numerodeaños = int(input("Ingrese el numero de años:"))
capital =str((invertir * ((interesporcentual/100)+1))**numerodeaños)
capital = round(capital, 2)
print("La capital obtenida es:" + str(capital))

