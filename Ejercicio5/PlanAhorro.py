class PlanAhorro:
    __cantCuotasPlan=24            #Variable de clase
    __cuotasMinimasPagas= 6        #Variable de clase
    __codigo=0          
    __modeloVehiculo=""            #Variables de instancias
    __versionVehiculo= ""
    __valorVehiculo= 0
    def __init__(self, codigo,modelo,version,valor):  #Contructor
        self.__codigo = codigo
        self.__modeloVehiculo = modelo
        self.__versionVehiculo = version
        self.__valorVehiculo = int(valor)
    
    #*********Metodos de Clase (cls) Funciones de Miembros Estaticas*********
    @classmethod
    def getCantCuotasPlan(cls):
        return cls.__cantCuotasPlan
    
    @classmethod
    def getCuotasMinimasPagas(cls):
        return cls.__cuotasMinimasPagas    
    
    @classmethod
    def mostrar(cls):
        print("Cantidad de cuotas del plan: {} y la cantidad de cuotas minimas pagadas para liciar el vehiculo son: {}".format(cls.getCantCuotasPlan(), cls.getCuotasMinimasPagas())) 
    
    @classmethod
    def setCanCuotasPlan(cls,nuevo):
        cls.__cantCuotasPlan = int(nuevo)
        
    @classmethod
    def setCuotasMinimasPagas(cls,nuevo):
        cls.__cuotasMinimasPagas = int(nuevo)
        
        
        
    #***********Metodos de Instancias (self)*********
    def getCodigo(self):
        return self.__codigo
    
    def getModeloVehiculo(self):
        return self.__modeloVehiculo
    
    def getVersionVehiculo(self):
        return self.__versionVehiculo
    
    def getValorVehiculo(self):
        return self.__valorVehiculo
    
    def importeCuota(self):
        return float((self.__valorVehiculo / self.__cantCuotasPlan) + self.__valorVehiculo * 0.10)
    
    def setValorVehiculo(self,nuevo):
        self.__valorVehiculo = nuevo