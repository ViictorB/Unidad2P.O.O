import ClaseEmail as email

def CrearCuenta():
    Correo1 = "informatica.fcefn@gmail.com"
    objeto1 = email.Email("", "", "","")
    objeto1.crearCuenta(Correo1,"")
    print(f"Dirección de correo creada: {objeto1.retornaEmail()}")
    