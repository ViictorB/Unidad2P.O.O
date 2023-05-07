# ---****Ejercicio 1  VB  -  POO****---
import ClaseEmail as clase
import EmitirMensaje as m1
import ModificarContraseña as m2
import CrearCuenta as m3
import LeerArchivos as m4
import ContarDominios as m5

def test():
    objeto=clase.Email("alumnogood","gmail","com","6682sdd21")
    print("Objeto de Prueba: ")
    print(objeto.retornaEmail())
    print()

if __name__ == "__main__":
    test()
    objeto = m1.EmitirMensaje()
    m2.ModificarContraseña(objeto)
    m3.CrearCuenta()
    m4.LeerArchivos()
    m5.ContarDominios()
    