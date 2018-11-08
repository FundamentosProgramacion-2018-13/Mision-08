# encoding: UTF-8
# Autor: Silvia Ferman
# LISTAS


# Funcion que recibe una lista de números enteros y regresa una nueva con la suma acumulada de los datos.
#  suma --> i + 1
def sumarAcumulado(listaUno):
    listaNueva = []
    suma = 0
    for dato in listaUno:
        suma = suma + dato
        listaNueva.append(suma)
    return listaNueva


 # Funcion que recibe una lista de valores enteros y regresa una nueva lista, pero sin el primero y último elemento
def recortarLista(listaDos):
     eliminar = listaDos[1:len(listaDos)-1:]
     return eliminar


# Funcion que recibe una lista de valores, regresa True (valores ordenados) o False (otro caso)
def estanOrdenados(listaTres):
    for k in range(len(listaTres)):
        if k != 0:
            if listaTres[k] < listaTres[k - 1]:
                return False
    else:
        return True

    
# Funcion que recibe 2 cadenas, regresa True (ANAGRAMAS) o False (otro caso)
def sonAnagramas(cadenaUno, cadenaDos):
    cadenaUnoM = list(cadenaUno.upper())
    cadenaDosM = list(cadenaDos.upper())
    cadenaUnoM.sort()
    cadenaDosM.sort()
    if cadenaUnoM == cadenaDosM:
        return True
    else:
        return False

    
# Funcion que recibe una lista de numeros enteros, regresa True (datos copiados) o False (datos unicos)
def hayDuplicados(listaCuatro):
    for dato in listaCuatro:
        aparece = listaCuatro.count(dato)
        if aparece > 1:
            return True
    else:
        return False


# Funcion que recibe una lista de valores enteros y elimina los valores repetidos
# Solo deja un dato de los valores repetidos
def borrarDuplicados(lista):
    lista.sort()
    for dato in lista:
        while lista.count(dato) > 1:
            lista.remove(dato)
        lista=lista
    return lista


# FUNCION PRINCIPAL
def main():
    listaA = [1, 2, 3]
    listaB = [1, 2, 3, 4, 5]
    listaC = [1,2]
    listaD = []
    listaE = [7,23,15]
    listaF = [1,2,3,1,4,5]
    listaG = [5,7,4,6,10]
    listaH =[1,8,3,4,3,1,8,2,7,8]
    listaI = [5]
    listas = [listaA, listaB, listaC, listaD, listaE, listaF, listaG, listaH, listaI]
    print("Ejercicio 1:")
    for lista1 in listas:
        a = sumarAcumulado(lista1)
        print("La lista", lista1, "regresa la lista acumulada", a)
    print()  # Espacio entre ejercicios
    print("Ejercicio 2:")
    for lista2 in listas:
        b = recortarLista(lista2)
        print("La lista original", lista2, "regresa", b)
    print()  # Espacio entre ejercicios
    print("Ejercicio 3:")
    for lista3 in listas:
        valor = estanOrdenados(lista3)
        if valor == True:
            print("La lista", lista3, "Los valores estan ordenados")
        if valor == False:
            print("La lista", lista3, "Los valores NO está ordenados")
    print()  # Espacio entre ejercicios
    print("Ejercicio 4:")
    print("Roma y Mora son ANAGRAMAS (T/F):", sonAnagramas("Roma", "Mora"))
    print("Hola y Hello son ANAGRAMAS (T/F):", sonAnagramas("Hola", "Hello"))
    print("ana y nana son ANAGRAMAS (T/F):", sonAnagramas("ana", "nana"))
    print()  # Espacio entre ejercicios
    print("Ejercicio 5")
    for lista4 in listas:
        valor = hayDuplicados(lista4)
        if valor == True:
            print("La lista", lista4, "Tiene valores duplicados")
        if valor == False:
            print("La lista", lista4, "NO tiene valores duplicados")
    print()  # Espacio entre ejercicios
    print("Ejercicio 6")
    for lista5 in listas:
        e = borrarDuplicados(lista5)
        print("De la lista", lista5, "esta es la que NO tiene duplicados", e)


# Llama a la FUNCION PRINCIPAL
main()
