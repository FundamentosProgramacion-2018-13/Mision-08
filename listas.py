#Nombre: Alexys Martín Coate Reyes
#Descripción: Realizar una serie de funciones con base en las listas y sus diferentes operaciones y propiedades.


def sumarAcumulado(lista):
    nuevaLista = []
    copiaLista = lista[:]
    for i in range(len(copiaLista)):
        sumaLista = sum(copiaLista)
        nuevaLista.append(sumaLista)
        copiaLista.pop()
    nuevaLista.reverse()
    return nuevaLista


def recortarLista(lista):
    copiaLista = lista[:]
    if copiaLista != []:
        copiaLista.pop(0)
        if copiaLista != []:
            copiaLista.pop()
    return copiaLista


def estanOrdenados(lista):
    resultado = True
    copiaLista = lista[:]
    for valor in lista:
        copiaLista.pop(0)
        if copiaLista != []:
            if valor < copiaLista[0]:
                continue
            elif valor > copiaLista[0]:
                resultado = False
                break
    return resultado
# QUE PASA SI LA LISTA ESTA VACIA????


def sonAnagramas(str1, str2):
    lista_str1 = set(str1.lower())
    lista_str2 = set(str2.lower())
    resultado = True
    if lista_str1 != lista_str2:
        resultado = False
    return resultado


def hayDuplicados(lista):
    resultado = False
    for dato in lista:
        #print(lista.count(dato))
        if lista.count(dato) > 1:
            resultado = True
            break
    return resultado
# QUE PASA SI LA LISTA ESTA VACIA????


def borrarDuplicados(lista):
    copiaLista = lista[:]
    copiaLista.reverse()
    for dato in copiaLista:
        if lista.count(dato) > 1:
            lista.reverse()
            lista.remove(dato)
            lista.reverse()
    return lista
# QUE PASA SI LA LISTA ESTA VACIA????



def main():
    lista = [1,2,3,4,3,2,1]
    str1 = "Mora"
    str2 = "Roma"

    print("""Ejercicio 1:
            La lista {} regresa la lista acumulada {}
            """.format(lista, sumarAcumulado(lista)))

    print("""Ejercicio 2:
            Lista original {}, regresa  {}
            """.format(lista, recortarLista(lista)))

    print("""Ejercicio 3:
            ¿La lista {} está ordenada? {}
            """.format(lista, estanOrdenados(lista)))

    print("""Ejercicio 4:
            ¿{} y {} son anagramas? {}
            """.format(str1,str2, sonAnagramas(str1,str2)))

    print("""Ejercicio 5:
            ¿La lista {} tiene duplicados? {}
            """.format(lista, hayDuplicados(lista)))

    print("""Ejercicio 6:
            Lista original {} : Lista sin duplicados {}
            """.format(lista, borrarDuplicados(lista)))

"""
    a = sumarAcumulado(lista)
    print(a)
    b = recortarLista(lista)
    print(b)
    c = estanOrdenados(lista)
    print(c)
    e = sonAnagramas("amor", "ROMA")
    print(e)
    f = hayDuplicados(lista)
    print(f)
    g = borrarDuplicados(lista)
    print(g)
"""
main()