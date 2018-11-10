#Autor: Víctor Manuel Rodríguez Loyola
#Misión 8

def sumarAcumulado(lista):
    nuevaLista= []
    acumulado=0
    for numeros in lista:
        acumulado+=numeros
        nuevaLista.append(acumulado)
    return nuevaLista


def recortarLista(lista):
    nuevalista= list(lista)
    if len(nuevalista)>0:
       nuevalista.remove(nuevalista[0])
       nuevalista.remove(len(nuevalista)+1)
    return nuevalista


def estanOrdenados(lista):
    resta=lista[len(lista)-1]
    for indice in range(len(lista)-2,-1,-1):
        resta-=lista[indice]
    comparar=(lista[0]-1)*(-1)
    if resta == comparar:
        return True
    else:
        return False


def sonAnagramas(palabra1,palabra2):
    palUno= list(palabra1)
    palDos= list(palabra2)
    if len(palUno)!=len(palDos):
        return False
    else:
        for k in range (len(palUno)):
            if palUno[k] in palDos:
                return True
            else:
                return False


def hayDuplicados(lista):
    duplicados=0
    if len(lista)==0:
        duplicados= False
    for k in lista:
        duplicados= lista.count(k)
        if duplicados>1:
            duplicados=True
            break
        else:
            duplicados= False
    return duplicados


def borrarDuplicados(lista):
    duplicados = 0
    for k in lista:
        duplicados = lista.count(k)
        if duplicados > 1:
            lista.remove(k)
        else:
            continue
    return lista


def main():
    print("Ejercicio 1:")
    print("La lista [1,2,3,4,5] regresa la lista acumulada", sumarAcumulado([1,2,3,4,5]))
    print("La lista [] regresa la lista acumulada", sumarAcumulado([]))
    print("La lista [5] regresa la lista acumulada", sumarAcumulado([5]))
    print("\nEjercicio 2:")
    print("Lista original [1,2,3,4,5], regresa", recortarLista([1,2,3,4,5]))
    print("Lista original [1,2,3], regresa", recortarLista([1, 2, 3]))
    print("Lista original [], regresa", recortarLista([]))
    print("\nEjercicio 3:")
    print("Lista original [1,2,3] regresa", estanOrdenados([1,2,3]))
    print("Lista original [7,23,15] regresa", estanOrdenados([7, 23, 15]))
    print("Lista original [20,21,22] regresa", estanOrdenados([20, 21, 22]))
    print("\nEjercicio 4:")
    print("Al ingresar las palabras Mora y Roma, regresa", sonAnagramas("MORA", "ROMA"))
    print("Al ingresar las palabras Hola y Hello, regresa", sonAnagramas("Hola", "Hello"))
    print("Al ingresar las palabras ana y nana, regresa", sonAnagramas("ana", "nana"))
    print("\nEjercicio 5:")
    print("Lista original [1,2,3,1,4,5], regresa", hayDuplicados([1,2,3,1,4,5]))
    print("Lista original [5,7,4,6,10], regresa", hayDuplicados([5,7,4,6,10]))
    print("Lista original [2,2,3,4,7,8,8], regresa", hayDuplicados([2,2,3,4,7,8,8]))
    print("\nEjercicio 6:")
    print("Lista original [1,8,3,4,3,1,8,2,7,8] regresa", borrarDuplicados([1,8,3,4,3,1,8,2,7,8]))
    print("Lista original [1,1,2,3,4,1] regresa", borrarDuplicados([1,1,2,3,4,1]))
    print("Lista original [4,5,6,7,8,8,7,6,5,4] regresa", borrarDuplicados([4,5,6,7,8,8,7,6,5,4]))


main()