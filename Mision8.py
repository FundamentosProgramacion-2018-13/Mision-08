# Autor: Ivan
# Descripción: Diferentes funciones que utilizan listas para realizar tareas.


# Esta función suma los números de una lista
def sumarAcumulado(lista):
    nuevaLista = []
    if len(lista)>0:
        nuevaLista.append(lista[0])
        for x in range(1, len(lista)):
            nuevaLista.append(lista[x]+nuevaLista[x-1])

    return nuevaLista


# Esta función quita el primer y el últmo término
def recortarLista(listaPrueba):
    listaRecortada = []
    if len(listaPrueba)>2:
        for x in range(1, len(listaPrueba)-1):
            listaRecortada.append(listaPrueba[x])

    return listaRecortada


# Esta función determina si están o no ordenados los números de una lista
def estanOrdenados(listaPrueba):
    ordenados = True
    for x in range(1, len(listaPrueba)):
        if listaPrueba[x] < listaPrueba[x-1]:
            ordenados = False

    return ordenados


# Esta función determina si dos palabras son anagramas
def sonAnagramas(cadenaPrueba1, cadenaPrueba2):
    sonAnagramas = False
    if len(cadenaPrueba1) == len(cadenaPrueba2):
        for x in range(len(cadenaPrueba1)):
            if cadenaPrueba1[x] in cadenaPrueba2:
                sonAnagramas = True

    return sonAnagramas


# Esta función determina si los números están duplicados
def hayDuplicados(listaPrueba):
    duplicados = False
    for x in range(0, len(listaPrueba)):
        for y in range(x+1, len(listaPrueba)):
            if listaPrueba[x] == listaPrueba[y]:
                duplicados = True

    return duplicados


# Esta función elimina los duplicados de una lista
def borrarDuplicados(listaPrueba):
    listaSinDuplicados = []
    for x in listaPrueba:
        if x not in listaSinDuplicados:
            listaSinDuplicados.append(x)
    listaPrueba = listaSinDuplicados

    return listaPrueba


# Esta función hace las listas y manda a llamar a las funciones
def main():
    listaPrueba = []
    listaPrueba.append(1)
    listaPrueba.append(3)
    listaPrueba.append(9)
    listaPrueba.append(45)
    listaPrueba.append(23)
    listaPrueba.append(45)
    listaPrueba.append(9)
    listaPrueba.append(9)
    listaPrueba.append(32)
    listaPrueba.append(9)

    listaPrueba2 = []
    listaPrueba3 = [1, 2, 3, 4, 5]
    listaPrueba4 = [8, 9]
    listaPrueba5 = [9, 8, 7, 6, 5, 4, 3, 3, 3, 2, 1, 5, 4]
    listaSumaAcumulada1 = sumarAcumulado(listaPrueba)
    listaSumaAcumulada2 = sumarAcumulado(listaPrueba2)
    listaSumaAcumulada3 = sumarAcumulado(listaPrueba3)
    listaSumaAcumulada4 = sumarAcumulado(listaPrueba4)
    listaSumaAcumulada5 = sumarAcumulado(listaPrueba5)
    print("Ejercicio 1:")
    print("La lista", listaPrueba, "regresa la lista acumulada", listaSumaAcumulada1)
    print("La lista", listaPrueba2, "regresa la lista acumulada", listaSumaAcumulada2)
    print("La lista", listaPrueba3, "regresa la lista acumulada", listaSumaAcumulada3)
    print("La lista", listaPrueba4, "regresa la lista acumulada", listaSumaAcumulada4)
    print("La lista", listaPrueba5, "regresa la lista acumulada", listaSumaAcumulada5)
    print("")

    listaRecortada1 = recortarLista(listaPrueba)
    listaRecortada2 = recortarLista(listaPrueba2)
    listaRecortada3 = recortarLista(listaPrueba3)
    listaRecortada4 = recortarLista(listaPrueba4)
    listaRecortada5 = recortarLista(listaPrueba5)
    print("Ejercicio 2:")
    print("La lista", listaPrueba, "regresa", listaRecortada1)
    print("La lista", listaPrueba2, "regresa", listaRecortada2)
    print("La lista", listaPrueba3, "regresa", listaRecortada3)
    print("La lista", listaPrueba4, "regresa", listaRecortada4)
    print("La lista", listaPrueba5, "regresa", listaRecortada5)
    print("")

    listaOrdenada1 = estanOrdenados(listaPrueba)
    listaOrdenada2 = estanOrdenados(listaPrueba2)
    listaOrdenada3 = estanOrdenados(listaPrueba3)
    listaOrdenada4 = estanOrdenados(listaPrueba4)
    listaOrdenada5 = estanOrdenados(listaPrueba5)
    print("Ejercicio 3:")
    print("La lista", listaPrueba, "está ordenada:", listaOrdenada1)
    print("La lista", listaPrueba2, "está ordenada:", listaOrdenada2)
    print("La lista", listaPrueba3, "está ordenada:", listaOrdenada3)
    print("La lista", listaPrueba4, "está ordenada:", listaOrdenada4)
    print("La lista", listaPrueba5, "está ordenada:", listaOrdenada5)
    print("")

    cadenaPrueba1 = "Roma"
    cadenaPrueba2 = "Mora"
    anagrama1 = sonAnagramas(cadenaPrueba1, cadenaPrueba2)
    cadenaPrueba3 = "Correr"
    cadenaPrueba4 = "Rayo"
    anagrama2 = sonAnagramas(cadenaPrueba3, cadenaPrueba4)
    cadenaPrueba5 = "Azul"
    cadenaPrueba6 = "Rojo"
    anagrama3 = sonAnagramas(cadenaPrueba5, cadenaPrueba6)
    cadenaPrueba7 = "Amor"
    cadenaPrueba8 = "Ramo"
    anagrama4 = sonAnagramas(cadenaPrueba7, cadenaPrueba8)
    cadenaPrueba9 = "Mar"
    cadenaPrueba10 = "RAM"
    anagrama5 = sonAnagramas(cadenaPrueba9, cadenaPrueba10)
    print("Ejercicio 4:")
    print("Las palabras", cadenaPrueba1, "y", cadenaPrueba2, "son anagramas:", anagrama1)
    print("Las palabras", cadenaPrueba3, "y", cadenaPrueba4, "son anagramas:", anagrama2)
    print("Las palabras", cadenaPrueba5, "y", cadenaPrueba6, "son anagramas:", anagrama3)
    print("Las palabras", cadenaPrueba7, "y", cadenaPrueba8, "son anagramas:", anagrama4)
    print("Las palabras", cadenaPrueba9, "y", cadenaPrueba10, "son anagramas:", anagrama5)
    print("")

    duplicados1 = hayDuplicados(listaPrueba)
    duplicados2 = hayDuplicados(listaPrueba2)
    duplicados3 = hayDuplicados(listaPrueba3)
    duplicados4 = hayDuplicados(listaPrueba4)
    duplicados5 = hayDuplicados(listaPrueba5)
    print("Ejercicio 5:")
    print("En la lista", listaPrueba, "hay duplicados: ", duplicados1)
    print("En la lista", listaPrueba2, "hay duplicados: ", duplicados2)
    print("En la lista", listaPrueba3, "hay duplicados: ", duplicados3)
    print("En la lista", listaPrueba4, "hay duplicados: ", duplicados4)
    print("En la lista", listaPrueba5, "hay duplicados: ", duplicados5)
    print("")

    listaSinDuplicados1 = borrarDuplicados(listaPrueba)
    listaSinDuplicados2 = borrarDuplicados(listaPrueba2)
    listaSinDuplicados3 = borrarDuplicados(listaPrueba3)
    listaSinDuplicados4 = borrarDuplicados(listaPrueba4)
    listaSinDuplicados5 = borrarDuplicados(listaPrueba5)
    print("Ejercicio 6:")
    print("Lista original:", listaPrueba, "Lista sin duplicados: ", listaSinDuplicados1)
    print("Lista original:", listaPrueba2, "Lista sin duplicados: ", listaSinDuplicados2)
    print("Lista original:", listaPrueba3, "Lista sin duplicados: ", listaSinDuplicados3)
    print("Lista original:", listaPrueba4, "Lista sin duplicados: ", listaSinDuplicados4)
    print("Lista original:", listaPrueba5, "Lista sin duplicados: ", listaSinDuplicados5)

    
main()
