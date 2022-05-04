#Escribir un programa que haga transformaciones de pesos a dólares
#Debe preguntarle al usuario si desea transformar de pesos mexicanos a dólares
#de pesos chilenos a dólares, o desde pesos argentinos a dólares.
#Mostrar por pantalla la cantidad de monedas a convertir, la moneda que se convirtió y el monto en dólares
#Peso Chileno a dólar: 855
#Peso Mexicano a dólar: 20
#Peso Argentino a dólar: 115

print("1 de pesos mexicanos a dolares")
print("2 de pesos chilenos a dolares")
print("3 de pesos argentinos a dolares")
print ("")
hl=int(input("coloque aqui opcion"))
print ("")
if hl==1:
    pesm=int(input("introdusca cantidad de pesos mexicanos"))
    dol1=pesm*855
    print ("")
    print ("dolares=", pesm)
if hl==2:
    pesc=float(input("introdusca pesos chilenos"))
    dol2=pesc*20
    print("")
    print("dolares=", dol2)
if hl==3:
    pesa=int(input("introdusca cantidad de pesos argentinos"))
    dol3=pesa*1.18
    print("")
    print("dolares=", dol3)
    print("")
















