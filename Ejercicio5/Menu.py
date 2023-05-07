import PlanAhorro
import modificarValor as m1
import mostrarCuotasMinimas as m2
import modificarValor as m3
import modificarCantidad as m4
import mostrarOpciones as m5



def Menu(lista):
    m5.mostrarOpciones()
    op=str(input("Ingrese una opcion->> "))
    while(op != "0"):
        if (op == "a"):
            indice=int(input("Ingrese el elemento a modificar del (1 al {}):  ".format(len(lista))))
            if (indice <= len(lista) and indice > 0):
                m1.modificarValor(lista,indice)
            else:
                print("Numero Ingresado Incorrecto!")
        elif (op == "b"):
            m2.mostrarCuotasMinimas(lista)
        elif (op == "c"):
            indice=int(input("Ingrese un elemento de los planes registrados del (1 al {}):  ".format(len(lista))))
            if (indice <= len(lista) and indice > 0):
                print("El monto para liciar vehiculo es: $", (lista[indice-1].getCuotasMinimasPagas() * lista[indice-1].importeCuota()))
            else:
                print("Numero Ingresado Incorrecto!")
        elif (op == "d"):
            cod = str(input("Ingrese un codigo de plan: "))
            m4.modificarCantidad(lista,cod)
        else:
            print("Opcion Incorrecta!")
        m5.mostrarOpciones()
        op=str(input("Ingrese una nueva Opcion->> "))
    print("Finalizando.....")