# Autor: Luis Armando Miranda Alcocer
# Misión 8: Ejercicio con listas


def sumarAcumulado(lista):
    print("Ejercicio 1: ")
    sumaEnIndice=0  #Acumulador empieza en 0
    segundaLista=[] #Lista nueva
    for i in lista:  # 0, 1,2... Para cada valor en la lista
        sumaEnIndice += i   #Se irán sumando los numeros correspondientes a cada índice anterior
        segundaLista.append(sumaEnIndice)   #Se agrega cada uno en la lista nueva
    return(segundaLista)    #Regresa la lista nueva


def recortarLista(lista):
    print("Ejercicio 2: ")
    segundaLista=[] #Se crea una segunda lista
    for k in range(1,len(lista)-1): #En un rango desde el indice en la posición 1(inicia en 0), hasta la penúltima
        segundaLista.append(lista[k]) #Se agregan en la segunda lista
    return(segundaLista)


def estanOrdenados(lista):
    print("Ejercicio 3: ")
    for k in range(0, len(lista) - 1):
        if lista[k + 1] >= lista[k]:
            return(True)
        else:
            return(False)


def sonAnagramas():
    print("Ejercicio 4: ")
    palabra = input("Teclea palabra1: ")
    lista1 = list(palabra)
    palabra2 = input("Teclea palabra2: ")
    lista2 = list(palabra2)

    listaReversa=lista1
    listaReversa.reverse()
    if listaReversa == lista2:
        return True
    else:
        return False


def hayDuplicados(listaDuplicado):
    print("Ejercicio 5: ")
    contador= 0
    for k in range(0, len(listaDuplicado)):
        if listaDuplicado[k] == listaDuplicado[k+1]:
            return True
        else:
            return False


def borrarDuplicados(listaDuplicado):
    print("Ejercicio 6: ")
    pass


def main():
    lista=[1,2,3,4,5]

    primerFuncion= sumarAcumulado(lista)
    print(primerFuncion)
    print(" ")

    segundaFuncion= recortarLista(lista)
    print(segundaFuncion)
    print(" ")

    terceraFuncion= estanOrdenados(lista)
    print(terceraFuncion)
    print(" ")

    cuartaFuncion= sonAnagramas()
    print(cuartaFuncion)
    print(" ")

    listaDuplicado=[1,2,2,3,4,5,5]
    hayDuplicados()

    borrarDuplicados()



main()