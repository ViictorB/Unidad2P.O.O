import ClaseConjunto
import MenudeOpciones as m1

def Menu(Con1,Con2,Con3):
    m1.MenudeOpciones()
    op=int(input("Ingrese una opcion --> "))
    print()
    while op != 0:
        if op == 1:
            print("Conjunto A = {}".format(Con1.getConjunto()))
            print("Conjunto B = {}".format(Con2.getConjunto()))
            print("Conjunto C = {}".format(Con3.getConjunto()))
            
        elif op == 2:
            c1=str(input("Ingrese el primer conjunto a operar: "))
            c2=str(input("Ingrese el segundo conjunto a operar: "))
            if (c1 == "A" or c1=="B" or c1=="C") and (c2=="A" or c2=="B" or c2=="C"):
                if (c1 == "A" and c2 == "B") or (c1 == "B" and c2 == "A"):
                    suma = Con1 + Con2
                    print("La Suma entre A y B es: ", suma.getConjunto())
                elif (c1 == "A" and c2 == "C") or (c1 == "C" and c2 == "A"):
                    suma = Con1 + Con3
                    print("La Suma entre A y C es: ", suma.getConjunto())
                elif (c1 == "B" and c2 == "C") or (c1 == "C" and c2 == "B"):
                    suma = Con2 + Con3
                    print("La Suma entre B y C es: ", suma.getConjunto())
            else:
                print("Error en Selecionar los Conjuntos!")
                
        elif op == 3:  
            c1=str(input("Ingrese el primer conjunto a operar: "))
            c2=str(input("Ingrese el segundo conjunto a operar: "))
            if (c1 == "A" or c1=="B" or c1=="C") and (c2=="A" or c2=="B" or c2=="C"):
                if c1 == "A" and c2 == "B":
                    resta = Con1 - Con2
                    print("La Resta entre A y B es: ", resta.getConjunto())
                elif c1 == "A" and c2 == "C":
                    resta = Con1 - Con3
                    print("La Resta entre A y C es: ", resta.getConjunto())
                elif c1 == "B" and c2 == "C":
                    resta = Con2 - Con3
                    print("La Resta entre B y C es: ", resta.getConjunto())
                elif c1 == "B" and c2 == "A":
                    resta = Con2 - Con1
                    print("La Resta entre B y A es: ", resta.getConjunto())
                elif c1 == "C" and c2 == "A":
                    resta = Con3 - Con1
                    print("La Resta entre C y A es: ", resta.getConjunto())
                elif c1 == "C" and c2 == "B":
                    resta = Con3 - Con2
                    print("La Resta entre C y B es: ", resta.getConjunto())
                       
        elif op == 4:
            c1=str(input("Ingrese el primer conjunto a operar: "))
            c2=str(input("Ingrese el segundo conjunto a operar: "))
            if (c1 == "A" or c1=="B" or c1=="C") and (c2=="A" or c2=="B" or c2=="C"):
                if (c1 == "A" and c2 == "B") or (c1 == "B" and c2 == "A"):
                    print("Son Iguales los Conjuntos A y B: ", Con1 == Con2)
                elif (c1 == "A" and c2 == "C") or (c1 == "C" and c2 == "A"):
                    print("Son Iguales los Conjuntos A y C: ", Con1 == Con3)
                elif (c1 == "B" and c2 == "C") or (c1 == "C" and c2 == "B"):
                    print("Son Iguales los Conjuntos B y C: ", Con2 == Con3)
            else:
                print("Error en Selecionar los Conjuntos!")
        else:
            print("Opcion Incorrecta!")
        if op != 0:
           m1.MenudeOpciones()
           op=int(input("Ingrese una nueva opcion --> "))
           print()
    print("Finalizando......")