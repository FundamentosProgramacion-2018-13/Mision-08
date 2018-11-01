# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Diferentes funciones que, en su mayoría, reciben listas, las manipulan y regresan nuevas


def sumarAcumulador(listaOriginal):
    acumulador, listaNueva = 0, []
    for n in listaOriginal:
        acumulador += n
        listaNueva.append(acumulador)
    return listaNueva


def recortarLista(listaOriginal):
    listaNueva = listaOriginal
    listaNueva.pop()
    listaNueva.pop(0)
    return listaNueva


def estanOrdenados(listaOriginal):
    for n in range(1, len(listaOriginal)):
        if listaOriginal[n-1] > listaOriginal[n]:
            return False
    return True


def sonAnagramas(cadena1: str, cadena2: str):
    cadena1, cadena2 = cadena1.lower(), cadena2.lower()
    if len(cadena1) == len(cadena2):
        for n in cadena2.split():
            cadena1 = cadena1.strip(n)
        if cadena1 == "":
            return True
        else:
            return False
    else:
        return False


def hayDuplicados(listaOriginal):
    listaOriginal.sort()
    for n in range(1, len(listaOriginal)):
        if listaOriginal[n-1] == listaOriginal[n]:
            return False
    return True


def borrarDuplicados(listaOriginal):
    listaNueva = []
    for n in listaOriginal:
        if listaNueva.count(n) == 0:
            listaNueva.append(n)
    listaOriginal = listaNueva
    return listaOriginal
