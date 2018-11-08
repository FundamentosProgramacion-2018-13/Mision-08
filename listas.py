#Autor: Claudio Mayoral García
#Descripción: son funciones que realizan ciertas funciones con listas


#Es una funcion que recibe una lista y regresa el acumulado deella
def sumarAcumulado(listaOriginal):
    acumulado = 0
    nuevaLista = []
    for x in listaOriginal:
        acumulado += x
        nuevaLista.append(acumulado)
    return nuevaLista


#Es una función que recibe una lista y regresa una lista sin primer ni ultimo termino
def recortarLista(listaOriginal):
    nuevaLista = listaOriginal[1:len(listaOriginal)-1]
    return nuevaLista


#Es una función que recibe una lista y regresa si esta ordenada o no
def estanOrdenados(listaOriginal):
    nuevaLista = []
    for x in range(len(listaOriginal)):
        if x != 0:
            if listaOriginal[x] < listaOriginal[x-1]:
                return False
    if len(nuevaLista) == 0:
        return True


#Es una función que recibe dos palabras y te dice si son anagramas
def sonAnagramas(string, string2):
    lista1 = list(string.upper())
    lista2 = list(string2.upper())
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    else:
        return False


#Es una función que recibe una lista y te dice si hay numeros duplicados
def hayDuplicados(listaOriginal):
    listaOriginal.sort()
    listaFalso = []
    for x in range(len(listaOriginal)):
        if x != 0:
            if listaOriginal[x] == listaOriginal[x-1]:
                return True
    if len(listaFalso) == 0:
        return False


#Es una función que elimina los duplicados de la lista original y regresa la lista sin los duplicados
def borrarDuplicados(listaOriginal):
    for x in range(len(listaOriginal)-1, -1, -1):
        repetidos = listaOriginal.count(listaOriginal[x])
        if repetidos > 1:
            listaOriginal.remove(listaOriginal[x])


#Función principal
def main():
    a = [1, 2, 3, 4, 5]
    b = []
    c = [10]
    d, e = "ana", "aan"
    f, g = "aMoR", "rOmA"
    h, i = "ragaa", "raga"
    m = [1, 3, 5, 2, 54, 543, 321, 826, 326, 532, 22, 1, 2,3, 4, 5, 5]
    x = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    print("-------------------------------------------------------------------------")
    print("Ejercicio 1:")
    print("La lista", a, "regresa la lista acumulada", sumarAcumulado(a))
    print("La lista", b, "regresa la lista acumulada", sumarAcumulado(b))
    print("La lista", c, "regresa la lista acumulada", sumarAcumulado(c))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 2:")
    print("La lista original ", a, "regresa ", recortarLista(a))
    print("La lista original ", b, "regresa ", recortarLista(b))
    print("La lista original ", c, "regresa ", recortarLista(c))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 3:")
    print("La lista ", a, "se regresa ordenada: ", estanOrdenados(a))
    print("La lista ", b, "se regresa ordenada: ", estanOrdenados(b))
    print("La lista ", c, "se regresa ordenada: ", estanOrdenados(c))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 4: ")
    print("Las cadenas ", e, "y ", d, "son anagramas: ", sonAnagramas(e, d))
    print("Las cadenas ", g, "y ", f, "son anagramas: ", sonAnagramas(g, f))
    print("Las cadenas ", i, "y ", h, "son anagramas: ", sonAnagramas(i, h))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 5:")
    print("En la lista", m, "Hay duplicados: ", hayDuplicados(m))
    print("En la lista", b, "Hay duplicados: ", hayDuplicados(b))
    print("En la lista", c, "Hay duplicados: ", hayDuplicados(c))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 6: ")
    m2 = m.copy()
    borrarDuplicados(m2)
    print("La lista", m, "sin duplicados es: ", borrarDuplicados(m2))

    print("La lista", b, "sin duplicados es: ", borrarDuplicados(b))
    y = x.copy()
    borrarDuplicados(y)
    print("La lista", x, "sin duplicados es: ", y)
    print("-------------------------------------------------------------------------")


#Llama a la función principal
main()