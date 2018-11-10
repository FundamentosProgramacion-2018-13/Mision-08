#Autor: Erick David Ramírez Martínez, A01748155, Grupo: 02
# Programa que realiza varias funciones con listas


# Función que suma acumulativamente los valores de una lista
def sumarAcumulado(lista):
    nuevaLista = []
    valor = 0
    for k in range(len(lista)):
        valor = valor + lista[k]
        nuevaLista.append(valor)

    return nuevaLista


# Función que elimina el primer y último valor de una lista
def recortarLista(lista):
    nuevaLista = []
    for k in range(1, len(lista)-1):
        nuevaLista.append(lista[k])

    return nuevaLista


# Función que analiza una lista y verifica si esta está ordenada o no
def estanOrdenados(lista):
    listaVacia = []
    if lista != listaVacia:
        if len(lista) == 1:
            return True
        for k in range(len(lista)):
            for j in range(k+1, len(lista)):
                if lista[k] <= lista[j]:
                    ordenados = True
                else:
                    ordenados = False
                    return ordenados
        else:
            ordenados = True
            return ordenados
    else:
        return True


# Función que compara 2 cadenas y señala si son anagramas o no
def sonAnagramas(cadena1, cadena2):
    listaVacia = []
    listaCadena1 = list(cadena1.lower())
    listaCadena2 = list(cadena2.lower())
    if len(listaCadena1) == len(listaCadena2):
        for k in range(len(listaCadena1)):
            for j in range(len(listaCadena2)):
                if listaCadena2[j] == listaCadena1[k]:
                    letra = listaCadena1[k]
                    listaCadena2.remove(letra)
                    break
        if listaCadena2 == listaVacia:
            anagramas = True
        else:
            anagramas = False
    else:
        anagramas = False

    return anagramas


# Función que evalúa una lista y muestra si hay duplicados o no
def hayDuplicados(lista):
    if len(lista) !=0:
        for k in range(len(lista)):
            for j in range(k+1, len(lista)):
                if lista[k] == lista[j]:
                    return True
    return False


# Función que borra los duplicados de una lista.
def borrarDuplicados(lista):
    for k in range(len(lista)):
        for j in range(-1, -len(lista)+k, -1):
            if lista[k] == lista[j]:
                lista[j] = 0.5
    for k in range(len(lista)):
        if lista[j] == 0.5:
            lista.remove(0.5)
    return lista


def main():
    print("EJERCICIO 1")
    lista1 = [1,2,3,4,5]
    lista2 = []
    lista3 = [1]
    print("La lista: ", lista1, " regresa la lista acumulada, ", sumarAcumulado(lista1))
    print("La lista: ", lista2, " regresa la lista acumulada, ", sumarAcumulado(lista2))
    print("La lista: ", lista3, " regresa la lista acumulada, ", sumarAcumulado(lista3))
    print("")
    print("EJERCICIO 2")
    lista4 = [1,2,3,4,5]
    lista5 = []
    lista6 = [1,2]
    print("La lista: ", lista4, " regresa, ", recortarLista(lista4))
    print("La lista: ", lista5, " regresa, ", recortarLista(lista5))
    print("La lista: ", lista6, " regresa, ", recortarLista(lista6))
    print("")
    print("EJERCICIO 3")
    lista7 = [4,2,5,7]
    lista8 = [1,3,4,6,7,9]
    lista9 = []
    print("La lista: ", lista7, " regresa, ", estanOrdenados(lista7))
    print("La lista: ", lista8, " regresa, ", estanOrdenados(lista8))
    print("La lista: ", lista9, " regresa, ", estanOrdenados(lista9))
    print("")
    print("EJERCICIO 4")
    cadena1 = "Mora"
    cadena2 = "RoMa"
    cadena3 = "ANitaLavaLatina"
    cadena4 = "LavaTiNaAniTaLA"
    cadena5 = "hhoola"
    cadena6 = "aalohh"
    print("Las cadenas: ", cadena1, "y", cadena2, " regresan, ", sonAnagramas(cadena1,cadena2))
    print("Las cadenas: ", cadena3, "y", cadena4, " regresan, ", sonAnagramas(cadena3,cadena4))
    print("Las cadenas: ", cadena5, "y", cadena6, " regresan, ", sonAnagramas(cadena5,cadena6))
    print("")
    print("EJERCICIO 5")
    lista10 = [2,2,2,2,2,2,2,2]
    lista11= []
    lista12 = [3,33,333,1,2,4,5]
    print("La lista: ", lista10, " regresa, ", hayDuplicados(lista10))
    print("La lista: ", lista11, " regresa, ", hayDuplicados(lista11))
    print("La lista: ", lista12, " regresa, ", hayDuplicados(lista12))
    print("")
    print("EJERCICIO 6")
    lista13 = [8,8,8,8,8,8,8]
    lista14= []
    lista15 = [1,8,3,4,3,1,8,2,7,8]
    print("La lista: [8,8,8,8,8,8,8] regresa, ", borrarDuplicados(lista13))
    print("La lista: [] regresa, ", borrarDuplicados(lista14))
    print("La lista: [1,8,3,4,3,1,8,2,7,8] regresa, ", borrarDuplicados(lista15))


main()