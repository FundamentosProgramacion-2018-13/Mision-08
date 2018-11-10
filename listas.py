def sumarAcumulado(numeros):
    lista = []
    suma = 0
    for numero in numeros:
        suma += numero
        lista.append(suma)
    return lista


def recortarLista(numeros):
    lista = []
    for numero in range(2,len(numeros)):
        lista.append(numero)
    return lista


def estanOrdenados(numeros):
    for numero in range(1,len(numeros)):
        if numeros[numero] < numeros[numero-1]:
                return "False"
    return "True"


def sonAnagramas(palabra1,palabra2):
    lista1 = list(palabra1)
    lista2 = list(palabra2)
    lista1 = sorted(lista1)
    lista2 = sorted(lista2)

    return (lista1==lista2)


def hayDuplicados(numeros):
    for numero in numeros:
        if numeros.count(numero)>1:
            return "True"
        else:
            return "False"
    return "False"


def borrarDuplicados(numeros):
    numeros = list(set(numeros))
    return numeros


def main():
    print("Ejercicio 1:")
    print("La lista [1,2,3,4,5] regresa la suma acumulada de:",sumarAcumulado([1,2,3,4,5]))
    print("La lista [] regresa la suma acumulada de:", sumarAcumulado([]))
    print("La lista [5] regresa la suma acumulada de:", sumarAcumulado([5]))

    print("Ejercicio 2:")
    print("La lista original [1,2,3,4,5] regresa la lista recortada:",recortarLista([1,2,3,4,5]))
    print("La lista original [1,2] regresa la lista recortada:", recortarLista([1, 2]))
    print("La lista original [] regresa la lista recortada:", recortarLista([]))

    print("Ejercicio 3:")
    print("La lista [1,2,3] ¿Está ordenada?",estanOrdenados([1,2,3]))
    print("La lista [7,23,15] ¿Está ordenada?", estanOrdenados([7, 23, 15]))

    print("Ejercicio 4:")
    print("Las palabras ANA y NANA ¿son Anagramas?", sonAnagramas("ana","nana"))
    print("Las palabras ROMA y MORA ¿son Anagramas?", sonAnagramas("roma", "mora"))
    print("Las palabras HOLA y HELLO ¿son Anagramas?", sonAnagramas("hola", "hello"))

    print("Ejercicio 5:")
    print("En la lista [1,2,3,4,5] ¿hay duplicados?", hayDuplicados([1,2,3,4,5]))
    print("En la lista [1,1,2,3,5,4,6,2] ¿hay duplicados?", hayDuplicados([1,1,2,3,5,4,6,2]))

    print("Ejercicio 6:")
    print("La lista [1,2,3,4,5] sin duplicados es:", borrarDuplicados([1, 2, 3, 4, 5]))
    print("La lista [1,6,4,8,3,1,3,6,8,90,23,12,4,6,67,3,5,6,7,8,4,6,2,8,6,4,2,5,4,3] sin duplicados es:", borrarDuplicados([1,6,4,8,3,1,3,6,8,90,23,12,4,6,67,3,5,6,7,8,4,6,2,8,6,4,2,5,4,3]))


main()