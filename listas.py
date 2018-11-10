def sumarAcumulado(lista):
    suma = 0
    listaSuma = []
    for dato in lista:
        suma += dato
        listaSuma.append(suma)
    return listaSuma


def recortarLista(lista):
    listaRecortada = []
    for k in range(len(lista)):
        if k == 0 or k == (len(lista) - 1):
            pass
        else:
            listaRecortada.append(lista[k])
    return listaRecortada


def estanOrdenados(lista):
    for k in range(1, len(lista)):
        if lista[k] < lista[k-1]:
            return False
    return True


def sonAnagramas(palabra1, palabra2):
    letrasIguales = 0
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if len(palabra1) == len(palabra2):
        for char in palabra1:
            if char in palabra2:
                letrasIguales += 1
        if letrasIguales == len(palabra1):
            return True
        else:
            return False
    return False


def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato) >= 2:
            return True
    return False


def borrarDuplicados(lista):
    for dato in lista:
        while lista.count(dato) >= 2:
            lista.remove(dato)
    return lista


def main():

    print("Ejercicio 1:")
    print("Lista original: [1,2,3,4,5] regresa la lista acumulada", sumarAcumulado([1, 2, 3, 4, 5]))
    print("Lista original: [5] regresa la lista acumulada", sumarAcumulado([5]))
    print("Lista original: [] regresa la lista acumulada", sumarAcumulado([]))

    print("""
Ejercicio 2:""")
    print("Lista original: [1,2,3,4,5] regresa la lista recortada", recortarLista([1, 2, 3, 4, 5]))
    print("Lista original: [3, 4] regresa la lista recortada", recortarLista([3, 4]))
    print("Lista original: [] regresa la lista recortada", recortarLista([]))

    print("""
Ejercicio 3:""")
    print("Lista original: [1,2,3,4,5]. ¿Están ordenados?: ", estanOrdenados([1, 2, 3, 4, 5]))
    print("Lista original: [1,5,11,9,1]. ¿Están ordenados?: ", estanOrdenados([1, 5, 11, 9, 1]))
    print("Lista original: [5,4,3]. ¿Están ordenados?: ", estanOrdenados([5,4,3]))

    print("""
Ejercicio 4:""")
    print("Palabra 1: jabon. Palabra 2: banjo. ¿Son anagramas?: ", sonAnagramas("jabon", "banjo"))
    print("Palabra 1: Pollo. Palabra 2: Repollo. A ¿Son anagramas?: ", sonAnagramas("Pollo", "Repollo"))
    print("Palabra 1: RoMaN. Palabra 2: nOrMa. ¿Son anagramas?: ", sonAnagramas("RoMaN", "nOrMa"))

    print("""
Ejercicio 5:""")
    print("Lista original: [1,2,3,4,5]. ¿Hay duplicados?: ", hayDuplicados([1, 2, 3, 4, 5]))
    print("Lista original: [1,5,11,9,1]. ¿Hay duplicados?: ", hayDuplicados([1, 5, 11, 9, 1]))
    print("Lista original: [5,4,3]. ¿Hay duplicados?: ", hayDuplicados([5,4,3]))

    print("""
Ejercicio 6:""")
    print("Lista original: [1,2,3,3,3,3,3,4,5] regresa la lista sin duplicados", borrarDuplicados([1,2,3,3,3,3,3,4,5]))
    print("Lista original: [1,1,10,10] regresa la lista sin duplicados", borrarDuplicados([1,1,10,10]))
    print("Lista original: [5] regresa la lista sin duplicados", borrarDuplicados([5]))

main()

