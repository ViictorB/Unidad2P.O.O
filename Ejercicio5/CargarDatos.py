import csv
import PlanAhorro as clase

def CargarDatos(lista):
    archivo = open("Actividades\\Ejercicio5\\planes.csv")
    reader = csv.reader(archivo, delimiter= ";")
    for i in reader:
       codigo = i[0]
       modelo = i[1]
       version = i[2]
       valor = i[3]
       cuotasPlan = i[4]
       cuotasMinPagas = i[5]
       un_dato = clase.PlanAhorro(codigo,modelo,version,valor)
       un_dato.setCanCuotasPlan(cuotasPlan)
       un_dato.setCuotasMinimasPagas(cuotasMinPagas)
       lista.append(un_dato)
    print("Lista cargada con exito!")