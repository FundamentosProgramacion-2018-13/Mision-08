# Autor : Saúl Figueora Conde.
# Matrícula: A01747306.
# Grupo 02.
# Descripción: Éste programa resuelve 6 ejercicios que aplican los conocimientos obtenidos acerca del uso de listas en
# python.
#----------------------------------------------------------------------------------------------------------------------
from random import randint


# Se declara la función sumarAcumulado que recibe como parámetro una lista de números enteros y regresa una nueva lista
# con la suma acumulada de los datos.
def sumarAcumulado(lista):
    nuevaLista = []
    contador = 0
    L = len(lista)
    suma = 0

    for i in range(0, L):
        suma = 0

        if contador == 0:
            nuevaLista.append(lista[i])
            contador += 1
        else:
            for j in range(0, i+1):
                suma += lista[j]
            nuevaLista.append(suma)

    return nuevaLista


# Se declara la función recortarLista que recibe como par;ametro una lista de valores enteros y regresa una nueva lista
# sin el primero y el último elemento.
def recortarLista(lista):
    nuevaLista = []
    n = len(lista)

    if len(lista) == 0 or len(lista) == 1:
        nuevaLista = []

    else:
        for elemento in range(1, n - 1):
            nuevaLista.append(lista[elemento])

    return nuevaLista


# Se declara la función estanOrdenados que recibe como parámetro una lista de valores y regresa True si los valores
# están ordenados, False en otro caso.
def estanOrdenados(lista):
    nuevaLista = False
    n = len(lista)
    counter = 0
    counter2 = 0

    if n == 0 or n == 1:
        nuevaLista = True

    for elementos in range(0, n-1):

        if lista[elementos] <= lista[elementos+1]:
            counter += 1

    if counter == n-1:
        nuevaLista = True

    if nuevaLista == False:
        for elementos in range(0, n - 1):

            if lista[elementos] >= lista[elementos + 1]:
                counter2 += 1

        if counter2 == n - 1:
            nuevaLista = True
    return nuevaLista


# Se declara la función sonAnagramas que recibe como parámetros dos cadenas. Regresa True si son anagramas, False
# en otro caso.
def sonAnagramas(palabraA, palabraB):
    resultado = True
    n1 = len(palabraA)
    n2 = len(palabraB)
    counter_check = 0

    palabraUno = palabraA.upper()
    palabraDos = palabraB.upper()

    if n1 != n2:
        resultado = False
        return resultado

    for caracteresA in range(0, n1):
        for caracteresB in range(0, n2):
            if palabraUno[caracteresA] == palabraDos[caracteresB]:
                counter_check = 1
        if counter_check == 1:
            counter_check = 0
        else:
            resultado = False
            return resultado
    return resultado


# Se declara la función hayDuplicados que recibe como parámetro una lista de números enteros y regresa True si
# alguno de sus datos está duplicado, False si todos son únicos.
def hayDuplicados(lista):
    n = len(lista)
    existenDuplicados = False
    numberCounter = 0

    if n == 1:
        existenDuplicados = False
        return existenDuplicados

    for i in range(0, n):
        numberCounter = 0
        for j in range (0, n):
            if lista[i] == lista[j]:
                numberCounter += 1
        if numberCounter >= 2:
            existenDuplicados = True

    return existenDuplicados


# Se declara la función borrarDuplicados que recibe como parámetro una lista de valores enteros y elimina de ésta
# los valores repetidos (dejando solo uno del conjunto de repetidos).
def borrarDuplicados(lista):
    n = len(lista)
    existenDuplicados = False
    numberCounter = 0
    duplicados_check = True

    if n == 1:
        existenDuplicados = False
        return lista

    for i in range(0, n):
        numberCounter = 0
        for j in range(0, n):
            if lista[i] == lista[j]:
                numberCounter += 1
        if numberCounter >= 2:
            existenDuplicados = True

    if existenDuplicados == True:
        for x in range(0, n):
            numberCounter = 0
            for y in range(0, n):
                if lista[y] == lista[x]:
                    numberCounter += 1
            if numberCounter >= 2:
                lista.remove(lista[x])
                break

    else:
        return lista

    while duplicados_check == True:
        duplicados_check = hayDuplicados(lista)
        lista1 = borrarDuplicados(lista)

    return lista


# Se declara la función main. Aquí se prueban cada una de las funciones con varios casos para demostrar que el programa
# funciona correctamente
def main():
    lista1 = []
    lista2 = []
    lista3 = [] # se queda vacía
    escribirLista = True
    k = randint(0, 11)

    numeroElementos = int(float(input("Agregue el número de valores que tendrá la lista: ")))
    if numeroElementos <= 0:
        main()

    while escribirLista == True:
        numero = abs(int(float(input("Agregue un valor numérico a esta lista: "))))
        lista1.append(numero)
        numeroElementos -= 1
        if numeroElementos <= 0:
            escribirLista = False

    for i in range(k):
        i = randint(0, 11)
        lista2.append(i)

    nuevaLista1 = sumarAcumulado(lista1)
    nuevaLista2 = sumarAcumulado(lista2)
    nuevaLista3 = sumarAcumulado(lista3)

    print("Ejercicio 1: ")
    print("La lista {} regresa la lista acumulada {}".format(lista1, nuevaLista1))
    print("La lista {} regresa la lista acumulada {}".format(lista2, nuevaLista2))
    print("La lista {} regresa la lista acumulada {}".format(lista3, nuevaLista3))

    print("")

    pausa = input("Pausa...")

    nuevaLista1 = recortarLista(lista1)
    nuevaLista2 = recortarLista(lista2)
    nuevaLista3 = recortarLista(lista3)

    print("Ejercicio 2: ")
    print("Lista original {}, regresa {}".format(lista1, nuevaLista1))
    print("Lista original {}, regresa {}".format(lista2, nuevaLista2))
    print("Lista original {}, regresa {}".format(lista3, nuevaLista3))

    print("")

    pausa = input("Pausa...")

    nuevaLista1 = estanOrdenados(lista1)
    nuevaLista2 = estanOrdenados(lista2)
    nuevaLista3 = estanOrdenados(lista3)

    print("Ejercicio 3: ")
    print("La lista {} está ordenada: {}".format(lista1, nuevaLista1))
    print("La lista {} está ordenada: {}".format(lista2, nuevaLista2))
    print("La lista {} está ordenada: {}".format(lista3, nuevaLista3))

    print("")

    pausa = input("Pausa...")

    palabraA = input("Escriba la primera palabra: ")
    palabraB = input("Escriba la segunda palabra: ")

    resultado = sonAnagramas(palabraA, palabraB)

    print("")
    print("Ejercicio 4: ")
    print("{} y {} son anagramas: {}".format(palabraA, palabraB, resultado))

    palabraA = ""
    palabraB = ""

    resultado = sonAnagramas(palabraA, palabraB)

    print("{} y {} son anagramas: {}".format(palabraA, palabraB, resultado))
    print("")

    palabraA = "Hola"
    palabraB = "Hola"

    resultado = sonAnagramas(palabraA, palabraB)

    print("{} y {} son anagramas: {}".format(palabraA, palabraB, resultado))
    print("")

    palabraA = "AgRa"
    palabraB = "raag"

    resultado = sonAnagramas(palabraA, palabraB)

    print("{} y {} son anagramas: {}".format(palabraA, palabraB, resultado))
    print("")

    palabraA = "mam"
    palabraB = "mim"

    resultado = sonAnagramas(palabraA, palabraB)

    print("{} y {} son anagramas: {}".format(palabraA, palabraB, resultado))
    print("")

    pausa = input("Pausa...")

    nuevaLista1 = hayDuplicados(lista1)
    nuevaLista2 = hayDuplicados(lista2)
    nuevaLista3 = hayDuplicados(lista3)

    print("Ejercicio 5: ")
    print("La lista {}, tiene duplicados: {}".format(lista1, nuevaLista1))
    print("La lista {}, tiene duplicados: {}".format(lista2, nuevaLista2))
    print("La lista {}, tiene duplicados: {}".format(lista3, nuevaLista3))

    print("")

    pausa = input("Pausa...")

    lista1 = borrarDuplicados(lista1)

    lista2 = borrarDuplicados(lista2)

    lista3 = borrarDuplicados(lista3)

    print("Ejercicio 6: ")
    print("La lista, al borrar los duplicados, queda así: {} ".format(lista1))
    print("La lista, al borrar los duplicados, queda así: {} ".format(lista2))
    print("La lista, al borrar los duplicados, queda así: {} ".format(lista3))

    pausa = input("Salir...")


# Se llama a la función main para que corra el programa.
main()