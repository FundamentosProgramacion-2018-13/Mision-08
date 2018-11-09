# Autor: David Isaí López Jaimes    A01748363
# Programa que hace diferentes funciones, modificaciones a las listas y nuevas listas

lista = [1,2,3,4,5]
listaVacia = []
lista11 = [5,6,7,8]
lista12 = [1,2,3]
lista13 = [7,23,15]


def sumarAcumulado(lista):      # Función que suma i*1 de la lusta y o acumula
    lista2 = []
    acumulador = 0
    for valor in lista:
        valor += acumulador
        acumulador = valor
        lista2.append(acumulador)
    return lista2


def recortarLista(lista):           # Función que borra de una lista original en valor maximo y mínimo, regresa lista nueva
    lista2 = []
    for dato in lista:
        if dato != 0:
            lista2.append(dato)
    lista2.remove(max(lista))
    lista2.remove(min(lista))

    return lista2


def estanOrdenados(lista):      # Verifica si la lista esta ordenada o no
    lista2 = []
    valor = 0
    for dato in lista:
        if dato > valor:
            valor = dato
            lista2.append(valor)
            if lista2 == lista:
                return True
    return False


def sonAnagramas(cadena1, cadena2):         # Función que verifica si 2 cadenas son anagramas
    lista2 = list(cadena2)

    pos1 = 0
    aunOK = True

    while pos1 < len(cadena1) and aunOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(lista2) and not encontrado:
            if cadena1[pos1] == lista2[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1

        if encontrado:
            lista2[pos2] = None
        else:
            aunOK = False

        pos1 = pos1 + 1

    return aunOK


def hayDuplicados(lista):       # Función que busca si hay valores repetidos en una lista y regresa True ó False
    repetido = []

    for valor in lista:
        if valor not in repetido:
            repetido.append(valor)
    if len(repetido) == len(lista):
        return False
    return True


def borrarDuplicados(lista):        # Función que borra valores duplicados de una lista
    lista2 = []
    for valor in lista:
        if valor not in lista2:
            lista2.append(valor)
    return lista2


def main():
    print("Ejercicio 1:")          # Casos ejemplo 1
    lista2 = sumarAcumulado(lista)
    print("La lista ", lista, "regresa la suma acumulada ", lista2)
    lista3 = sumarAcumulado(listaVacia)
    print("La lista ", listaVacia, "regresa la suma acumulada ", lista3)
    lista4 = sumarAcumulado(lista11)
    print("La lista ", lista11, "regresa la suma acumulada ", lista4)

    print("\nEjercicio 2:")          # Casos ejemplo 2
    lista5 = recortarLista(lista)
    print("Lista original ", lista, "regresa ", lista5)
    lista6 = recortarLista(lista12)
    print("Lista original ", lista12, "regresa ", lista6)
    lista7 = recortarLista(lista11)
    print("Lista original ", lista11, "regresa ", lista7)

    print("\nEjercicio 3:")          # Casos ejemplo 3
    orden = estanOrdenados(lista)
    print("Lista original ", lista, "estan ordenados:  ", orden)
    orden2 = estanOrdenados(lista13)
    print("Lista original ", lista13, "estan ordenados: ", orden2)
    orden3 = estanOrdenados(lista12)
    print("Lista original ", lista12, "estan ordenados ", orden3)

    print("\nEjercicio 4:")     # Casos ejemplo 4
    cadena1 = 'Hola'
    cadena2 = 'Hello'
    anagrama1 = sonAnagramas(cadena1, cadena2)
    print("Son anagramas %s y %s" % (cadena1, cadena2), " = ",anagrama1)
    cadena1 = 'roma'
    cadena2 = 'mora'
    anagrama2 = sonAnagramas(cadena1, cadena2)
    print("Son anagramas %s y %s" % (cadena1, cadena2), " = ",anagrama2)
    cadena1 = 'ana'
    cadena2 = 'ani'
    anagrama3 = sonAnagramas(cadena1, cadena2)
    print("Son anagramas %s y %s" % (cadena1, cadena2), " = ",anagrama3)

    print("\nEjercicio 5:")      # Casos ejemplo 5
    lst = [1,2,3,4,5]
    duplicados = hayDuplicados(lst)
    print("En la lista ", lst, "hay duplicados: ", duplicados)
    lst2 = [1,2,3,4,3,5]
    duplicados2 = hayDuplicados(lst2)
    print("En la lista ", lst2, "hay duplicados: ", duplicados2)
    lst3 = [5,7,8,6]
    duplicados3 = hayDuplicados(lst3)
    print("En la lista ", lst3, "hay duplicados: ", duplicados3)

    print("\nEjercicio 6: ")        # Casos ejercicio 6
    lsta = [1,8,4,3,8,5]
    borrarDup = borrarDuplicados(lsta)
    print("Lista ", lsta, "lista sin duplicados ", borrarDup)
    lstb = [1, 2,3,4,4,5,5,]
    borrarDup2 = borrarDuplicados(lstb)
    print("Lista ", lstb, "lista sin duplicados ", borrarDup2)
    lstc = [29,56,7,7,8,8,89]
    borrarDup3 = borrarDuplicados(lstc)
    print("Lista ", lstc, "lista sin duplicados ", borrarDup3)



main()





