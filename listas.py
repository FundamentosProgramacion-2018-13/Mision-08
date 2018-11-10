# Luis Ricardo Chagala Cervantes
# Funciones con diferentes listas y diferentes tipos de ejercicios ejercicios.


def sumarAcumulado(lista):
    listaN = []
    for k in range(1, len(lista)+1):
        listaN.append(sum(lista[:k]))
    return listaN


def recortarLista(lista):
    listaN = []
    for k in range(1, len(lista)-1):
        listaN.append(lista[k])
    return listaN


def estanOrdenados(lista):
    variable = True
    for k in range(1, len(lista)):
        if lista[k] > lista[k-1]:
            variable = True
        if not lista[k] > lista[k-1]and len(lista) > 2:
            variable = False
            break

    return variable


def sonAnagramas(cadena, cadena02):
    palabra1 = cadena.lower()
    palabra2 = cadena02.lower()
    variable = 0
    for x in range(0, len(palabra1)):
        for y in range(0, len(palabra2)):
            if palabra1[x] == palabra2[y]:
                variable = 1
                break
            elif palabra1[x] != palabra2[y]:
                variable = 2

    if variable == 1 and len(palabra1) == len(palabra2):
        check = True
        return check
    elif variable == 2:
        check = False
        return check
    elif len(palabra1) != len(palabra2):
        check = False
        return check


def hayDuplicados(lista):
    check = None
    variable = len(lista)
    variable1 = len(list(set(lista)))
    if variable == variable1:
        check = False
    if variable > variable1:
        check = True
    return check


def borrarDuplicados(lista):
    lista = list(set(lista))
    return lista


def main():
    lista0 = [1, 2, 3, 4, 5]
    lista1 = []
    lista2 = [5]
    print("Ejercicio 1: ")
    print("La lista", lista0, "regresa la lista acumulada", sumarAcumulado(lista0))
    print("La lista", lista1, "regresa la lista acumulada", sumarAcumulado(lista1))
    print("La lista", lista2, "regresa la lista acumulada", sumarAcumulado(lista2))
    print()

    lista3 = [1, 2, 3, 4, 5]
    lista4 = [1, 2, 3]
    lista5 = []
    print("Ejercicio 2: ")
    print("La lista", lista3, "regresa ", recortarLista(lista3))
    print("La lista", lista4, "regresa ", recortarLista(lista4))
    print("La lista", lista5, "regresa ", recortarLista(lista5))
    print()

    lista6 = [1, 2, 3, 4, 5]
    lista7 = [1, 2, 3, 2]
    lista8 = [4]
    lista = []
    print("Ejercicio 3: ")
    print("La lista", lista6, "regresa ", estanOrdenados(lista6))
    print("La lista", lista7, "regresa ", estanOrdenados(lista7))
    print("La lista", lista8, "regresa ", estanOrdenados(lista8))
    print("La lista", lista, "regresa ", estanOrdenados(lista))
    print()

    print("Ejercicio 4:")
    print("Las palabras", "Roma y Mora", "regresa", sonAnagramas("ITESM", "times"))
    print("Las palabras", "Hola y Hello", "regresa", sonAnagramas("Hola", "Hello"))
    print("Las palabras", "ana y nana", "regresa", sonAnagramas("ana", "nana"))
    print()

    lista9 = [1, 2, 3, 1, 4, 5]
    lista10 = [5, 7, 4, 6, 10]
    lista11 = [1, 2, 3, 2, 5]
    print("Ejercicio 5: ")
    print("La lista", lista9, "regresa ", hayDuplicados(lista9))
    print("La lista", lista10, "regresa ", hayDuplicados(lista10))
    print("La lista", lista11, "regresa ", hayDuplicados(lista11))
    print()

    lista12 = [1, 8, 3, 4, 3, 1, 8, 2, 7, 8]
    lista13 = [1, 2, 3, 1, 2, 3]
    lista14 = []
    print("Ejercicio 6: ")
    print("La lista", lista12, "regresa ", borrarDuplicados(lista12))
    print("La lista", lista13, "regresa ", borrarDuplicados(lista13))
    print("La lista", lista14, "regresa ", borrarDuplicados(lista14))

main()