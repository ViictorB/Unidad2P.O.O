#CLASE Email
class Email: 
    def __init__(self, idCuenta, dominio, tipoDominio, contraseña): #Atributos
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña
     
     #METODOS                          
    def retornaEmail(self):
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}"
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self, Correo,contra):
        if (Correo.count("@") and (Correo.count("."))):
           partes = Correo.split("@")
           idCuenta, dominio_entero = partes
           dominio_partes = dominio_entero.split(".")
           if (len(partes) != 2) and (len(dominio_partes) != 2):
               print("Dirección de correo invalida.")
               return
           dominio, tipoDominio = dominio_partes
           self.__idCuenta = idCuenta
           self.__dominio = dominio
           self.__tipoDominio = tipoDominio
           self.__contraseña = contra
           print("Cuenta creada con exito!")
        else:
            print("Direccion de correo invalida")
   
    def modificarContraseña(self, contraseñaActual, nuevaContraseña):
        if self.__contraseña == contraseñaActual:
            self.__contraseña = nuevaContraseña
            print("Contraseña modificada con exito!")
        else:
            print("Contraseña actual incorrecta!. No se pudo modificar la contraseña.")
            