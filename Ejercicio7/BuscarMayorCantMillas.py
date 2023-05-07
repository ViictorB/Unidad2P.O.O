import ClaseViajero as clase

def BuscarMayorCantMillas(lista):
    
    # mayor = int(0)                 #OTRA FORMA DE RESOLVERLO
    # for i in range(len(lista)):
    #     if lista[i].cantidadTotalMillas() > mayor:
    #         mayor = lista[i].cantidadTotalMillas()
            
    # for i in range(len(lista)):
    #     if (lista[i].cantidadTotalMillas() == mayor):
    #         print("Viajero {} con {} millas acumuladas".format(lista[i].getnum(), lista[i].cantidadTotalMillas())
    
    #CON SOBRECARGA DE OPERADORES   > ,  ==
    mayor = clase.ViajeroFrecuente(0,"","","",0)
    for i in range(len(lista)):
       if ( lista[i] > mayor):
           mayor.setMillas(lista[i].cantidadTotalMillas())
       
    for i in range(len(lista)):
        if (lista[i] == mayor):
            print("Viajero {} con {} millas acumuladas".format(lista[i].getnum(), lista[i].cantidadTotalMillas()))
            