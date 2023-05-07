import ClaseViajero as cviajero
import csv

def LeerArchivos(lista):
    archivo=open("Actividades\\Ejercicio2\\Viajeros.csv")
    reader=csv.reader(archivo,delimiter=";")
    bandera=True
    for i in reader:
        if bandera:
            bandera=False
        else:
            num=i[0]
            dni=i[1]
            nombre=i[2]
            ape=i[3]
            millas=i[4]
            viajero=cviajero.ViajeroFrecuente(num, dni, nombre, ape, millas)
            lista.append(viajero)
    archivo.close()