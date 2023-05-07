import ClaseMateria as cs    
import csv    
    
class ManejadorMaterias:   #MANEJADOR LISTA
    def __init__(self):
        self.__lista=[]
        
    def CargarMaterias(self):
        archivo = open("Actividades\\Ejercicio Integrador\\materiasAprobadas.csv")
        reader = csv.reader(archivo,delimiter=";")
        band = True
        for i in reader:
            if band:
                band=False
            else:   
                dni = i[0]
                nombre= i[1]
                fecha = i[2]
                nota = i[3]
                aprobacion = i[4]
                objeto = cs.MateriasAprobadas(dni,nombre,fecha,nota,aprobacion)
                self.__lista.append(objeto)
        print("Lista Cargada con Exito!")
        
    def buscarNotas(self,dni):
        acum = 0
        contador= 0
        for i in range(len(self.__lista)):
            if dni == self.__lista[i].getDni():
                acum += self.__lista[i].getNota()
                print("Nota: ", self.__lista[i].getNota())
                contador+=1
        print("Promedio Total: ", acum / contador)
        
    def buscarMaterias(self,materia):
        listadeDni=[]
        for i in range(len(self.__lista)):
            if self.__lista[i].getNombre() == materia:
                listadeDni.append(self.__lista[i].getDni())
        return listadeDni
    
    def tamaño(self):
        return int(len(self.__lista))
    
    def getAprobacion(self,indice):
        return self.__lista[indice].getAprobacion()
        
    def getDni(self,indice):
        return self.__lista[indice].getDni()
    
    def getFecha(self,indice):
        return self.__lista[indice].getFecha()
    
    def getNota(self,indice):
        return self.__lista[indice].getNota()
    
    def getMateria(self,indice):
        return self.__lista[indice].getNombre()
                