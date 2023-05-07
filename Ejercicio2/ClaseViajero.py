class ViajeroFrecuente:
    __num_viajero=0
    __dni=""
    __nombre=""
    __apellido=""
    __millasacum=0

    def __init__(self, num, dni, nombre, ape, millas):
        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=ape
        self.__millasacum=int(millas) 
    def getnum(self):
        return self.__num_viajero
    
    def cantidadTotalMillas(self):
        return self.__millasacum
    
    def acumularMillas(self, cant):
        self.__millasacum+=int(cant) 
        return self.__millasacum
    
    def canjearMillas(self,cant):
        self.__millasacum-=int(cant)
        return self.__millasacum
    
    def __str__(self):
        return ("Num: {} DNI: {} Nombre: {} Apellido: {} millas: {}".format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millasacum))
    