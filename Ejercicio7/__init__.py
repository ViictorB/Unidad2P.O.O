# ---****Ejercicio 7  VB  -  POO****---
import sys
import ClaseViajero as cviajero
import LeerArchivo as m1
import Menu as m2

if __name__=="__main__":
    Lista=[]
    m1.LeerArchivos(Lista)
    m2.Menu(Lista)
    print("Cantidad de referencias: ", sys.getrefcount(cviajero))