import ClaseEmail as clase
import csv

def ContarDominios():
    band = True
    archivos = open("Actividades\\Ejercicio1\\correos.csv")
    reader= csv.reader(archivos,delimiter=";")
    cont = 0
    TipoDominio = str(input("Ingrese un dominio a buscar: "))
    for i in reader:
        if band:
            band = False
        else:
            if TipoDominio == str(i[1]):
                cont += 1
    if cont > 0:
        print(f"El dominio ingresado {TipoDominio} aparece en {cont} direcciones de correo.")
    else:
        print("No se encontraron correos con ese dominio.")
    archivos.close  