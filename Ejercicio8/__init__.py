import ClaseConjunto as cl
import Menu as m1
    
if __name__ == "__main__":              
   A = cl.Conjunto([1,2,3,4])
   B = cl.Conjunto([3,6,9])
   C = cl.Conjunto([1,4,3,2])
   m1.Menu(A,B,C)

   #print(A.getConjunto() + B.getConjunto()) # NO se puede hacer esto
   # suma = A + B
   # print("La Suma es: ", suma.getConjunto())
   # resta = A - B
   # print("La Resta es: ", resta.getConjunto())
   # Iguales = A == C
   # print("Son iguales A y C :", Iguales)
