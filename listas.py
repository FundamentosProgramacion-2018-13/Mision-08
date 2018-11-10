#Sebastian Macias Ibarra - A01376492
#Ejercicio de listas. Funciones que cumplen con con lo pedido


def sumarAcumulado(lista):
    listaNueva = []    #Se crea una nueva lista
    suma = 0       #Acumulador
    for dato in lista:   #con nun FOR, se le da el rango de la lista
        suma = suma + dato   #Se le suman valroes
        listaNueva.append(suma)   #Inserta el nuevo valor en la lista

    return listaNueva   #Regresa la nueva lista


def recortarLista(lista):
    listaNueva = []    #Nueva lista. A esta se le agregarán los datos
    for k in range(1, len(lista)-1):   #Se crea una lista nueva que comienza en el índice 1. Con  ayuda del FOR visita y agrega valores. Termina uno antres, evitanddo así que se agrege el último valor
        listaNueva.append(lista[k])    #Inserta el nuevo valor en la lista

    return listaNueva  #Regresa la nueva lista


def estanOrdenados(lista):
    variableVerdad = True                #EL valor inicial es verdadero
    for k in range(1, len(lista)):       #Chequeo de que el dato anterior sea menor
        if lista[k] > lista[k-1]:
            variableVerdad = True
        if not lista[k] > lista[k-1] and len(lista) > 2:        #Si no  se cumple la condición, se termina el ptrograma y se declara false
            variableVerdad = False
            break

    return variableVerdad       #Regresa el valor de la variable


def sonAnagramas(palabraA, palabraB):
    palabra1 = palabraA.lower()        #Convierte todas la letras del string en minúsculas
    palabra2 = palabraB.lower()
    valor = 0

    for letra1 in range(0, len(palabra1)):
        for letra2 in range(0, len(palabra2)):
            if palabra1[letra1] == palabra2[letra2]:      #Se analizan y comparan las letras de cada palabra
                valor = 1    #En dado caso que haya una letra igual, crea un brake y sigue en la función
                break

            elif palabra1[letra1] != palabra2[letra2]:      #Si alguna letra no fue encontrada se vuelve falso
                valor = 2

    if valor == 1 and len(palabra1) == len(palabra2):     #Si todas las letras son iguales y tienen la misma longitud es un anagrama
        check = True
        return check

    elif len(palabra1) != len(palabra2):        #Si la longitud de las palabras no son iguales no es un anagrama
        check = False
        return check

    elif valor == 2:              #Si hay una diferente o no hay una letra es falso
        check = False
        return check


def hayDuplicados(lista):
    check = None     #Variabel booleana que tiene valor nulo. Es la que dirá si es True or False

    longitud = len(lista)               #La longitud de la lista se guarda en la variable 1
    sinDobles = len(list(set(lista)))        #Variable que elimina los datos duplicados.

    if longitud == sinDobles:     #Si no hay cambios, es falso
        check = False
    if longitud > sinDobles:       #Si hay cambio es verdadero
        check = True
    return check


def borrarDuplicados(lista):
    lista = list(set(lista))       #Ddentro de la lista, la función "set" se encara de eliminar los valores repetidos en dado caso qque haya
    return lista


def main():
    #Comprueba que la primera funcion funcoiona
    listaEjemplo1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    listaEjemplo2 = [8]
    listaEjemplo3 = []
    print("Ejercicio 1: ")
    print("Lista original", listaEjemplo1, "regresa la lista acumulada", sumarAcumulado(listaEjemplo1))
    print("Lista original", listaEjemplo2, "regresa la lista acumulada", sumarAcumulado(listaEjemplo2))
    print("Lista original", listaEjemplo3, "regresa la lista acumulada", sumarAcumulado(listaEjemplo3))
    print("")

    # Comprueba que la segunda funcion funcoiona
    listaEjemplo4 = [1, 2, 3, 4, 5, 6, 7]
    listaEjemplo5 = [2, 3, 4]
    listaEjemplo6 = []
    print("Ejercicio 2: ")
    print("Lista original", listaEjemplo4, "regresa ", recortarLista(listaEjemplo4))
    print("Lista original", listaEjemplo5, "regresa ", recortarLista(listaEjemplo5))
    print("Lista original", listaEjemplo6, "regresa ", recortarLista(listaEjemplo6))
    print("")

    # Comprueba que la tercera funcion funcoiona
    listaEjemplo7 = [1, 2, 3, 4, 5, 6]
    listaEjemplo8 = [1, 7, 4, 2]
    listaEjemplo9 = [10]
    listaEjemplo10 = []
    print("Ejercicio 3: ")
    print("Lista original", listaEjemplo7, "regresa ", estanOrdenados(listaEjemplo7))
    print("Lista original", listaEjemplo8, "regresa ", estanOrdenados(listaEjemplo8))
    print("Lista original", listaEjemplo9, "regresa ", estanOrdenados(listaEjemplo9))
    print("Lista original", listaEjemplo10, "regresa ", estanOrdenados(listaEjemplo10))
    print("")

    # Comprueba que la cuarta funcion funcoiona
    print("Ejercicio 4:")
    print("Las palabras", "Roma y Mora", "regresa", sonAnagramas("Roma", "Mora"))
    print("Las palabras", "Hola y Hello", "regresa", sonAnagramas("Hola", "Hello"))
    print("Las palabras", "ana y nana", "regresa", sonAnagramas("ana", "nana"))
    print("")

    # Comprueba que la quinta funcion funcoiona
    listaEjemplo11 = [1, 2, 3, 4, 5, 7,  5 ]
    listaEjemplo12 = [5, 7, 4, 6, 10]
    listaEjemplo13 = [2, 3, 2, 5]
    print("Ejercicio 5: ")
    print("Lista original", listaEjemplo11, "regresa ", hayDuplicados(listaEjemplo11))
    print("Lista original", listaEjemplo12, "regresa ", hayDuplicados(listaEjemplo12))
    print("Lista original", listaEjemplo13, "regresa ", hayDuplicados(listaEjemplo13))
    print("")

    # Comprueba que la sexta funcion funcoiona
    listaEjemplo14 = [1, 8, 3, 4, 3, 1, 8, 2, 7, 8, 9, 11, 5, 7, 5, 3, 2, 1, 1, 8]
    listaEjemplo15 = [1, 2, 3, 1, 2, 3, 1, 1, 4, 3, 2]
    listaEjemplo16 = []
    print("Ejercicio 6: ")
    print("La lista", listaEjemplo14, "regresa ", borrarDuplicados(listaEjemplo14))
    print("La lista", listaEjemplo15, "regresa ", borrarDuplicados(listaEjemplo15))
    print("La lista", listaEjemplo16, "regresa ", borrarDuplicados(listaEjemplo16))


main()
