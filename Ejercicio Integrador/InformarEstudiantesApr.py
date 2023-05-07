import ManejadorAlumnos as mA
import ManejadorMaterias as mM

#Funcion
def InformarAprobados(arreglo,lista):
    materia=str(input("Ingrese una Materia:")) #pido la materia
    nuevaLista = lista.buscarMaterias(materia) #busco si existe esa materia
    if len(nuevaLista) != 0: #verifico si lo encontro o no para hacer el proceso
        for i in range(lista.tamaño()): 
            if lista.getAprobacion(i) == "P" and lista.getNota(i) >= 7 and materia == lista.getMateria(i): #condicion
                indice=arreglo.BuscarDni(lista.getDni(i)) 
                print("{} {} {} {} {} {}".format(lista.getDni(i),arreglo.getApellido(indice), arreglo.getNombre(indice), lista.getFecha(i), lista.getNota(i), arreglo.getAño(indice)))
    else:
        print("No se encontro ese tipo de Nombre de materia.")