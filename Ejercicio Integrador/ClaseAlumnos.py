#********CLASE ALUMNOS (ARREGLOS)********
class Alumnos:
    __dni = ""
    __apellido = ""
    __nombre = ""
    __carrera = ""
    __añoCarrera = 0
    def __init__(self,dni,apell,nomb,carrera,año):
        self.__dni = dni
        self.__apellido = apell
        self.__nombre = nomb
        self.__carrera = carrera
        self.__añoCarrera = int(año)
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getCarrera(self):
        return self.__carrera
    def getAñoCarrera(self):
        return self.__añoCarrera
    
    def __gt__(self,otro):
        return Alumnos("","","","",self.__añoCarrera > otro.getAñoCarrera)