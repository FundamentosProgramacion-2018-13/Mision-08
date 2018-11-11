# Autor: Juan Carlos Flores García, A01376511. Grupo 4

# Descripción: Programa que lee listas y modifica los datos dentro de ellas.


def sumarAcumulado(lista):
    sumar = 0
    sumarALista = []

    for numero in lista:
        sumar += numero
        sumarALista.append(sumar)
    return sumarALista


def recortarLista(lista):

    listaParaRecordar = lista[1:(len(lista) - 1)]
    return listaParaRecordar


def estanOrdenados(lista):
    for valor in range(1, len(lista)):
        if lista[valor - 1] > lista[valor]:
            return False
    return True


def sonAnagramas(cadena1, cadena2):
    listaA1 = list(cadena1)
    listaA2 = list(cadena2)
    listaA1.sort()
    listaA2.sort()

    if listaA1 == listaA2:
        return True
    else:
        return False


def hayDuplicados(lista):
    for valor in lista:
        if lista.count(valor) > 1:
            return True
    return False


def borrarDuplicados(lista):
    lista.sort
    for valor in lista:
        while lista.count(valor) > 1:
            lista.remove(valor)
    return lista


def main():
    print("Ejercicio 1:")
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("La lista: ", a, "regresa la lista acumulada", sumarAcumulado(a))
    print("La lista: ", b, "regresa la lista acumulada", sumarAcumulado(b))
    print("La lista: [] regresa la lista acumulada", sumarAcumulado([]))
    print("")

    print("Ejercicio 2:")
    c = [1, 2, 3, 4, 5]
    d = [1, 2]
    print("Lista original: ", c, "regresa la lista recortada", recortarLista(c))
    print("Lista original: ", d, " regresa la lista recortada", recortarLista(d))
    print("Lista original: [] regresa la lista recortada", recortarLista([]))
    print("")

    print("Ejercicio 3:")
    e = [1, 2, 3, 4]
    f = [7, 23, 15]
    print("Lista original: ", e, "La lista tiene un orden: ", estanOrdenados(e))
    print("Lista original: ", f, "La lista tiene un orden: ", estanOrdenados(f))
    print("")

    print("Ejercicio 4:")
    print("¿Las palabras mora y roma son anagramas?: ", sonAnagramas("roma", "mora"))
    print("¿Las palabras hola y hello son anagramas?:", sonAnagramas("hola", "hello"))
    print("¿Las palabras hola y hello son anagramas?: ", sonAnagramas("ana", "nana"))
    print("")

    print("Ejercicio 5:")
    g = [1, 2, 3, 1, 4, 5]
    h = [5, 7, 4, 6, 10]
    print("Lista original: ", g, "¿La lista tiene duplicados?: ", hayDuplicados(g))
    print("Lista original: ", h, "¿La lista tiene duplicados?: ", hayDuplicados(h))
    print("Lista original: []. ¿La lista tiene duplicados?: ", hayDuplicados([]))
    print("")

    print("Ejercicio 6:")
    i = [4, 4, 4, 5, 6, 7]
    j = [1, 2, 2, 2, 3]
    k = [5, 5, 8, 6, 10, 10]
    print("Lista original: [4, 4, 4, 5, 6, 7]", "regresa la lista sin duplicados", borrarDuplicados(i))
    print("Lista original:  [1, 2, 2, 2, 3]", "regresa la lista sin duplicados", borrarDuplicados(j))
    print("Lista original:  [5, 5, 8, 6, 10, 10]", "regresa la lista sin duplicados", borrarDuplicados(k))


main()

