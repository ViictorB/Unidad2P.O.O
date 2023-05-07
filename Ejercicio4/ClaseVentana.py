class Ventana:
    __titulo = ""
    __izqX = 0
    __izqY = 0
    __derX = 0
    __derY = 0

    def __init__(self, titulo="", izqX=0, izqY=0, derX=500, derY=500):
        self.__titulo = titulo
        self.__izqX = izqX
        self.__izqY = izqY
        self.__derX = derX
        self.__derY = derY

    def mostrar(self):
        print("Ejes Izquierdos: ({},{}) Ejes Derechos: ({},{})".format(
            self.__izqX, self.__izqY, self.__derX, self.__derY))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return self.__izqY

    def ancho(self):
        return self.__derX
    
    def moverDerecha(self,mover):
        nuevo = mover + self.__izqX
        if nuevo <= 500:
            self.__izqX += mover
        else:
            print("No es posible moverse a la derecha!")

    def moverIzquierda(self,mover):
        nuevo = self.__izqX - mover
        if nuevo <= 0:
            self.__izqx -= mover
        else:
            print("No es posible moverse a la izquierda")

    def bajar (self,mover):
        nuevo = self.__izqY - mover
        if nuevo <= 500:
            self.__izqX -= mover
        else:
            print("No es posible Bajar!")
        
    def subir (self,mover): 
        nuevo =self.__izqY + mover
        if nuevo >=0:
            self.__izqY += mover
        else:
            print("No es posible Bajar!")