import informarPromedio as m1
import InformarEstudiantesApr as m2
import MostrarListadoOrdenado as m3


def menu(arre,list):
    print("************Menu de Opciones**************")
    print("a - Informar Promedio de Alumno")
    print("b - Informar Estudiantes que aprobaron una Materia")
    print("c - Mostrar Ordenado Listado de alumnos")
    print("0 - Finalizar Operancion")
    print("**************************************")
    op=str(input("Ingrese una opcion--->"))
    while op != "0":
        if op == "a":
            m1.informarPromedio(arre,list)
        elif op == "b":
            m2.InformarAprobados(arre,list)
        elif op == "c":
            m3.MostrarLisOrdenado(arre,list)
        else:
            print("Opcion Incorrecta")
        if op != "0":
           print()
           print("************Menu de Opciones**************")
           print("a - Informar Promedio de Alumno")
           print("b - Informar Estudiantes que aprobaron una Materia")
           print("c - Mostrar Ordenado Listado de alumnos")
           print("0 - Finalizar Operancion")
           print("**************************************")
           op=str(input("Ingrese una opcion--->"))
    print("Finalizando...")