# ---****Ejercicio 2  VB  -  POO****---

import ClaseViajero as cviajero
import LeerArchivo as m1
import Menu as m2

def test():
    objetoPrueba = cviajero.ViajeroFrecuente(1999,"213131", "Juan", "Dias", 233)
    print("Objeto de Prueba:")
    print(objetoPrueba)
    print()
if __name__=="__main__":
    Lista=[]
    test()
    m1.LeerArchivos(Lista)
    m2.Menu(Lista)
