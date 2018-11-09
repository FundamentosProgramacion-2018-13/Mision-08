#Jocelyn López Ortía A01377451
#Listas

def sumarAcumulado(lista):
    nuevoNumero = 0
    listaAcumulada = []
    for dato in lista:
        nuevoNumero += dato
        listaAcumulada.append(nuevoNumero)
    return listaAcumulada


def recortarLista(lista):
    counter = 0
    listaRecortada = []
    for dato in lista:
        if counter != 0 and counter != len(lista)-1:
            listaRecortada.append(dato)
        counter +=1
    return listaRecortada


def estanOrdenados(lista):
    numeroAnterior = lista[0]
    for dato in lista:
        if dato < numeroAnterior:
            return False
        numeroAnterior = dato
    return True


def sonAnagramas(palabra1,palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    p1=list(palabra1)
    p2=list(palabra2)
    lista = []
    if len(p1)==len(p2):
        for dato in p1:
            if dato in p2:
                lista.append(dato)
    if len(p1) == len(lista):
        return True
    return False


def hayDuplicados(lista):
    for dato in lista:
        if lista.count(dato)>=2:
            return True
    return False


def borrarDuplicados(lista):
    for k in range(len(lista) - 1, -1, -1):
        if lista.count(lista[k]) >= 2:
            lista.remove(lista[k])
    return lista



def main():
    print("Ejercicio 1")
    print("La lista [1,2,3,4,5] regresa la lista acumulada ", sumarAcumulado([1,2,3,4,5]))
    print("La lista [] regresa la lista acumulada ", sumarAcumulado([]))
    print("La lista [5] regresa la lista acumulada ", sumarAcumulado([5]))

    print()
    print("Ejercicio 2")
    print("La lista [1,2,3,4,5] regresa la lista acumulada ", recortarLista([1, 2, 3, 4, 5]))
    print("La lista [1,2,3] regresa la lista acumulada ", recortarLista([1,2,3]))
    print("La lista [] regresa la lista acumulada ", recortarLista([]))

    print()
    print("Ejercicio 3")
    print("La lista [1,2,3,4,5] regresa la lista acumulada ", estanOrdenados([1, 2, 3, 4, 5]))
    print("La lista [3,4,5,2,1] regresa la lista acumulada ", estanOrdenados([3,4,5,2,1]))
    print("La lista [5,9] regresa la lista acumulada ", estanOrdenados([5,9]))

    print()
    print("Ejercicio 4")
    print("Las palabras roma y mora regresan ", sonAnagramas("Roma","Mora"))
    print("Las palabras rosa y mora regresan ", sonAnagramas("rosa","mora"))
    print("Las palabras casa y saca regresanaa ", sonAnagramas("casa", "saca"))

    print()
    print("Ejercicio 5")
    print("La lista [1,2,3,4,5] regresa la lista acumulada ", hayDuplicados([1, 2, 3, 4, 5]))
    print("La lista [1,2,2,5,6,3,3] regresa la lista acumulada ", hayDuplicados([1,2,2,5,6,3,3]))
    print("La lista [] regresa la lista acumulada ", hayDuplicados([]))

    print()
    print("Ejercicio 6")
    print("La lista [1,2,2,2,3,3,4,5,2] regresa la lista acumulada ", borrarDuplicados([1,2,2,2,3,3,4,5,2]))
    print("La lista [1,2,3] regresa la lista acumulada ", borrarDuplicados([1, 2, 3]))
    print("La lista [] regresa la lista acumulada ", borrarDuplicados([]))


main()