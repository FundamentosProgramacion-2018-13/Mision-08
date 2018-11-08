# Autor: Alejandro Torices Oliva
# Es un programa que experimenta con el uso de las listas


# Es una función que coloca en el índice del elemento la suma con los elementos anteriores
def sumarAcumulado(listaNumeros):
    listaSuma = []
    for k in range(len(listaNumeros)):
        i = sum(listaNumeros[:k + 1])
        listaSuma.append(i)
    return listaSuma


# Es una función que recibe una lista y regresa otra lista sin el primer ni el último elementos de la lista original
def recortarLista(listaNumeros):
    nuevaLista = listaNumeros[1:len(listaNumeros)-1]
    return nuevaLista


# Es una función que determina si los elementos de la lista estan ordenados o no
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


# Es una función que determina si dos cadenas son anagramas o no
def sonAnagramas(string1, string2):
    lista1Cap = list(string1.upper())
    lista2Cap = list(string2.upper())
    lista1Cap.sort()
    lista2Cap.sort()
    if lista1Cap == lista2Cap:
        return True
    else:
        return False


# Es una función que determina si hay elementos duplicados en una lista
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


# Es una función que elimina los duplicados de una lista
def borrarDuplicados(listaNumeros):
    for k in range(len(listaNumeros)-1, -1, -1):
        apariciones = listaNumeros.count(listaNumeros[k])
        if apariciones > 1:
            listaNumeros.remove(listaNumeros[k])


# Es la función principal
def main():
    print('')
    print('Ejercicio 1:')
    for x in [[1, 2, 3, 5, 8], [], [10]]:
        print('La lista', x, 'regresa la lista acumulada', sumarAcumulado(x))
    print(' ')
    print('Ejercicio 2:')
    for x in [[1, 2, 3, 4, 5, 7, 10], [7, 9], []]:
        print('Lista original', x, ', regresa', recortarLista(x))
    print(' ')
    print('Ejercicio 3:')
    for x in [[1, 2, 3, 4, 5], [1, 4, 5, 6, 3], [1, 1, 3]]:
        print('La lista', x, 'está ordenada?', estanOrdenados(x))
    print('')
    print('Ejercicio 4: ')
    print('Mora y AMOR son anagramas?', sonAnagramas('Mora', 'AMOR'))
    print('TAMALES y maletas son anagramas?', sonAnagramas('TAMALES', 'maletas'))
    print('ana y Nana son anagramas?', sonAnagramas('ana', 'Nana'))
    print('')
    print('Ejercicio 5: ')
    for x in [[1, 2, 3, 4, 5], [5, 5, 6, 7, 8, 5, 7, 2], [12, 6, 8, 4, 4, 12]]:
        print('La lista', x, 'tiene duplicados?', hayDuplicados(x))

    print('')
    print('Ejercicio 6: ')
    for x in [[1, 2, 3, 4, 5], [5, 5, 6, 7, 8, 5, 7, 2], [12, 6, 8, 4, 4, 12]]:
        y = x.copy()
        borrarDuplicados(y)
        print('La lista', x, 'sin duplicados es:', y)




main()
