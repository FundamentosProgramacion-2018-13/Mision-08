#Autor: Samantha MArtínez Franco A01747686
#Ejercicios usando listas


#función que va sumando los numeros en cada posición
def sumarAcumulado(lista):
    acumulados=[]
    suma=0
    for n in lista:
        suma+=n
        acumulados.append(suma)
    return acumulados


#recibe una lista y quita el primero y el ultimo elemento
def recortarLista (lista):
    nuevaLista=lista.copy()
    if lista==[]:
        return lista
    else:
        nuevaLista.pop(0)
        nuevaLista.pop(-1)
        return nuevaLista


#checa si la lista estan ordenandos
def estanOrdenados(lista):
    for k in range(1,len(lista)):
        if lista[k-1]>lista[k]:
            return False
    return True


#checa si dos palabras son anagramas
def sonAnagramas(cadena1, cadena2):
    lista1=list(cadena1)
    lista2=list(cadena2)
    lista1.sort()
    lista2.sort()
    if lista1== lista2:
        return True
    else:
        return False


#checa si en la función hay numeros repetidos
def hayDuplicados(lista):
    for n in lista:
        if lista.count(n)>1:
            return True

    return False


#borra los numeros repetidos
def borrarDuplicados(lista):
    for k in range(len(lista)-1,-1,-1):
        if lista.count(lista[k])>1:
            lista.remove(lista[k])
    return lista



def main():
    print("Ejercicio 1: ")
    a1=[45,6,5]
    print("La lista ",a1 ,"regresa la lista Acumulada ", sumarAcumulado(a1))
    b1=[5]
    print("La lista ", b1, "regresa la lista Acumulada ", sumarAcumulado(b1))
    c1=[]
    print("La lista ", c1, "regresa la lista Acumulada ", sumarAcumulado(c1))
    d1=[1,2,3,4,5,6,7]
    print("La lista ", d1, "regresa la lista Acumulada ", sumarAcumulado(d1))

    print("Ejercicio 2: ")
    a2=[1,2,3,4,5,6]
    print("Lista original", a2 , ", regresa", recortarLista(a2))
    b2=[]
    print("Lista original", b2, ", regresa", recortarLista(b2))
    c2=[2,3,4]
    print("Lista original", c2, ", regresa", recortarLista(c2))
    d2=[34,55,35,65,3]
    print("Lista original", d2, ", regresa", recortarLista(d2))


    print("ejercicio 3: ")
    a3=[1,2,3,4,5]
    print("¿Los datos de la lista ", a3 ," estan ordenados?", estanOrdenados(a3))
    b3=[2,5,1,4]
    print("¿Los datos de la lista ", b3, "?", estanOrdenados(b3))
    c3=[5,4,3,2,1]
    print("¿Los datos de la lista ", c3, "?", estanOrdenados(b3))
    d3=[3,13,24,60]
    print("¿Los datos de la lista ", d3, "?", estanOrdenados(d3))

    print("Ejercicio 4: ")
    a41="amor"
    a42="roma"
    print("La palabra ", a41, "es anagrama de la palabra", a42, sonAnagramas(a41,a42))
    b41="ana"
    b42="nana"
    print("La palabra ", b41, "es anagrama de la palabra", b42, sonAnagramas(b41, b42))
    c41="mora"
    c42="roma"
    print("La palabra ", c41, "es anagrama de la palabra", c42, sonAnagramas(c41, c42))
    d41="hola"
    d42="hello"
    print("La palabra ", d41, "es anagrama de la palabra", d42, sonAnagramas(d41, d42))

    print("Ejercicio 5: ")
    a5 = [1, 2, 4, 3, 3, 3, 3, 4, 4, 5, 5, 6, 8, 6, 7]
    print("La lista ", a5, "tiene duplicados: ", hayDuplicados(a5))
    b5=[22,34,23,5,1,3,4]
    print("La lista ", b5, "tiene duplicados: ", hayDuplicados(b5))
    c5=[1,2,3,4,5,6,7,5]
    print("La lista ", c5, "tiene duplicados: ", hayDuplicados(c5))
    d5=[1,2,3,4,5,6]
    print("La lista ", d5, "tiene duplicados: ", hayDuplicados(d5))

    print("Ejercicio 6: ")
    a6 = [1, 2, 4, 3, 3, 3, 3, 4, 4, 5, 5, 6, 8, 6, 7]
    a6c=a6.copy()
    print("La lista ", a6, "sin duplicados: ", borrarDuplicados(a6c))
    b6 = [22, 34, 23, 5, 1, 3, 4,23,22]
    b6c=b6.copy()
    print("La lista ", b5, "sin duplicados: ", borrarDuplicados(b6c))
    c6 = [1, 2, 3, 4, 5, 6, 7, 5]
    c6c=c6.copy()
    print("La lista ", c5, "sin duplicados: ", borrarDuplicados(c6c))
    d6 = [1, 2, 3, 4, 5, 9,6,7,0,2]
    d6c=d6.copy()
    print("La lista ", d6, "sin duplicados: ", borrarDuplicados(d6c))


main()
