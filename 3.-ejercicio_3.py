#Escribir un programa que haga transformaciones de pesos a dólares
#Debe preguntarle al usuario si desea transformar de pesos mexicanos a dólares
#de pesos chilenos a dólares, o desde pesos argentinos a dólares.
#Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares
#Peso Chileno a dólar: 855
#Peso Mexicano a dólar: 20
#Peso Argentino a dólar: 115

print("""Seleccione la moneda desde la cual convertir  a dolares:
1 peso chileno
2 peso mexicano
3 peso argetino""")
opcion = int(input("ingrese la opcion: "))
dinero = int(input("Ingrese la capital a convertir: "))

if opcion == 1:
    tipo_cambio = "pesos chilenos"
    cambio = 855
    dolares = dinero / cambio
    dolares = round(dolares, 2)
elif opcion == 2:
    tipo_cambio = "Pesos mexicanos"
    cambio = 20
    dolares = dinero / cambio
    dolares = round(dolares, 2)
elif opcion ==3:
    tipo_cambio = "pesos argentinos"
    cambio = 115
    dolares = dinero / cambio
    dolares = round(dolares, 2)
    print("convirtio " + str(dinero) + " " + tipo_cambio + " a dolares y el total es: " + str(dolares))

    
















