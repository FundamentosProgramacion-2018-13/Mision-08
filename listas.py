#Francisco Ariel Arenas Enciso
#A01369122
#Desarrollo de lamisión 8 (listas)


'''Función que recibe la opción que el usuario quiere ejecutar'''
def leerOpcion():
    print('''
Francisco Ariel Arenas Enciso
MISIÓN #8
----------------------------------------------
OPCIONES DE EJERCICIOS A DESARROLLAR:
    1. Sumar acumulados de una lista
    2. Recortar lista introducida
    3. ¿Están ordenados tus datos?
    4. ¿Son anagramas?
    5. ¿Hay valoes duplicados?
    6. Borrar datos NO repetidos de una lista
    0. Salir
----------------------------------------------
''')
    opcion = int(input('¿Qué desea hacer? '))
    return opcion


'''Función que recibe una lista de main como parámetro y mediante un ciclo for, regresa una nueva lista con la suma de
los índices dentro de la lista pasada'''
def sumarAcumulado(listaSumar):
    listaNuevaSumar = []
    acumulador = 0
    for valor in listaSumar:
        acumulador += valor
        listaNuevaSumar.append(acumulador)
    return listaNuevaSumar


'''Función que recibe una lista de main como parámetro y regresa la lista orginial sin los valores de los
índices de los extremos a tráves de la función pop'''
def recortarLista(listaOriginal):
    del listaOriginal[0]
    listaOriginal.pop()
    return listaOriginal


'''Función que recibe una lista de main como parámetro y regresa un valor booleano (True o False) dependiendo si la 
lista en cuestión está ordenada. Esto se logramediante una función for que contine evalúa condiciones y fuera del for
un if evalua la respuesta del for'''
def estanOrdenados(listaEvaluar):
    primerParametroLista = listaEvaluar[0]
    condicion = 1
    for numero in listaEvaluar:
        if numero >= primerParametroLista:
            primerParametroLista = numero
            condicion = 1
        else:
            condicion = 0
    if condicion == 1:
        return True
    else:
        return False


'''Función que recibe dos cadenas como parámetros y ésta los convierte en una lista con el fin de poder analizar si
contienen los mismos índices mediante el uso de la función sort'''
def sonAnagramas(palabraUno, palabraDos):
    listaUno = list(palabraUno)
    listaDos = list(palabraDos)
    listaUno.sort()
    listaDos.sort()
    if listaUno == listaDos:
        return True
    else:
        return False


'''Mediante el uso de ciclos for, la función recibe como parametro una lista de main, haciedno uso de éste se evalua la 
una condición respecto a la cantidad de valores que hay  en la lista.'''
def hayDuplicados(listaDuplicados):
    for valores in listaDuplicados:
        if listaDuplicados.count(valores)>1:
            return True
        else:
            return False


'''MLa función recibe como parámetro una lista de main y mediante el uso de un ciclo for, así como de una condición if
la función evalua si la lista tiene valores repetidos'''
def borrarDuplicados(listaBorrarDuplicados):
    listaCopia = listaBorrarDuplicados[:]
    for valor in range(len(listaBorrarDuplicados)-1, -1, -1):
        valorNuevo = listaBorrarDuplicados[valor]
        valorDuplicado = listaBorrarDuplicados.count(valorNuevo)
        if valorDuplicado > 1:
            listaBorrarDuplicados.remove(valorNuevo)


'''Función main que contiene la lógica del ejercicio'''
def main():
    opcion = leerOpcion()
    while opcion != 0:
        if opcion == 1:
            print('''
Seleccionaste el Ejercicio 1.
            ''')
            lista = []
            valores = int(input('Escribe valores númericos [-1 para ver resultado]: '))
            while valores != -1:
                lista.append(valores)
                valores = int(input('Escribe una serie de números [-1 para ver resultado]: '))
            listaSumar = lista[:]
            print('La lista ', lista, 'regresa', sumarAcumulado(listaSumar))


        elif opcion == 2:
            print('''
Seleccionaste el Ejercicio 2.
            ''')
            lista = []
            valores= int(input('Escribe una serie de datos [-1 para ver resultado]: '))
            while valores != -1:
                lista.append(valores)
                valores = int(input('Escribe una serie de datos [-1 para ver resultado]: '))
            listaOriginal = lista[:]
            print('La lista original', lista, 'regresa', recortarLista(listaOriginal))


        elif opcion == 3:
            print('''
Seleccionaste el Ejercicio 3.
            ''')
            lista = []
            valores= int(input('Escribe una serie de datos [-1 para ver resultado]: '))
            while valores != -1:
                lista.append(valores)
                valores = int(input('Escribe una serie de datos [-1 para ver resultado]: '))
            listaEvaluar = lista
            print('La lista', listaEvaluar, '¿Tiene sus parámetros ordenados?', estanOrdenados(listaEvaluar))


        elif opcion == 4:
            print('''
Seleccionaste el Ejercicio 4.
            ''')
            listaUno = []
            listaDos = []
            for i in range(1):
                palabraUno = input('Escribe una palabra: ')
                palabraDos = input('Escribe otra palabra: ')
            print('¿',palabraUno, 'es anagrama de', palabraDos,'?', sonAnagramas(palabraUno, palabraDos))


        elif opcion == 5:
            print('''
Seleccionaste el Ejercicio 5.
            ''')
            lista = []
            valores = int(input('Escribe una serie de datos [-1 para dejar de escribir]: '))
            while valores != -1:
                lista.append(valores)
                valores = int(input('Escribe una serie de datos [-1 para dejar de escribir]: '))
            listaDuplicados = lista
            print('La lista', listaDuplicados, '¿Tiene duplicados?', hayDuplicados(listaDuplicados))

        elif opcion == 6:
            print('''
Seleccionaste el Ejercicio 6.
            ''')
            lista = []
            valores = int(input('Escribe una serie de datos [-1 para dejar de escribir]: '))
            while valores != -1:
                lista.append(valores)
                valores = int(input('Escribe una serie de datos [-1 para dejar de escribir]: '))
            listaBorrarDuplicados = lista
            print('La lista orginal es', listaBorrarDuplicados)
            borrarDuplicados(listaBorrarDuplicados)
            print('La lista actualizada queda', listaBorrarDuplicados)

        else:
            print('''
La opción no es válida
            ''')
            opcion = leerOpcion()


main()