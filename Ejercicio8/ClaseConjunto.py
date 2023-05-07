class Conjunto:
    __conjunto=set() #Creo un atributo que sera un set(conjunto)
    def __init__(self, lista):  #traigo una lista con lo elementos que tendra el set
        self.__conjunto = set(lista) #Hago el casteo de lista a un set
    
    def getConjunto(self):  # Retorno los elementos del set
        return self.__conjunto

    def __add__(self,otroConjunto):                                              #Otra manera con el operador:  "|"
        return Conjunto( self.__conjunto.union( otroConjunto.getConjunto() ) ) #MiConjunto( self.__conjunto | ( otroConjunto.getConjunto()) 
    
    def __sub__(self,otroConjunto):
        return Conjunto( self.__conjunto - otroConjunto.getConjunto())  #SOBRECARGA DE OPERADOR " - " 
    
    def __eq__(self, otroConjunto):                                    #SOBRECARGA DE IGUALDAD  " == "
        return  ( self.__conjunto == otroConjunto.getConjunto())    #Como devuelve un booleando no hace falta crear una instacia de la clase