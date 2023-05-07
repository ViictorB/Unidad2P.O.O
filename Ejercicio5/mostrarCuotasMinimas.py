import PlanAhorro

def mostrarCuotasMinimas(lista):    
    valor=float(input("Ingrese un valor de cuota Maxima: "))
    i = 0
    band = True
    print("Datos de los Planes cuyo importe de cuota es menor a {} son: ".format(valor))
    while i < len(lista):
        if valor > lista[i].importeCuota():
            print("Codigo del plan: ", lista[i].getCodigo())
            print("Modelo: ", lista[i].getModeloVehiculo())
            print("Version del vehiculo: ", lista[i].getVersionVehiculo())
            print()
            band = False
        i+=1
    if band:
        print("ERROR: No se encontraron planes con importes de cuotas minimos al ingresado!")