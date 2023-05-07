import ClaseEmail as clase
import csv

def LeerArchivos():
    band = True
    archivos = open("Actividades\\Ejercicio1\\correos.csv")
    reader= csv.reader(archivos,delimiter=";")
    for i in reader:
        if band:
            band = False
        else:
            nuevo = clase.Email("","","","")
            correo = nuevo.retornaEmail()
            contraseña=i[3]
            nuevo.crearCuenta(correo,contraseña)
    archivos.close  