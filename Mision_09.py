# Autor: Alejandro Torices Oliva
# Programa que hace más pruebas con listas


#Es una función que regresa una nueva lista con los elementos pares de una lista dada.
def extraerPares(lista):
    nuevaLista = []
    for elemento in lista:
        if elemento % 2 == 0:
            nuevaLista.append(elemento)
    return nuevaLista


# Es una función que regresa una lista con los elementos que son mayores a un elemento previo.
def extraerMayoresPrevio(lista):
    nuevaLista = []
    for k in range(1, len(lista)):
        if lista[k] > lista[k-1]:
            nuevaLista.append(lista[k])
    return nuevaLista


# Es una función que intercambia los números en una lista de 2 en 2.
def intercambiarParejas(lista):
    nuevaLista = []
    for k in range(1, len(lista), 2):
        nuevaLista.append(lista[k])
        nuevaLista.append(lista[k-1])
    if len(lista)% 2 == 1:
        nuevaLista.append(lista[-1])
    return nuevaLista


# Es una función que intercambia el valor mayor con el menor y visceversa.
def intercambiarMM(lista):
    if lista != []:
        maximo = list.index(lista, max(lista))
        minimo = list.index(lista, min(lista))
        lista[maximo], lista[minimo] = lista[minimo], lista[maximo]


# Es una función que elimina el elemento mayor y menor de una lista y calcula el promedio.
def promediarCentro(lista):
    nuevaLista = lista
    nuevaLista.sort()
    a = nuevaLista[1:len(lista)-1]
    if len(a) > 0:
        promedio = sum(a)//len(a)
        return promedio
    else:
        return 0


# Es una función que calcula la media y la desviación estándar de los elementos de una lista.
def calcularEstadistica(lista):
    divisor = len(lista)
    if divisor != 0:
        media = sum(lista)/divisor
    else:
        media = 0
    if divisor > 1:
        suma = 0
        for x in lista:
            suma += (x - media)**2
        desviacion = (suma/(len(lista)-1))**0.5
    else:
        desviacion = 0
    return media, desviacion


# Es una función que calcula la suma de una lista exceptuando los valores que se encuentren antes y después del 13,
# incluyéndolo.
def calcularSuma(listaOriginal):
    lista = listaOriginal
    if 13 not in lista:
        return sum(lista)
    else:
        for k in range(len(lista)):
            if lista[k] == 13:
                if k != 0:
                    lista[k-1] = False
                lista[k] = False
                if k != len(lista):
                    lista[k+1] = False
        while False in lista:
            lista.remove(False)
        return sum(lista)
