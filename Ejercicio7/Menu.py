import ClaseViajero
import BuscarMayorCantMillas as m1

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
               print("a - Consultar cantidad de millas")
               print("b - Acumular millas")
               print("c - Canjear millas")
               print("d - Mostrar Viajero/s con mayor millas acumuladas: ")
               print("e - Comparar cantidad de millas ")
               print("")
               op=input("Ingrese una opción: ")
               if(op=="a"):
                   print(Lista[i].cantidadTotalMillas())
               elif(op=="b"):
                   millas=int(input("Ingrese cantidad de millas para acumular: ")) 
                   suma = millas + Lista[i] #operamos al reves ahora
                   Lista[i].setMillas(suma.cantidadTotalMillas())       
                   print("Millas en total: ", Lista[i].cantidadTotalMillas())
               elif(op=="c"):
                   millas=int(input("Ingrese la cantidad de millas a canjear: "))
                   if (millas <= Lista[i].cantidadTotalMillas()):
                       resta = millas  - Lista[i]#
                       print("Millas restantes: ", resta.cantidadTotalMillas())
                       Lista[i].setMillas(resta.cantidadTotalMillas())
                   else:
                       print("Cantidad de millas insuficientes para canjear")
               elif(op =="d"):
                    m1.BuscarMayorCantMillas(Lista)
               elif(op == "e"):
                   num1=int(input("Ingrese un numero: "))
                   num2=int(input("Ingrese otro numero: "))
                   print("El numero {} es Igual que {}? ".format(num1, Lista[i].cantidadTotalMillas()), num1 == Lista[i]) 
                   print("El numero {} es Igual que {}?  ".format(num2, Lista[i].cantidadTotalMillas()), Lista[i] == num2)
               else:
                   band = True
                   print("Finalizando...")
        else:
            i+=1
                