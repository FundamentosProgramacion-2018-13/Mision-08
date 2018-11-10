# Autor: Luisa Fernanda Arellano Alvarado
# Tarea listas


def sumarAcumulado(lista): # recibe una lista de números enteros y regresa una nueva con la suma
    Suma = [] # lista vacía
    for k in range(len(lista)):
        i = sum(lista[0:k + 1]) # empieza en 0 y se le va añadiendo 1
        Suma.append(i) # se le agrega a la lista vacía i
    return Suma


def recortarLista(lista): # recibe como parametro una lista de valores enteros y regresa una nueva, sin el primer y último digito
    Nueva = lista[1:len(lista)-1]
    return Nueva


def estanOrdenados(lista): # verifica si las listas están ordenadas o no
    for k in range(len(lista)):
        if k != 0:
            if lista[k] < lista[k-1]:
             return False
    else:
     return True


def sonAnagramas(stringUno, stringDos): # verifica si un par de palabras son anagramas
    listaUno = list(stringUno.upper()) # Convierte la cadena de caracteres en mayusculas
    listaDos = list(stringDos.upper())
    listaUno.sort() # sort = invierte los valores
    listaDos.sort()
    if listaUno == listaDos:
        return True
    else:
        return False


def hayDuplicados(lista): # recibe una lista y recorre cada valor de ella, si hay duplicado regresa true si no regresa false
    for numero in lista:
        duplicados = lista.count(numero)
        if duplicados > 1:
         return True
    else:
        return False


def borrarDuplicados(lista): # Genera una nueva lista que no tenga duplicados
    for k in range(len(lista) -1,-1,-1):
        duplicados = lista.count(lista[k]) # cuenta la cantidad que hay en la lista de cada digito
        if duplicados > 1: # si es mayor a uno se elimina y
         lista.remove(lista[k])


def main():
    print('---------------------------------------------')
    print('Ejercicio 1:')
    for x in [[1, 2, 3, 5, 8], [], [5]]:
        print('La lista', x, 'regresa la lista acumulada', sumarAcumulado(x))
    print('--------------------------------------------------------')
    print('Ejercicio 2:')
    for x in [[1, 2, 3, 4, 5], [1, 2,3], []]:
        print('Lista original', x, ', regresa', recortarLista(x))
    print('---------------------------------------------------')
    print('Ejercicio 3:')
    for x in [[1, 2, 3, 5, 4], [1, 4, 5, 6, 3], [3,4, 5]]:
        print('La lista', x, 'Los valores estan ordenados?', estanOrdenados(x))
    print('---------------------------------------------------')
    print('Ejercicio 4: ')
    print('ana y Nana son anagramas?', sonAnagramas('ana', 'Nana'))
    print('Mora y AMOR son anagramas?', sonAnagramas('Mora', 'AMOR'))
    print('Hola y Hello son anagramas?', sonAnagramas('Hola', 'Hello'))
    print('-----------------------------------------------------')
    print('Ejercicio 5: ')
    for x in [[1, 2, 3, 4, 5], [5, 5, 6, 7, 8, 5, 7, 2], [12, 6, 8, 4, 4, 12]]:
        print('La lista', x, 'hay duplicados?', hayDuplicados(x))

    print('---------------------------------------------------')
    print('Ejercicio 6: ')
    for x in [[1, 2, 3, 4, 5], [5, 5, 6, 7, 8, 5, 7, 6]]:
        d = x.copy() # d =  duplicados, hace una copia de las listas que tiene x
        borrarDuplicados(d)
        print('lista original', x, 'sin duplicado:', d)


main()
