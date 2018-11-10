#Autor: Jesús Emmanuel Alcalá Nava
#Descripción:este programa realiza diferentes ejercicios como contar duplicados o verificar si un par de palabras son anagramas


def sumarAcumulado(lista):
    suma = 0
    listaSumada = []
    for dato in lista:
        suma += dato
        listaSumada.append(suma)
    return listaSumada


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
    print("Lista original: [3,4] regresa la lista recortada", recortarLista([3, 4]))
    print("Lista original: [] regresa la lista recortada", recortarLista([]))

    print("""
Ejercicio 3:""")
    print("Lista original: [1,2,3]. ¿Están ordenados?: ", estanOrdenados([1, 2, 3]))
    print("Lista original: [6,10,40,2,9]. ¿Están ordenados?: ", estanOrdenados([6, 10, 40, 2, 9]))
    print("Lista original: [5,4,3]. ¿Están ordenados?: ", estanOrdenados([9, 2, 1]))

    print("""
Ejercicio 4:""")
    print("Palabra 1: alegan. Palabra 2: Ángela. ¿Son anagramas?: ", sonAnagramas("alegan", "Ángela"))
    print("Palabra 1: riesgo. Palabra 2: Sergio. A ¿Son anagramas?: ", sonAnagramas("riesgo", "Sergio"))
    print("Palabra 1: loco. Palabra 2: malos. ¿Son anagramas?: ", sonAnagramas("loco", "malos"))

    print("""
Ejercicio 5:""")
    print("Lista original: [1,2,3,1,4,5]. ¿Hay duplicados?: ", hayDuplicados([1, 2, 3, 1,  4, 5]))
    print("Lista original: [2,5,6,7]. ¿Hay duplicados?: ", hayDuplicados([2, 5, 6, 7]))
    print("Lista original: [1,3,3]. ¿Hay duplicados?: ", hayDuplicados([1, 3, 3]))

    print("""
Ejercicio 6:""")
    print("Lista original: [1,2,2,2,3,4,4,5] regresa la lista sin duplicados", borrarDuplicados([1, 2, 2, 2, 3, 4, 4, 5]))
    print("Lista original: [30,500,550,60] regresa la lista sin duplicados", borrarDuplicados([30, 500, 550, 60]))
    print("Lista original: [1] regresa la lista sin duplicados", borrarDuplicados([1]))

main()
