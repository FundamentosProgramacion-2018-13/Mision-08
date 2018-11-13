#Autor: Arturo Marquez Olivar. A01376086.
#Completa las funciones de la mision 8.


#Recibe una lista que va agrgando los valores de la misma lista y te regresa una nueva lista con el resultado.
def sumarAcumulado(listaNumeros):
    listaSuma = []
    for k in range(len(listaNumeros)):
        i = sum(listaNumeros[:k + 1])
        listaSuma.append(i)
    return listaSuma


#Recibe una lista y elimina el primer y ultimo valor de la lista y te regresa una nueva lista con esos valores eliminados.
def recortarLista(listaNumeros):
    listaNueva = listaNumeros[1:len(listaNumeros)-1]
    return listaNueva


#Ordena los valores de una lista recibida, regresandolos en una nueva lista
def estanOrdenados(listaNumeros):
    ordenado = []
    for k in range(len(listaNumeros)):
        if k != 0:
            if listaNumeros[k] < listaNumeros[k-1]:
                ordenado.append(False)
    if False in ordenado:
        return False
    else:

        return True


#Compurueba si los datos de una lista resivida son anagramas.
def sonAnagramas(string1, string2):
    lista1Cap = list(string1.upper())
    lista2Cap = list(string2.upper())
    lista1Cap.sort()
    lista2Cap.sort()
    if lista1Cap == lista2Cap:
        return True
    else:
        return False


#Revisa si hay dulicados dentro de una lista para poder eliminarlos en otra funcion.
def hayDuplicados(listaNumeros):
    duplicados = []
    for numero in listaNumeros:
        apariciones = listaNumeros.count(numero)
        if apariciones > 1:
            duplicados.append(True)
    if True in duplicados:
        return True
    else:
        return False


#Borra los duplicados de una lista y regresa los nuevos en una lista nueva.
def borrarDuplicados(listaNumeros):
    for k in range(len(listaNumeros) -1, -1, -1):
        duplicados = listaNumeros.count(listaNumeros[k])
        if duplicados > 1:
            listaNumeros.remove(listaNumeros[k])

def main():

    print("Ejercicio 1:")
    for x in [[1, 2, 3, 5, 8], [], [10]]:
        print("Con la lista", x, "regresa la lista acumulada", sumarAcumulado(x))

    print("Ejercicio 2:")
    for x in [[1, 2, 3, 4, 5, 7, 10], [7, 9], []]:
        print("Con la lista original", x, ", regresa", recortarLista(x))

    print("Ejercicio 3:")
    for x in [[1, 2, 3, 4, 5], [1, 4, 5, 6, 3], [1, 1, 3]]:
        print("Con la lista", x, "está ordenada?", estanOrdenados(x))

    print("Ejercicio 4: ")
    print("Ana y Nana son anagramas?", sonAnagramas("ana", "Nana"))
    print("Mora y AMOR son anagramas?", sonAnagramas("Mora", "AMOR"))
    print("Frase y fresa son anagramas?", sonAnagramas("Frase", "fresa"))

    print("Ejercicio 5: ")
    for x in [[1, 2, 3, 4, 5], [5, 5, 6, 7, 8, 5, 7, 2], [12, 6, 8, 4, 4, 12]]:
        print("Con la lista", x, "tiene duplicados?", hayDuplicados(x))

    print("Ejercicio 6: ")
    for x in [[1, 2, 3, 4, 5], [5, 5, 6, 7, 8, 5, 7, 2], [12, 6, 8, 4, 4, 12]]:
        y = x.copy()
        borrarDuplicados(y)
        print("Con la lista", x, "sin duplicados es:", y)


main()