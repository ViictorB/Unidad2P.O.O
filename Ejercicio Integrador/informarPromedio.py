import ManejadorAlumnos
import ManejadorMaterias

#Funcion
def informarPromedio(arreglo,lista):
    Dni = str(input("Ingrese el DNI de un alumno:"))
    DniABuscar=arreglo.compararDNI(Dni)
    if DniABuscar != "Error":
        lista.buscarNotas(DniABuscar)
    else:
        print("No se encontro el DNI Ingresado")