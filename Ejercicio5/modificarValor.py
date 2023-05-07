import PlanAhorro

def modificarValor(lista, i):
    print("Codigo del plan: {} Modelo: {} Version: {}".format(lista[i-1].getCodigo(), lista[i-1].getModeloVehiculo(), lista[i-1].getVersionVehiculo())) 
    valor=int(input("Ingrese el nuevo valor del vehiculo: "))
    lista[i-1].setValorVehiculo(valor)
    print("Nuevo valor '{}' modificado con exito!".format(lista[i-1].getValorVehiculo()))