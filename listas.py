# Autora: Mariana Caballero Cabrera  A01376544

#Programa con varias funciones que trabajan con listas


#Función que recibe como parámetro una lista de números enteros y regresa UNA NUEVA lista con la suma acumulada de los datos
def sumarAcumulado (listaEnteros):
    nuevaLista = []
    nuevoDato=0
    for dato in listaEnteros:
        nuevoDato +=dato
        nuevaLista.append(nuevoDato)

    return nuevaLista


# Función que recibe como parámetro una lista de valores enteros y regresa una nueva lista, pero sin el primero y último elemento
def recortarLista (listaEnteros3):
    nuevaLista = []
    for dato in listaEnteros3:
        if dato != listaEnteros3[0] and dato != listaEnteros3[-1]:
            nuevaLista.append(dato)

    return nuevaLista


#Función que recibe una lista de valores y regresa True si los valores están ordenados, False en otro caso.
def estanOrdenados (listaNumeros):
    b=0
    if listaNumeros == []:
        b="No hay datos"
    else:
        if min (listaNumeros)==listaNumeros[0] and max(listaNumeros)==listaNumeros[-1] :
         b = "True"

        else:
         b = "False"


    return b


# Función que recibe dos cadenas como parámetros, regresa True si son anagramas,False en otro caso
def sonAnagramas (n,m):
    a="No hay palabras"
    n=n.lower()
    m=m.lower()
    z=list(n)
    y=list(m)
    for dato in z:
        if dato in y and len(z)==len(y):
            a = "True"
        else:
            a = "False"

    return a


# Función  que recibe una lista de números enteros, regresa True si alguno de sus datos está duplicado, False si todos son únicos
def hayDuplicados (listaNumeros2):
    c="No hay datos"
    for n in listaNumeros2:
        if listaNumeros2.count(n)>=2:
            c = "True"
        else:
            c = "False"

    return c


#Función que recibe una lista de valores enteros y elimina de ésta los valores repetidos (solo deja uno del conjunto de repetidos).
def borrarDuplicados (listaNumeros13):
    for k in range(len(listaNumeros13) - 1, -1, -1):
        if listaNumeros13.count(listaNumeros13[k]) > 1:
            listaNumeros13.remove(listaNumeros13[k])

#Función principal
def main ():
    print("")
    print("Ejercicio 1:")
    listaEnteros1 = [1,2,3,4,5]
    listaEnteros2= []
    listaEnteros3 = [5]
    sA1=sumarAcumulado(listaEnteros1)
    sA2 = sumarAcumulado(listaEnteros2)
    sA3 = sumarAcumulado(listaEnteros3)
    print ("La lista",listaEnteros1,"regresa la lista acumulada",sA1)
    print("La lista",listaEnteros2,"regresa la lista acumulada", sA2)
    print("La lista",listaEnteros3,"regresa la lista acumulada", sA3)

    print("")
    print("Ejercicio 2:")
    listaEnteros4 = [1,2,3,4,5]
    listaEnteros5 = [1,2,3]
    listaEnteros6 = []
    rL4 = recortarLista(listaEnteros4)
    rL5 = recortarLista(listaEnteros5)
    rL6 = recortarLista(listaEnteros6)
    print("Lista original",listaEnteros4,", regresa", rL4)
    print("Lista original", listaEnteros5, ", regresa", rL5)
    print("Lista original", listaEnteros6, ", regresa", rL6)

    print("")
    print("Ejercicio 3:")
    listaNumeros7 = [4,2,6]
    listaNumeros8 = [58,99,100]
    listaNumeros9 = []
    eO7 = estanOrdenados(listaNumeros7)
    eO8 = estanOrdenados(listaNumeros8)
    eO9 = estanOrdenados(listaNumeros9)
    print("Lista",listaNumeros7, "¿datos ordenados?",eO7)
    print("Lista", listaNumeros8, "¿datos ordenados?", eO8)
    print("Lista", listaNumeros9, "¿datos ordenados?", eO9)

    print("")
    print("Ejercicio 4:")
    n10 = str("Roma")
    m10 = str("Mora")
    n11 = str("Hola")
    m11 = str("Hello")
    n12 = str("ana")
    m12 = str("nana")
    sA10 = sonAnagramas(n10,m10)
    sA11 = sonAnagramas(n11, m11)
    sA12 = sonAnagramas(n12, m12)
    print("Las palabras",n10,"y",m10,"¿son anagramas?",sA10)
    print("Las palabras", n11, "y", m11, "¿son anagramas?", sA11)
    print("Las palabras", n12, "y", m12, "¿son anagramas?", sA12)

    print("")
    print("Ejercicio 5:")
    listaNumeros13 = [2,2,4,7,8,8]
    listaNumeros14 = [1,2,3,4,5,6,7]
    listaNumeros15 = []
    hD13 = hayDuplicados(listaNumeros13)
    hD14 = hayDuplicados(listaNumeros14)
    hD15 = hayDuplicados(listaNumeros15)
    print("En la lista",listaNumeros13,"¿hay duplicados?" ,hD13)
    print("En la lista", listaNumeros14, "¿hay duplicados?", hD14)
    print("En la lista", listaNumeros15, "¿hay duplicados?", hD15)

    print("")
    print("Ejercicio 6:")
    listaNumeros13 = [2, 2, 4, 7, 8, 8,8,8,22]
    listaNumeros14 = [1, 2, 3, 4, 5, 6, 7]
    listaNumeros15 = []
    x=listaNumeros13.copy()
    y = listaNumeros14.copy()
    z = listaNumeros15.copy()
    borrarDuplicados(x)
    borrarDuplicados(y)
    borrarDuplicados(z)
    print("De la lista",listaNumeros13,"regresa",x)
    print("De la lista", listaNumeros14, "regresa", y)
    print("De la lista", listaNumeros15, "regresa", z)





#Llamamos a la función principal
main()




