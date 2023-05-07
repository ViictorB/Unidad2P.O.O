import ClaseAlumnos as cs
import numpy as np
import csv

class ManejadorAlumnos:  #MANEJADOR ARREGLO
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self):
        self.__alumnos=np.empty(20,dtype=cs.Alumnos)
    def CargarAlumnos(self):
        archivo = open("Actividades\\Ejercicio Integrador\\alumnos.csv")
        reader = csv.reader(archivo,delimiter=";")
        band = True
        for i in reader:
            if band:
                band = False
            else:
              dni = i[0]
              apell = i[1]
              nomb = i[2]
              carrera = i[3]
              año = i[4]
              objeto = cs.Alumnos(dni,apell,nomb,carrera,año)
              if self.__cantidad == self.__dimension:
                  self.__dimension += self.__incremento
                  self.__alumnos.resize(self.__dimension)###????
              self.__alumnos[self.__cantidad] = objeto
              self.__cantidad +=1
        print("Arreglo Cargado Con exito!")
    
    def compararDNI(self,dni):
        band = True
        for i in range(self.__cantidad):
            if dni == self.__alumnos[i].getDni():
                indice = i
                band = False
        if band:
            aux = "Error"
        else:
            aux = self.__alumnos[indice].getDni()
        return aux

    def BuscarDni(self, dni):
        for i in range(self.__cantidad):
            if self.__alumnos[i].getDni() == dni:
               return i
           
    def obtenerListOrdenadaApelldo(self):
        listaOrdenada=[]
        for i in range(self.__cantidad):
            listaOrdenada.append([self.__alumnos[i].getApellido(),self.__alumnos[i].getNombre()])
        return listaOrdenada
             
    
    def getNombre(self,indice):
        return self.__alumnos[indice].getNombre()
    
    def getApellido(self,indice):
        return self.__alumnos[indice].getApellido()
    
    def getAño(self,indice):
        return self.__alumnos[indice].getAñoCarrera()
    