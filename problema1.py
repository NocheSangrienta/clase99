def sumar_5_enteros():
    #definimos las variables
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0


    # Ingresamos los numeros:
    while contadorWhile < tamano:
        lista.append(int(input("ingrese numero " + str(contadorWhile+1) +": ")))
        contadorWhile +=1

    # sumamos los numeros:
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile +=1

    print("los elementos de la lista son:")
    for numero in lista:
        print(numero,end=', ')

        print("\nLa suma de todos sus elementos es:")
        print(suma)




