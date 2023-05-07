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
    
    def setMillas(self,otro):
        self.__millasacum = int(otro)
        
    def acumularMillas(self, cant):
        self.__millasacum+=int(cant) 
        return self.__millasacum
    
    def canjearMillas(self,cant):
        self.__millasacum-=int(cant)
        return self.__millasacum
    
    def __gt__(self,otro):
        return self.__millasacum > otro.cantidadTotalMillas()

    def __eq__(self,otro): # ==
        return self.__millasacum == otro
    
    def __req__(self,otro): # == (reverse)
        return self.__millasacum == otro
    
    #def __add__(self,otro):
        #return ViajeroFrecuente(0,"","","",self.__millasacum + otro)

    #def __sub__(self,otro):
        #return ViajeroFrecuente(0,"","","",self.__millasacum - otro)
    
    def __radd__(self,otro): #suma reverse
        return ViajeroFrecuente(0,"","","",self.__millasacum + otro)
    
    def __rsub__(self,otro): #resta reverse
        return ViajeroFrecuente(0,"","","",self.__millasacum - otro)
    
    