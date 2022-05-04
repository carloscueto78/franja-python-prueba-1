#Escribir un programa que le pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años
#muestre por pantalla el capital obtenido en la inversión redondeado a dos decimales.


invertir = int(input("Ingrese la cantidad a invertir:"))
interesporcentual = int(input("Ingrese el interes porcentual anual:"))
numerodeaños = int(input("Ingrese el numero de años:"))
capital =str((invertir * ((interesporcentual/100)+1))**numerodeaños)
capital2 =round(capital, 2)
capital2 =str(capital2)
print("La capital obtenida es:" + capital)
