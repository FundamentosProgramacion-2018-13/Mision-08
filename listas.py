#Alex Fernando Leyva Martinez - A01747078 - GRUPO 04
# Este programa permite poner en práctica los usos de listas con disitintos tipos de ejercicios


# Esta función se encarga de ir sumando los números en la lista, es decir, acumulárlos
def sumarAcumulado(listaNumeros):
    listaSuma = []
    for k in range(len(listaNumeros)):
        n = sum(listaNumeros[:k+1])
        listaSuma.append(n)

    return listaSuma


# Esta función se encarga de eliminar el primer y último número
def recortarLista(listaNumeros):
    listaRecortada = []
    for k in range(len(listaNumeros)):
        limites = len(listaNumeros)-1
        listaRecortada = listaNumeros[1:limites:1]

    return listaRecortada

# Esta función se encarga de mencionar si los números están ordenados o no
def estanOrdenados(listaNumeros):
    listaOrdenanda = []
    for k in range(1, len(listaNumeros)):
        if listaNumeros[k] < listaNumeros[k - 1]:
            listaOrdenanda.append(False)
    if False in listaOrdenanda:
        return False
    else:
        return True


# Esta función se encarga de comprobar se las palabras usadas son anagramas
def sonAnagramas(string, string2):
    lista1 = list(string.upper())
    lista2 = list(string2.upper())
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    else:
        return False


# Esta función se encarga de comprobar si los hay números duplicados en la lista a examinar
def hayDuplicados(listaNumeros):
    contador = 0
    for dato in listaNumeros:
        duplicados = listaNumeros.count(dato)
        if duplicados > 1:
            contador += 1

    if contador > 0:
        return True
    else:
        return False

# Esta función se encarga de eliminar los números duplicados dentro de la lista
def borrarDuplicados(listaNumeros):
    for k in range(len(listaNumeros)-1, -1, -1):
        repetidos = listaNumeros.count(listaNumeros[k])
        if repetidos > 1:
            listaNumeros.remove(listaNumeros[k])

    return listaNumeros


# Función Principal
def main():
    print("Ejercicio 1:")
    for k in [1,2,3,4,5], [], [5]:
        print("La lista", k,"regresa la lista acumulada", sumarAcumulado(k))
    print("--------------------")
    print("Ejercicio 2:")
    for k in [1,2,3,4,5], [1,2,3], []:
        print("Lista Original",k,", regresa", recortarLista(k))
    print("--------------------")
    print("Ejercicio 3:")
    for k in [1,2,3], [7,23,15], [12,13,11]:
        print("La lista", k, "están ordenados?", estanOrdenados(k))
    print("--------------------")
    print("Ejercicio 4:")
    print("Las palabras Roma y Mora son anagramas? ", sonAnagramas("ROMA", "MoRa"))
    print("Las palabras Hola y Hello son anagramas? ", sonAnagramas("HoLa", "HELLo"))
    print("Las palabras Casa y Saca son anagramas? ", sonAnagramas("CaSa", "SACa"))
    print("--------------------")
    print("Ejercicio 5:")
    for k in [1,2,3,1,5], [5,7,4,6,10], [1,2,3,4,4,5,6,7,7]:
        print("La lista", k,"tiene elementos repetidos?", hayDuplicados(k))
    print("--------------------")
    print("Ejercicio 6:")
    for k in [1,8,3,4,3,1,8,2,7,8], [1,2,3,3,4,5,6,6,7,8], [1,2,3,4,5]:
        m = k.copy()
        print("Lista Original", m, "regresa", borrarDuplicados(k))
    print("--------------------")

main()





