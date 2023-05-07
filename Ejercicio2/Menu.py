import ClaseViajero

def Menu(Lista):
    NumViajero=input("Ingrese número de viajero: ")
    i = 0
    band = False
    op = ""
    while (band != True) and (i< len(Lista)):
        if NumViajero==Lista[i].getnum():
            band = True
            while op != "0" :
               print("")
               print("MENU DE OPCIONES:")
               print("0 - Finalizar operacion!")
               print ("a -Consultar cantidad de millas")
               print("b -Acumular millas")
               print ("c -Canjear millas")
               print("")
               op=input("Ingrese una opción: ")
               if(op=="a"):
                   print(Lista[i].cantidadTotalMillas())
               elif(op=="b"):
                   millas=input("Ingrese cantidad de millas para acumular: ")
                   print("Millas en total: ", Lista[i].acumularMillas(millas))
               elif(op=="c"):
                   millas=int(input("Ingrese la cantidad de millas a canjear: "))
                   if (millas <= Lista[i].cantidadTotalMillas()):
                       print("Millas restantes: ", Lista[i].canjearMillas(millas))
                   else:
                       print("Cantidad de millas insuficientes para canjear")
        else:
            i+=1
                