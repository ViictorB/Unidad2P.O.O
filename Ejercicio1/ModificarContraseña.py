import ClaseEmail as email

def ModificarContraseña(objeto):
    contraseñaActual = input("Ingrese la contraseña actual: ")
    nuevaContraseña = input("Ingrese la nueva contraseña: ")
    objeto.modificarContraseña(contraseñaActual, nuevaContraseña)