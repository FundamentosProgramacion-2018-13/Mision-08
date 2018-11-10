#encoding: UTF-8
#Misión 8
#Javier Alexandro Vargas Sánchez
#Programa que realiza diversas funciones con listas

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def sumarAcumulado(lista): #Dada una lista, Suma el número de la posición anterior de la lista con el numero de la posición
    #actual
    acumulador = 0

    listaSumada = []


    for numero in lista:
         acumulador += numero
         listaSumada.append(acumulador)

    return listaSumada
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def recortarLista(lista): #Dada una lista, elimina el primer y el último valor de la lista
    if lista == []:
        return lista
    else:
        listaRecortada =[]

        if len(lista) == 2:
            lista = []

            return lista

        for numero in lista:

            if numero == lista[-1] or numero == len(lista)-1: #Condiciona al primer y último valor de la lista
                pass
            else:
                listaRecortada.append(lista[numero])

        return listaRecortada
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def estanOrdenados(lista): # Determina si los números tienen un orden dependiendo de su valor
    condicion = True

    for numero in range(len(lista)):

        if lista[numero - 1] > lista[numero]:
            condicion = False
        else:
            condicion = True
    return condicion
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def sonAnagramas(cadena1, cadena2): #Dadas 2 palabras, detecta si estas son o no anagramas
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()

    palabra1 = list(cadena1)
    palabra2 = list(cadena2)

    condicion = False

    longitud1 = len(palabra1)
    longitud2 = len(palabra2)

    if longitud1 == longitud2: #Condiciona para que las palabras con el mismo numero de letras sigan el proceso

        for letra in palabra1:

            if letra in palabra2:

                condicion = True


    return condicion
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def hayDuplicados(lista): #Detecta si en una lista se repiten números

    condicion = False

    for numero in range(len(lista)):

        lista.count(lista[numero])
        if lista.count(lista[numero]) > 1:
            condicion = True

    return condicion
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def borrarDuplicados(lista):

    for numero in lista:

        while lista.count(numero) > 1: #Condiciona y elimina los valores que se presentan mas de 1 vez en la lista

            lista.remove(numero)

        lista = lista

    return lista

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def main():
    #------------------------------------------------------------------------------------------------Pruebas Ejercicio 1
    listaEj1A = [1,2,3]
    listaEj1B = []
    listaEj1C = [5]

    #------------------------------------------------------------------------------------------------Pruebas Ejercicio 2
    listaEj2A = [1,2,3,4,5]
    listaEj2B =[1,2]
    listaEj2C = []

    #------------------------------------------------------------------------------------------------Pruebas Ejercicio 3
    listaEj3A = [1,2,3]
    listaEj3B = [7,23,15]

    #-------------------------------------------------------------------------------------------------Pruebas Ejericio 4
    palabra1 = "Roma"
    palabra2 = "Mora"
    palabra3 = "Hola"
    palabra4 = "Hello"
    palabra5 = "Ana"
    palabra6 = "nana"

    #------------------------------------------------------------------------------------------------Pruebas Ejercicio 5
    listaEj5A = [1,2,3,1,4,5]
    listaEj5B =[5,4,3,2,1]

    #------------------------------------------------------------------------------------------------Pruebas Ejercicio 6
    listaEj6A = [1,8,3,4,3,1,8,2,7,8]
    listaEj6B = []

    ####################################################################################################################
    print("Ejercicio 1:")
    print("La lista", listaEj1A, "regresa la lista acumulada", sumarAcumulado(listaEj1A))
    print("La lista", listaEj1B, "regresa la lista acumulada", sumarAcumulado(listaEj1B))
    print("La lista", listaEj1C, "regresa la lista acumulada", sumarAcumulado(listaEj1C))
    print()
    ####################################################################################################################
    print("Ejercicio 2:")
    print("La lista original", listaEj2A, ", regresa", recortarLista(listaEj2A))
    print("La lista original", listaEj2B, ", regresa", recortarLista(listaEj2B))
    print("La lista original", listaEj2C, ", regresa", recortarLista(listaEj2C))
    print()
    ####################################################################################################################
    print("Ejercicio 3:")
    print("En la lista", listaEj3A, ", ¿están ordenados los numeros?", estanOrdenados(listaEj3A))
    print("En la lista", listaEj3B, ", ¿están ordenados los numeros?", estanOrdenados(listaEj3B))
    print()
    ####################################################################################################################
    print("Ejercicio 4:")
    print("Las palabras", palabra1, "y", palabra2, "¿son anagramas?",  sonAnagramas(palabra1,palabra2))
    print("Las palabras", palabra3, "y", palabra4, "¿son anagramas?", sonAnagramas(palabra3, palabra4))
    print("Las palabras", palabra5, "y", palabra6, "¿son anagramas?", sonAnagramas(palabra5, palabra6))
    print()
    ####################################################################################################################
    print("Ejercicio 5:")
    print("Dentro de la lista", listaEj5A, "¿existen números que se repiten?", hayDuplicados(listaEj5A))
    print("Dentro de la lista", listaEj5B, "¿existen números que se repiten?", hayDuplicados(listaEj5B))
    print()
    ####################################################################################################################
    print("Ejercicio 6:")
    print("Si a la lista", listaEj6A, "le quitamos los número repetidos, queda así", borrarDuplicados(listaEj6A))
    print("Si a la lista", listaEj6B, "le quitamos los número repetidos, queda así", borrarDuplicados(listaEj6B))
    print()
    ####################################################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
main()