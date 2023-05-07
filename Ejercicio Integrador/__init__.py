import ClaseAlumnos
import ClaseMateria
import ManejadorMaterias as mM
import ManejadorAlumnos as mA
import Menu as m1
                         
if __name__ == "__main__":
   arreglo = mA.ManejadorAlumnos()    
   arreglo.CargarAlumnos()
   listaaa = mM.ManejadorMaterias()
   listaaa.CargarMaterias()
   m1.menu(arreglo,listaaa)
   
   