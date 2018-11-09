#Autor: Zoe Caballero Dominguez A01747247 Grupo 04
# Descripcion: Varias funciones utilizando listas


# Acumula la sumatoria de los numeros de una lista dada y devuelve una nueva lista
def sumarAcumulado(lista):
    k = 0
    nuevaLista = []
    for n in lista:
        k += n
        nuevaLista.append(k)
    return nuevaLista


#Crea una nueva lista a partir de los elementos de otra lista, excepto por el primer y último número
def recortarLista(lista):
    nuevaLista = []
    for k in range (len(lista)):
        if k == 0 or k == len(lista)-1:
            pass
        else:
            nuevaLista.append(lista[k])
    return nuevaLista


# Determina si los elementos de una lista están ordenados de menor a menor
def estanOrdenados (lista):
    condicion = 1
    primerElemento = lista[0]
    for dato in lista:
        if dato >= primerElemento:
            primerElemento = dato
            condicion = 1
        else:
            condicion = 0

    if condicion == 1:
        return True
    else:
        return False


#Determina si dos palabras son anagramas
def sonAnagramas (cadena1, cadena2):
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()
    lista1 = list(cadena1)
    lista2 = list(cadena2)
    nuevaLista=[]
    if len(cadena1)!= len(cadena2):
        return False
    else:
        for k in lista2:
            if k in lista1:
                nuevaLista.append(k)
            else:
                pass
        if nuevaLista == lista2:
            return True
        else:
            return False


#Determina si un elemento de una lista se repite
def hayDuplicados(lista):
     for k in lista:
         veces = lista.count(k)
         if veces >= 2:
             return True
         else:
             return False


#Elimina los elementos duplicados de una lista
def borrarDuplicados(lista):
    for k in range(len(lista)-1,-1,-1):
        dato = lista[k]
        duplicado = lista.count(dato)
        if duplicado > 1:
            lista.remove(dato)


# Función main, incluye varias pruebas de cada función
def main():
    #Prueba Funcion acummulados
    listaPrueba1 = [1,2,3,4,5]
    listaPrueba2 = []
    listaPrueba3 = [5]
    print("Ejercicio 1:")
    print("La lista", listaPrueba1, "regresa la lista acumulada", sumarAcumulado(listaPrueba1))
    print("La lista", listaPrueba2, "regresa la lista acumulada", sumarAcumulado(listaPrueba2))
    print("La lista", listaPrueba3, "regresa la lista acumulada", sumarAcumulado(listaPrueba3))
    print("")

    #Prueba Funcion recortarLista
    print("Ejercicio 2:")
    listaPrueba4 = [1,2,3]
    print("Lista original", listaPrueba1, "regresa", recortarLista(listaPrueba1))
    print("Lista original", listaPrueba4, "regresa", recortarLista(listaPrueba4))
    print("Lista original", listaPrueba2, "regresa", recortarLista(listaPrueba2))
    print("")

    #Prueba funcion estanOrdenados
    listaPrueba5 = [7,23,15]
    listaPrueba6 = [0,1,9,4]
    print("Ejercicio 4:")
    print("¿La lista original", listaPrueba1, "está ordenada?",estanOrdenados(listaPrueba1))
    print("¿La lista original", listaPrueba5, "está ordenada?", estanOrdenados(listaPrueba5))
    print("¿La lista original", listaPrueba6, "está ordenada?", estanOrdenados(listaPrueba6))
    print("")

    #Prueba funcon sonAnagramas
    cadena1Prueba1 =  "Roma"
    cadena2Prueba1 = "Amor"
    cadena1Prueba2 = "frase"
    cadena2Prueba2 = "fresa"
    cadena1Prueba3 = "Ana"
    cadena2Prueba3 = "nana"
    print("Ejercicio 4:")
    print("¿Las palabras:", cadena1Prueba1, "y", cadena2Prueba1, "son anagramas?", sonAnagramas(cadena1Prueba1, cadena2Prueba1))
    print("¿Las palabras:", cadena1Prueba2, "y", cadena2Prueba2, "son anagramas?", sonAnagramas(cadena1Prueba2, cadena2Prueba2))
    print("¿Las palabras:", cadena1Prueba3, "y", cadena2Prueba3, "son anagramas?", sonAnagramas(cadena1Prueba3, cadena2Prueba3))
    print("")

    #Prueba funcuin hay Duplicados
    listaPrueba7 = [1,2,3,1,4,5]
    listaPrueba8 = [5,5,3,4,7]
    print("Ejercicio 5:")
    print("¿En la lista", listaPrueba7, "hay duplicados?", hayDuplicados(listaPrueba7))
    print("¿En la lista", listaPrueba8, "hay duplicados?", hayDuplicados(listaPrueba8))
    print("¿En la lista", listaPrueba1, "hay duplicados?", hayDuplicados(listaPrueba1))
    print("")

    #Prueba funcion borrarDuplicados
    listaPruebaDuplicados = [1,8,3,4,3,1,8,7,8]
    print("Ejercicio 6:")
    print("Lista antes de la función:", listaPruebaDuplicados)
    borrarDuplicados(listaPruebaDuplicados)
    print("Lista despues de la función:", listaPruebaDuplicados)


#Llamar a la función
main()