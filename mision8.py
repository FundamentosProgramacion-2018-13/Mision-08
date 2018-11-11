# Danhel Alejandro Mercado Velasco
# Promagra con listas

# Lista con la suma acumulada de los datos
def sumarAcumulado(lista):
    listanueva = []
    suma = 0
    for numero in lista:
        suma = suma + numero
        listanueva.append(suma)
    return listanueva


# Lista que regresa los datos pero sin el primero y último
def recortarLista(lista):
    listarecortada = []
    contador = 0
    for numero in lista:
        if contador != 0 and contador != len(lista)-1:
            listarecortada.append(numero)
        contador += 1
    return listarecortada


# Lista que dice si los valores estan ordenados o no
def estanOrdenados(lista):
    for numero in range(1, len(lista)):
        if lista[numero-1] > lista[numero]:
            return False
    return True

# Lista que dice si los valores son anagramas o no
def sonAnagramas(palabra1,palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    p1=list(palabra1)
    p2=list(palabra2)
    lista = []
    if len(p1)==len(p2):
        for valor in p1:
            if valor in p2:
                lista.append(valor)
    if len(p1) == len(lista):
        return True
    return False


# Lista recive numeros y dice cuales estan duplicados
def hayDuplicados(lista):
    for numero in lista:
        if lista.count(numero)>=2:
            return True
    return False


# Lista que borra los valores duplicados
def borrarDuplicados(lista):
    for n in range(len(lista)-1,-1,-1):
        if lista.count(lista[n])>1:
            lista.remove(lista[n])
    return lista

def main():
    print("""Ejercicio 1
    La lista [1,2,3,4,5] regresa la lista acumulada """, sumarAcumulado([1,2,3,4,5]),
    """La lista [] regresa la lista acumulada """, sumarAcumulado([]),
    """La lista [5] regresa la lista acumulada """, sumarAcumulado([5]))

    print("----------------------------------------------------------------------------")

    print("""Ejercicio 2
    La lista [1,2,3,4,5] regresa la lista acumulada """, recortarLista([1, 2, 3, 4, 5]),
    """La lista [1,2,3] regresa la lista acumulada """, recortarLista([1,2,3]),
    """La lista [] regresa la lista acumulada """, recortarLista([]))

    print("----------------------------------------------------------------------------")

    print("""Ejercicio 3
    La lista [1,2,3,4,5] regresa la lista acumulada """, estanOrdenados([1, 2, 3, 4, 5]),
    """La lista [3,4,5,2,1] regresa la lista acumulada """, estanOrdenados([3,4,5,2,1]),
    """La lista [5,9] regresa la lista acumulada """, estanOrdenados([5,9]))

    print("----------------------------------------------------------------------------")

    print("""Ejercicio 4
    Las palabras roma y mora regresan """, sonAnagramas("Roma","Mora"),
    """Las palabras hola y hello regresan """, sonAnagramas("Hola","Hello"),
    """Las palabras barco y banco regresan """, sonAnagramas("banco","barco"))

    print("----------------------------------------------------------------------------")

    print(""""Ejercicio 5
    La lista [1,2,3,4,5] regresa la lista acumulada """, hayDuplicados([1, 2, 3, 4, 5]),
    """La lista [1,2,2,5,6,3,3] regresa la lista acumulada """, hayDuplicados([1,2,2,5,6,3,3]),
    """La lista [] regresa la lista acumulada """, hayDuplicados([]))

    print("----------------------------------------------------------------------------")

    print("""Ejercicio 6
    La lista [1,8,3,4,3,1,8,2,7,8] regresa la lista acumulada """, borrarDuplicados([1,8,3,4,3,1,8,2,7,8]),
    """La lista [1,2,3,4,5] regresa la lista acumulada """, borrarDuplicados([1,2,3,4,5]),
    """La lista [] regresa la lista acumulada """, borrarDuplicados([]))

main()