#********CLASE MATERIAS (LISTA)********     
class MateriasAprobadas:
    __dni = ""
    __nombre = ""
    __fecha = ""
    __nota = 0
    __aprobacion = ""
    def __init__(self,dni,nomb,fecha,nota,aprob):
        self.__dni = str(dni)
        self.__nombre = nomb
        self.__fecha = fecha
        self.__nota = int(nota)
        self.__aprobacion = aprob
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getFecha(self):
        return self.__fecha
    def getNota(self):
        return self.__nota
    def getAprobacion(self):
        return self.__aprobacion