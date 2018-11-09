# Autor: Roberto Emmanuel González Muñoz
# Solución de problemas con listas.
from random import randint


# Genera un lista de números enteros.
def generarLista(n):
    lista = []
    for k in range(n):
        azar = randint(0, 255)
        lista.append(azar)
    return lista


# Regresa una nueva lista con la suma acumulada de datos.
def sumarAcumulado(listaEnteros):
    lista = []
    acumulado = 0
    for value in (listaEnteros):
        acumulado += value
        lista.append(acumulado)
    return lista


# Regresa una nueva lista pero, sin el primero y último elemento.
def recortarLista(listaEnteros):
    lista = []
    lista = listaEnteros[1:(len(listaEnteros)-1)]
    return lista


# True si los valores están ordenados, False en otro caso.
def estanOrdenados(listaReales):
    i = 0
    for k in listaReales:
        if k >= i:
            i = k
            a = True
        elif k < i:
            a = False
            return a
    return a


# True si son Anagramas, False en otro caso.
def sonAnagramas(cadena1,cadena2):
    listaA = list(cadena1)
    listaB = list(cadena2)
    sumaAB = 0
    if len(listaA) == len(listaB):
        for k in range(len(listaA)):
            for i in range(len(listaB)):
                letraenB = listaB.count(k)
                letraenA = listaA.count(k)
                sumaAB += letraenB + letraenA
                if letraenA != letraenB:
                    return False
                elif sumaAB % 2 != 0:
                    return False
        if sumaAB % 2 == 0:
            return True
    else:
        return False


# True si alguno de los datos está duplicado, False en otro caso.
def hayDuplicados(listaEnteros):
    lista = set(listaEnteros)
    for k in lista:
        cuenta = listaEnteros.count(k)
        if cuenta > 1:
            return True
    return False

# Elimina los valores duplicados en la lista a excepción del primero.
def borrarDuplicados(listaEnteros):
    lista = set(listaEnteros)
    for k in lista:
        cuenta = listaEnteros.count(k)
        if cuenta > 1:
            listaEnteros.remove(k)
    return listaEnteros


# Función que imprime los resultados de cada función con el formato correspondiente.
def imprimirExe(listaEnteros, listaReales, sumaAcumulada, listaRecortada, orden, anagrama, duplicado,
                listaNoDuplicados):

    # Imprimir funciones.
    print("___________________________________________________________________________________________________________")
    print("Ejercicio 1: ")
    print("La lista %s regresa la lista acumulada %s" % (listaEnteros, sumaAcumulada))
    print("___________________________________________________________________________________________________________")
    print("Ejercicio 2: ")
    print("La lista original %s , regresa %s" % (listaEnteros, listaRecortada))
    print("___________________________________________________________________________________________________________")
    print("Ejercicio 3: ")
    print("En la lista %s, hay orden? %s " % (listaReales, orden))
    print("___________________________________________________________________________________________________________")
    print("Ejercicio 4: ")
    print("Existe un anagrama? %s" % anagrama)
    print("___________________________________________________________________________________________________________")
    print("Ejercicio 5: ")
    print("La lista %s contiene duplicados? %s" % (listaEnteros,duplicado))
    print("___________________________________________________________________________________________________________")
    print("Ejercicio 6: ")
    print("Lista sin valores duplicados", listaNoDuplicados)
    print("___________________________________________________________________________________________________________")


def main():
    # Lista de números enteros y decimales.
    n = randint(0, 4)
    listaEnteros = generarLista(n)
    listaReales = listaEnteros

    # Cadena uno y dos para prueba de Anagrama.
    cadena1 = "Mary"
    cadena2 = "Army"

    # Llamado y almacenamiento de las funciones.
    sumaAcumulada = sumarAcumulado(listaEnteros)
    listaRecortada = recortarLista(listaEnteros)
    orden = estanOrdenados(listaReales)
    anagrama = sonAnagramas(cadena1, cadena2)
    duplicado = hayDuplicados(listaEnteros)
    listaNoDuplicados = borrarDuplicados(listaEnteros)

    # Imprime los resultados en patalla.
    imprimirExe(listaEnteros,listaReales,sumaAcumulada,listaRecortada,orden,anagrama,duplicado,listaNoDuplicados)


main()