#Autor: Oscar Alejandro Torres Maya, A01377686
#Descripcion: Mision 08, ejercicios con listas


#De una lista, va acumulando la suma de cada numero en la lista
def sumarAcumulado(lista):
    nuevaLista = []
    suma = 0
    for dato in range(len(lista)):
        suma = lista[dato] + suma
        nuevaLista.append(suma)
    return nuevaLista


#Borra el numero en posicion 0 y ultima posicion
def recortarLista(lista):
    if lista == []:
        return lista
    else:
        lista.pop(0)
        lista.pop(len(lista) - 1)
        nuevaLista = lista[:]
        return nuevaLista


#Dice si estan ordenados, es decir si van de menor a mayor
def estanOrdenados(lista):
    for datos in range(1, len(lista)):
        if lista[datos] < lista[datos - 1]:
            return False
    return True


#Dice si son anagramas, es decir que si se puede formar otra palabra con las mismas letras
def sonAnagramas(cadena1,cadena2):
    lista1 = list(cadena1.upper())
    lista2 = list(cadena2.upper())
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    else:
        return False


#Calcula si hay numeros duplicados en la lista
def hayDuplicados(lista):
    for numero in lista:
        if lista.count(numero) >= 2:
            return True
        else:
            return False


#Borra los numeros que estan duplicados y deja un numero de los duplicados solamente
def borrarDuplicados(lista):
    for datos in lista:
        repetidos = lista.count(datos)
        if repetidos >= 2:
            lista.remove(datos)
    return lista


def main():
    listaEnteros = [1,2,3,4,5,6,7]
    prueba1 = []
    prueba2 = [6]
    print("Ejercicio 1:")
    print("La lista",listaEnteros, "regresa la lista acumulada", sumarAcumulado(listaEnteros))
    print("La lista", prueba1, "regresa la lista acumulada", sumarAcumulado(prueba1))
    print("La lista", prueba2, "regresa la lista acumulada", sumarAcumulado(prueba2))
    print("")

    # No se porque si pongo la misma lista, me aparece el resultado y no la original
    print("Ejercicio 2:")
    prueba6 = [16, 18, 20]
    prueba1 = [1,2,3,4,5,6,7]
    prueba4 = []
    prueba5 = [16, 18, 20]
    print("Lista original", prueba1, "regresa", recortarLista(listaEnteros) )
    print("Lista original", prueba4, "regresa", recortarLista(prueba4) )
    print("Lista original", prueba5, "regresa", recortarLista(prueba6) )
    print("")

    print("Ejercicio 3:")
    listaEnteros = [3, 4, 2, 13, 4, 5, 2]
    prueba3 = [16, 18, 20]
    prueba4 = [1,2,3,4,5,1]
    print("Lista original", listaEnteros, "regresa", estanOrdenados(listaEnteros))
    print("Lista original", prueba3, "regresa", estanOrdenados(prueba3))
    print("Lista original", prueba4, "regresa", estanOrdenados(prueba4))

    print("")
    print("Ejercicio 4:")
    cadena1 = "Mora"
    cadena2 = "Roma"
    cadena3 = "Oso"
    cadena4 = "Baboso"
    cadena5 = "Roma"
    cadena6 = "Omar"
    print("Cadenas originales", cadena1,"y",cadena2, "regresa", sonAnagramas(cadena1,cadena2))
    print("Cadenas originales", cadena3,"y",cadena4, "regresa", sonAnagramas(cadena3, cadena4))
    print("Cadenas originales", cadena5,"y",cadena6, "regresa", sonAnagramas(cadena5, cadena6))

    print("")
    print("Ejercicio 5:")
    prueba2 = [5,6,1,7,8,5]
    prueba3 = [16, 18, 20]
    prueba4 = [1, 2, 3, 4, 5, 1]
    print("Lista original", prueba2, "regresa", hayDuplicados(prueba2))
    print("Lista original", prueba3, "regresa", hayDuplicados(prueba3))
    print("Lista original", prueba4, "regresa", hayDuplicados(prueba4))

    #No se porque si pongo la misma lista, me aparece el resultado y no la original
    print("")
    print("Ejercicio 6:")
    prueba7 = [1, 2, 3, 4, 5, 1]
    prueba8 = [1, 2, 3, 4, 5, 1]
    prueba9 = [3, 4, 2, 13, 4, 5, 2]
    prueba10 = [3, 4, 2, 13, 4, 5, 2]
    prueba11 = [16, 18, 20]
    prueba12 = [16, 18, 20]
    print("Lista original", prueba7, "regresa", borrarDuplicados(prueba8))
    print("Lista original", prueba9, "regresa", borrarDuplicados(prueba10))
    print("Lista original", prueba11, "regresa", borrarDuplicados(prueba12))

main()