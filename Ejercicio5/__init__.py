# ---****Ejercicio 5  VB  -  POO****---
import PlanAhorro
import CargarDatos as m1
import Menu as m2

if __name__=="__main__":
    #PlanAhorro.mostrar() #Verifico si existen las variables de clases (el mismo valor para todas las instancias)
    datos = []
    m1.CargarDatos(datos)
    m2.Menu(datos)