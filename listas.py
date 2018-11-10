# Autor: Ithan Alexis Pérez Sánchez
# Matrícula: A01377717
# Descripción: Misión 08 Listas de Python.

# El codigo empieza después de esta linea

def sumarAcumulado(listas):
    lista = []
    i = 0
    for k in listas:
        i += k
        lista.append(i)
    return lista

def recortarLista(listas):
    lista = []
    for k in range(2, len(listas)):
        lista.append(k)
    return lista

def estanOrdenados(listas):
    if listas == sorted(listas):
        return "True"
    else:
        return "False"

def sonAnagramas(palabra1, palabra2):
    local = 0

    if len(palabra1) == len(palabra2):
        for x in palabra1.upper():
            for y in palabra2.upper():
                if x == y:
                    local += 1
    if local == len(palabra1):
        return True
    return False


def hayDuplicados(listas):

    for k in listas:
        dobles = listas.count(k)
        if dobles > 1:
            return True
    return False

def borrarDuplicados(listas):

    lista = list(set(listas))
    return lista


def main():
    prueba = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    prueba2 = []
    prueba3 = [5]

    print("Ejercicio 1: ")
    print("La lista", prueba, "regresa la lista acumulada", sumarAcumulado(prueba))
    print("La lista", prueba2, "regresa la lista acumulada", sumarAcumulado(prueba2))
    print("La lista", prueba3, "regresa la lista acumulada", sumarAcumulado(prueba3))

    print("")

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numeros2 = [1, 2]
    numeros3 = []

    print("Ejercicio 2: ")
    print("Lista original", numeros, "regresa", recortarLista(numeros))
    print("Lista original", numeros2, "regresa", recortarLista(numeros2))
    print("Lista original", numeros3, "regresa", recortarLista(numeros3))

    print("")

    valor = [1, 2, 3]
    valor2 = [7, 23, 15]
    valor3 = []

    print("Ejercicio 3: ")
    print("Lista principal", valor, "¿Se encuentra ordenada?", estanOrdenados(valor))
    print("Lista principal", valor2, "¿Se encuentra ordenada?", estanOrdenados(valor2))
    print("Lista principal", valor3, "¿Se encuentra ordenada?", estanOrdenados(valor3))

    print("")

    palabra1 = "Roma"
    palabra2 = "Mora"
    palabra3 = "Hola"
    palabra4 = "Hello"

    print("Ejercicio 4: ")
    print("Las palabras", palabra1, palabra2, "¿Son anagramas?", sonAnagramas(palabra1, palabra2))
    print("Las palabras", palabra3, palabra4, "¿Son anagramas?", sonAnagramas(palabra3, palabra4))

    print("")

    termino = [1, 2, 3, 1, 4, 5]
    termino2 = [5, 7, 4, 6, 10]

    print("Ejercicio 5: ")
    print("En la Lista", termino, "¿Hay duplicados?", hayDuplicados(termino))
    print("En la Lista", termino2, "¿Hay duplicados?", hayDuplicados(termino2))

    print("")

    datos = [1, 8, 3, 4, 3, 1, 8, 2, 7, 8]

    print("Ejercicio 6: ")
    print("La lista hay valores duplicados", datos, "elimina los duplicados y deja cuales son", borrarDuplicados(datos))


main()