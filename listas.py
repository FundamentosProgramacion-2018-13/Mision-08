#   Carlos Badillo García
#   Programa que interactua con distintas listas y dependiendo la funcion, realizan ciertas cosas.


def sumarAcumulado(listaNum): #Función que usa los numeros de una lista, y los va sumando, creando un nuevo valor en otra lista
    nuevaL = []
    contador = 0

    for valor in listaNum:
        contador = contador + valor
        nuevaL.append(contador)
    return nuevaL


def recortarLista(listaNum): #Función que elimina el primer y ultimo dato de una lista
    nuevaL = listaNum[:]

    if listaNum == []:
        return []
    elif len(listaNum) == 1:
        return listaNum
    else:
        nuevaL.pop(0)
        nuevaL.pop(-1)
        return nuevaL


def estanOrdenados(listaNum): #Función que dice si los datos en una lista estan ordenados de menor a mayor
    if listaNum == []:
        return True
    for valor in range(len(listaNum)):
        if len(listaNum) == 1:
            return True
        elif listaNum[valor] <= listaNum[valor-1]:
            return True
        else:
            return False


def sonAnagramas(palabra1, palabra2): #Función que analiza dos palabra, las compara y dice si son anagramas o no
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    lista1 = list(palabra1)
    lista2 = list(palabra2)

    if len(lista1) == len(lista2):
        for letras in lista1:
            if letras in lista2:
                return True
            elif letras not in lista2:
                return False
        for letras in lista2:
            if letras in lista1:
                return True
            elif letras not in lista1:
                return False
    return False


def hayDuplicados(listaNum): #Función que dice si hay valores duplicado en una lista
    if listaNum == []:
        return False

    for valor in listaNum:
        repetidos = listaNum.count(valor)
        if repetidos >= 2:
            return True
        else:
            return False


def borrarDuplicados(listaNum): #Función que elimina los valores duplicados de una lista, si los hay.

    for valor in listaNum:
        while listaNum.count(valor) > 1:
            listaNum.remove(valor)
    return listaNum


def main():
    listaNum = []
    palabra1 = "amor"
    palabra2 = "roma"

    print(listaNum)
    print(sumarAcumulado(listaNum))
    print(recortarLista(listaNum))
    print(estanOrdenados(listaNum))
    print(sonAnagramas(palabra1, palabra2))
    print(hayDuplicados(listaNum))
    print(borrarDuplicados(listaNum))


main()