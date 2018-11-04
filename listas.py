#Jesús Zabdiel Sánchez Chávez   A01374964

#Mison 08 Listas


def sumarAcumulado(lista):
    listaNueva = []

    for x in range (len(lista)):
        cortarLista = lista[0:x+1:1]
        listaNueva.append(sum(cortarLista))
    return listaNueva

def recortarLista(lista):
    listaNueva = lista[:]
    if len(lista) > 0:
        listaNueva.pop()
        listaNueva.remove(listaNueva[0])
    return listaNueva

def estanOrdenados(lista):

    for x in range(len(lista)):
        if x+1 < len(lista):
            if lista[x] <= lista[x+1]:
                continue
            else:
                return False
    return True


def sonAnagramas (cadena1, cadena2):

    lista1 = list(cadena1)
    lista2 = list(cadena2)
    lista1.sort()
    lista2.sort()

    if lista1 == lista2:
        return True
    else:
        return False

def hayDuplicados(lista):
    lista.sort()
    for x in range (len(lista)):
        if x + 1 < len(lista):
            if lista[x] != lista[x+1]:
                continue
            else:
                return True
    return False


def  borrarDuplicados (lista):
    listaNueva = []
    for x in range (len(lista)):
        if lista[x] not in listaNueva:
            listaNueva.append(lista[x])
    lista = listaNueva

    return lista
