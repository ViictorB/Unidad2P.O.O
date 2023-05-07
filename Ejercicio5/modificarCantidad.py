import PlanAhorro

def modificarCantidad(lista,codigo):
    band=True
    i = 0
    while (band == True) and (i < len(lista)):
        if codigo == lista[i].getCodigo():
            print("Cuota Actual pagas para liciar vehiculo: ", lista[i].getCuotasMinimasPagas())
            nuevo = input("Ingrese el nuevo valor: ")
            lista[i].setCuotasMinimasPagas(nuevo)
            print("Valor modificado con exito!")
            band = False
        else:
            i+=1
    if band == True:
        print("No se encontro el codigo del plan ingresado!")
        