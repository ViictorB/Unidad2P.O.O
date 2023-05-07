import ManejadorAlumnos
import ManejadorMaterias

def MostrarLisOrdenado(arreglo, lista):
    ListPorApell = arreglo.obtenerListOrdenadaApelldo()
    ListPorApell.sort()
    print("Listado de Alumnos Ordenados Alfabeticamente: ")
    for i in range(len(ListPorApell)):
        print(ListPorApell[i])
