#Autor: Daniel Cordova Bermudez a01377242
#Grupo 02
#Mision 8: Serie de ejercicios que usan y manipulan listas para modificar los numeros dentro de ellas.


#Función sumarAcumulado se encarga de recibir una lista la cual suma los numeros y regresa una lista con la suma.
def sumarAcumulado(lista):

    suma = 0
    sumaLista = []
    for numero in lista:
        suma += numero
        sumaLista.append(suma)
    return sumaLista


#Función recortarLista se encarga de recortar el primero y ultimo numero de la lista.
def recortarLista(lista):

    listaRecortada = lista[1:(len(lista) - 1)]
    return listaRecortada


#Función estarOrdenados verifica si una lista se encuentra en orden.
def estanOrdenados(lista):

    for numero in range(1,len(lista)):
        if lista[numero-1]>lista[numero]:
            return False
    return True


#Función sonAnagramas verifica si dos strings/cadenas son anagramas.
def sonAnagramas(string1,string2):

    lista1=list(string1)
    lista2=list(string2)
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    else:
        return False


#Función hayDuplicados verifica si hay mas de un mismo numero dentro una lisa.
def hayDuplicados(lista):

    for numero in lista:
        if lista.count(numero) > 1:
            return True
    return False


#Función borrarDuplicados se encarga de borrar los numeros que se repiten en una lista.
def borrarDuplicados(lista):

    lista.sort()
    for numero in lista:
        while lista.count(numero) > 1:
            lista.remove(numero)
    return lista


#Funcion main, imrpime la informacion y llama a las demas funciones.
def main():

    print("Ejercicio 1:")
    a=[1, 2, 3]
    print("Lista original:", a ,"regresa la lista acumulada", sumarAcumulado(a))
    b = [1, 2]
    print("Lista original:", b, "regresa la lista acumulada", sumarAcumulado(b))
    print("Lista original: [] regresa la lista acumulada", sumarAcumulado([]))

    print("")
    print("Ejercicio 2:")
    c= [1, 2, 3, 4, 5]
    print("Lista original:", c ,"regresa la lista recortada", recortarLista(c))
    d= [1,2]
    print("Lista original:", d," regresa la lista recortada", recortarLista(d))
    print("Lista original: [] regresa la lista recortada", recortarLista([]))

    print("""
    Ejercicio 3:""")
    print("Lista original: [1,2,3,4,]. La lista tiene un orden: ", estanOrdenados([1, 2, 3, 4]))
    print("Lista original: [7,23,15]. La lista tiene un orden: ", estanOrdenados([7,23,15]))

    print("""
    Ejercicio 4:""")
    print("¿Las palabras mora y roma son anagramas?: ", sonAnagramas("roma", "mora"))
    print("¿Las palabras hola y hello son anagramas?:", sonAnagramas("hola", "hello"))
    print("¿Las palabras hola y hello son anagramas?: ", sonAnagramas("ana", "nana"))

    print("""
    Ejercicio 5:""")
    print("Lista original: [1, 2, 3, 1, 4, 5]. ¿Hay duplicados en la lista?: ", hayDuplicados([1, 2, 3, 1, 4, 5]))
    print("Lista original: [5,7,4,6,10]. ¿Hay duplicados en la lista?: ", hayDuplicados([5,7,4,6,10]))
    print("Lista original: []. ¿Hay duplicados en la lista?: ", hayDuplicados([]))

    print("""
    Ejercicio 6:""")
    print("Lista original: [1,2,3,3,3,3,3] regresa la lista sin duplicados",borrarDuplicados([1, 2, 3, 3, 3, 3, 3]))
    print("Lista original: [1,2,3,10] regresa la lista sin duplicados", borrarDuplicados([1, 2, 3, 10]))
    print("Lista original: [2,2,2,2,1,1,1,3] regresa la lista sin duplicados", borrarDuplicados([2,2,2,2,1,1,1,3]))


main()