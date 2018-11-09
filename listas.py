# Autor: David Isaí López Jaimes    A01748363
# Programa que hace diferentes funciones, modificaciones a las listas

lista = [1,2,3,4,5]
listaVacia = []
lista11 = [5,6,7,8]
lista12 = [1,2,3]
lista13 = [7,23,15]



def sumarAcumulado(lista):
    lista2 = []
    acumulador = 0
    for valor in lista:
        valor += acumulador
        acumulador = valor
        lista2.append(acumulador)
    return lista2


def recortarLista(lista):
    lista2 = []
    for dato in lista:
        if dato != 0:
            lista2.append(dato)
    lista2.remove(max(lista))
    lista2.remove(min(lista))

    return lista2


def estanOrdenados(lista):
    lista2 = []
    valor = 0
    for dato in lista:
        if dato > valor:
            valor = dato
            lista2.append(valor)
            if lista2 == lista:
                return True
    return False


def sonAnagramas(cadena1, cadena2):
    unaLista = list(cadena2)

    pos1 = 0
    aunOK = True

    while pos1 < len(cadena1) and aunOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(unaLista) and not encontrado:
            if cadena1[pos1] == unaLista[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1

        if encontrado:
            unaLista[pos2] = None
        else:
            aunOK = False

        pos1 = pos1 + 1

    return aunOK


def hayDuplicados(lista):
    repetido = []

    for valor in lista:
        if valor not in repetido:
            repetido.append(valor)
    if len(repetido) == 0:
        return True
    else:
        return False


def borrarDuplicados(lista):
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

    print("\nEjercicio 3:")          # Casos ejemplo 2
    orden = estanOrdenados(lista)
    print("Lista original ", lista, "estan ordenados:  ", orden)
    orden2 = estanOrdenados(lista13)
    print("Lista original ", lista13, "estan ordenados: ", orden2)
    orden3 = estanOrdenados(lista12)
    print("Lista original ", lista12, "estan ordenados ", orden3)








main()





