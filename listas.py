# Oscar MR, A01376398.
# Listas.


# Recibe como parámetro una lista de números enteros y regresa una nueva lista con la suma acumulada de los datos.
def sumarAcumulado(lista):
    nuevaLista = []
    acumuldor = 0

    for n in lista:
        acumuldor += n
        nuevaLista.append(acumuldor)

    return nuevaLista


# Recibe como parámetro una lista de valores enteros y regresa una nueva lista, pero sin el primero ni el último.
def recortarLista(lista):
    nuevaLista = []

    if len(lista) == 0:
        return []

    if len(lista) != 0:
        for dato in lista:
            nuevaLista.append(dato)

    nuevaLista.pop(lista.index(dato))
    nuevaLista.pop(0)

    return nuevaLista


# Recibe una lista de valores y regresa True si los valores están ordenados, False en otro caso.
def estanOrdenados(lista):
    for n in range(1, len(lista)):
        if lista[n-1] > lista[n]:
            return False
    return True


# Recibe dos cadenas como parámetros, regresa True si son anagramas, False en otro caso.
def sonAnagramas(string1, string2):

    listaString1 = list(string1.upper())
    listaString2 = list(string2.upper())

    if len(listaString1) == len(listaString2):
        listaString1.sort()
        listaString2.sort()

        if listaString1 == listaString2:
            return True
        else:
            return False
    else:
        return False


# Recibe una lista de números enteros, regresa True si alguno de sus datos esta duplicado , False si todos son únicos.
def hayDuplicados(lista):
    listaVacia = []

    for k in lista:
        repeticiones = lista.count(k)
        if repeticiones > 1:
            listaVacia.append(True)
    if True in listaVacia:
        return True
    else:
        return False


# Recibe una lista de valores enteros y elimina de ésta los valores repetidos (solo deja una del conjunto de repetidos).
def borrarDuplicados(lista):
    nuevaLista = []

    for k in lista:
        if nuevaLista.count(k) == 0:
            nuevaLista.append(k)

    lista = nuevaLista

    return lista


# Prueba las funciones.
def main():
    print("Ejercicio 1:")
    listaA = [1, 2, 3, 4, 5, 6]
    listaB = [50]
    listaC = []
    print("La lista", listaA, "regresa la lista acumulada", sumarAcumulado(listaA))
    print("La lista", listaB, "regresa la lista acumulada", sumarAcumulado(listaB))
    print("La lista", listaC, "regresa la lista acumulada", sumarAcumulado(listaC))
    print()

    print("Ejercicio 2:")
    listaD = [1, 2, 3, 4, 5]
    listaE = [1, 2, 3]
    listaF = []
    print("La lista", listaD, "regresa una nueva lista sin el primer y el último número ", recortarLista(listaD))
    print("La lista", listaE, "regresa una nueva lista sin el primer y el último número ", recortarLista(listaE))
    print("La lista", listaF, "regresa una nueva lista sin el primer y el último número ", recortarLista(listaF))
    print()

    print("Ejercicio 3:")
    listaG = [1, 3, 5, 7, 9]
    listaH = [2, 4, 6, 4, 2]
    listaI = [4]
    listaJ = []
    print("La lista", listaG, "regresa:", estanOrdenados(listaG))
    print("La lista", listaH, "regresa:", estanOrdenados(listaH))
    print("La lista", listaI, "regresa:", estanOrdenados(listaI))
    print("La lista", listaJ, "regresa:", estanOrdenados(listaJ))
    print()

    print("Ejercicio 4:")
    palabraA, palabraB = ("MoRa", "rOmA")
    palabraC, palabraD = ("Hola", "hello")
    palabraE, palabraF = ("arenera", "reneraa")
    print("Las palabras", palabraA, "y", palabraB, "regresa:", sonAnagramas(palabraA, palabraB))
    print("Las palabras", palabraC, "y", palabraD, "regresa:", sonAnagramas(palabraC, palabraD))
    print("Las palabras", palabraE, "y", palabraF, "regresa:", sonAnagramas(palabraE, palabraF))
    print()

    listaK = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    listaL = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    listaM = [5, 10, 15, 20, 25]
    print("Ejercicio 5:")
    print("La lista", listaK, "regresa:", hayDuplicados(listaK))
    print("La lista", listaL, "regresa:", hayDuplicados(listaL))
    print("La lista", listaM, "regresa:", hayDuplicados(listaM))
    print()

    listaN = [100, 200, 200, 500, 1000]
    listaO = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    listaP = []
    print("Ejercicio 6:")
    print("La lista", listaN, "regresa:", borrarDuplicados(listaN))
    print("La lista", listaO, "regresa:", borrarDuplicados(listaO))
    print("La lista", listaP, "regresa:", borrarDuplicados(listaP))


main()





