#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que emplea listas


#Recibe una lista de números enteros y regresa una nueva lista con la suma acumulada de datos.
def sumaracumulado(listaEnteros):
    listaSuma = []
    suma = 0
    for i in listaEnteros:
        suma += i
        listaSuma.append(suma)

    return listaSuma


#Recibe una lista de números enteros y regresa una nueva lista sin el primer ni ultimo elemento.
def recortarLista(listaEnteros):
    listaRecortada = []

    for k in range(1, len(listaEnteros)-1):
        listaRecortada.append(listaEnteros[k])

    return listaRecortada


#Recibe una lista y regresa True si los valores están ordenados, False si no.
def estanOrdenados(lista):
    numeroAnterior = lista[0]

    for i in lista:

        if i < numeroAnterior:
            return False
        else:
            numeroAnterior = i

    return True


#Recibe 2 cadenas y regresa True si son anagramas, False si no.
def sonAnagramas(string1, string2):
    str1 = string1.lower()
    str2 = string2.lower()
    listaStr1 = list(str1)
    listaStr2 = list(str2)
    listaStr2.reverse()

    if listaStr1 == listaStr2:
        return True
    else:
        return False


#Recibe una lista de números enteros y regresa True si alguno de sus datos está duplicado
def hayDuplicados(listaEnteros):

    for i in listaEnteros:

        numeroRepeticiones = listaEnteros.count(i)

        if numeroRepeticiones > 1:
            return True
        else:
            return False


#Recibe una lista de números enteros y modifica la lista para borrar algún dato duplicado.
def borrarDuplicados(listaEnteros):

    for i in listaEnteros:

        numeroRepeticiones = listaEnteros.count(i)

        if numeroRepeticiones > 1:
            listaEnteros.remove(i)

    return listaEnteros


#Función main para probar casos
def main():
    print(sumaracumulado([1,2,3,4,5]))
    print(recortarLista([1,2,3,4,5]))
    print(estanOrdenados([1,2,3]))
    print(sonAnagramas("rosa", "asor"))
    print(hayDuplicados([1,1,2,3,4,6,8,6]))
    print(borrarDuplicados([1,1,2,5,6,7,6]))


