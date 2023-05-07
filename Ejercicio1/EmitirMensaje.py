import ClaseEmail as clase

def EmitirMensaje():
    nombre = input("Ingrese el nombre de la persona: ")
    direccionCorreo = input("Ingrese la dirección de correo: ")
    contra = input("Ingrese la contraseña: ")
    nuevo_objeto = clase.Email("", "", "", "")
    nuevo_objeto.crearCuenta(direccionCorreo,contra)
    print(f"Estimado {nombre}, te enviaremos tus mensajes a la dirección {nuevo_objeto.retornaEmail()}")
    return nuevo_objeto