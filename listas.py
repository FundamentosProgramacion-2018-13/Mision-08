# Rubén Villalpando Bremont
# Misión 8, listas.


# Función que regresa una nueva lista de la suma de todos los números anteriores hasta esa posición.
def sumarAcumulado(lista):
    nuevaLista = []
    suma = 0
    for n in lista:
        suma += n
        nuevaLista.append(suma)
    return nuevaLista


# Función que toma  una lista y regresa una nueva sin el primer y úlirmo valor.
def recortarLista(lista):
    nuevaLista = lista[1:len(lista)-1]
    return nuevaLista


# Función que checa si los valores están ordenados o no.
def estanOrdenados(lista):
    for k in range(1, len(lista)):
        if lista[k-1] < lista[k]:
            continue
        else:
            return False
    return True


# Función que recibe 2 palabras y dice si son anagramas o no.
def sonAnagramas(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    listaStringUno = list(palabra1)
    listaStringDos = list(palabra2)
    listaStringUno.sort()
    listaStringDos.sort()
    if len(listaStringDos) != len(listaStringUno):
        return False
    for x in range(len(listaStringUno)):
        if listaStringDos[x] == listaStringUno[x]:
            continue
        else:
            return False
    return True


# Función que recibe una lista y te dice si contiene valores duplicados o no.
def hayDuplicados(lista):
    for n in range(len(lista)):
        for k in range(n+1, len(lista)):
            if lista[n] == lista[k]:
                return True
    return False


# Función que recibe una lista y regresa la misma lista pero sin valores duplicados.
def borrarDuplicados(lista):
    listaDeDuplicados = []
    for n in range(len(lista)):
        for k in range(n+1, len(lista)):
            if lista[n] == lista[k]:
                listaDeDuplicados.append(lista[k])
                break
    for x in listaDeDuplicados:
        lista.remove(x)

    return lista


# Función principal que checa todas las demás funciones.
def main():
    # Listas para probar
    a = [1, 2, 3, 4, 5]
    b = []
    c = [10]
    d = [3, 25, 63, 1, 2, 466, 34]
    e, f = "ana", "aan"
    g, h = "aMoR", "rOmA"
    i, j = "ragaa", "raga"
    k, l = "hacia", "hasia"
    m = [2, 3, 4, 5, 6, 7, 8, 2, 6, 3, 5, 7, 1, 6, 8, 7, 3, 5, 8, 7, ]
    m2 = [2, 3, 4, 5, 6, 7, 8, 2, 6, 3, 5, 7, 1, 6, 8, 7, 3, 5, 8, 7, ]
    n = [1, 2, 6, 3, 4, 8, 9, 10]
    o, p = "", ""
    x = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    x2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    # Probar muchos casos diferentes para ver que las funciones hagan lo que deberían hacer.
    print("Ejercicio 1:")
    print("La lista", a, "regresa la lista acumulada", sumarAcumulado(a))
    print("La lista", b, "regresa la lista acumulada", sumarAcumulado(b))
    print("La lista", c, "regresa la lista acumulada", sumarAcumulado(c))
    print("La lista", d, "regresa la lista acumulada", sumarAcumulado(d))
    print("")
    print("Ejercicio 2:")
    print("La lista original ", a, "regresa ", recortarLista(a))
    print("La lista original ", b, "regresa ", recortarLista(b))
    print("La lista original ", c, "regresa ", recortarLista(c))
    print("La lista original ", d, "regresa ", recortarLista(d))
    print("")
    print("Ejercicio 3:")
    print("La lista ", a, "Está ordenada: ", estanOrdenados(a))
    print("La lista ", b, "Está ordenada: ", estanOrdenados(b))
    print("La lista ", c, "Está ordenada: ", estanOrdenados(c))
    print("La lista ", d, "Está ordenada: ", estanOrdenados(d))
    print("")
    print("Ejercicio 4: ")
    print("Las cadenas ", e, "y ", f, "son anagramas: ", sonAnagramas(e, f))
    print("Las cadenas ", g, "y ", h, "son anagramas: ", sonAnagramas(g, h))
    print("Las cadenas ", i, "y ", j, "son anagramas: ", sonAnagramas(i, j))
    print("Las cadenas ", k, "y ", l, "son anagramas: ", sonAnagramas(k, l))
    print("Las cadenas ", o, "y ", p, "son anagramas: ", sonAnagramas(o, p))
    print("")
    print("Ejercicio 5:")
    print("En la lista", m, "Hay duplicados: ", hayDuplicados(m))
    print("En la lista", n, "Hay duplicados: ", hayDuplicados(n))
    print("En la lista", b, "Hay duplicados: ", hayDuplicados(b))
    print("En la lista", c, "Hay duplicados: ", hayDuplicados(c))
    print("")
    print("Ejercicio 6: ")
    print("La lista", m, "eliminando los duplicados se vuelve ", borrarDuplicados(m2))
    print("La lista", n, "eliminando los duplicados se vuelve ", borrarDuplicados(n))
    print("La lista", b, "eliminando los duplicados se vuelve ", borrarDuplicados(b))
    print("La lista", x, "eliminando los duplicados se vuelve ", borrarDuplicados(x2))

# Llamar a la función principal
main()
