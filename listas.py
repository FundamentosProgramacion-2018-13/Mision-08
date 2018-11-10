# Autor: Humberto Carrillo Gómez
# Descripción: Prueba varias funciones con listas para demostrar su uso.


def sumarAcumulado(listaNumeros):  # Recibe una lista de números y crea una nueva lista con la suma de los valores

    nuevaLista=[]
    contadorSuma = 0                 # Aquí se acumula el valor de la suma de los datos de la lista.
    for valor in listaNumeros:       # Visitar cada dato de la listaNumeros
        contadorSuma = contadorSuma+valor  # Sumar al contador el valor de los elementos de la lista
        nuevaLista.append(contadorSuma)    # Agregar a la lista el valor de la suma
    return nuevaLista


def recortarLista(listaNumeros):  # Recibe una lista y la regresa sin el primer y último dato.

    listaRecortada = listaNumeros[:]         # Aquí se clona una lista
    if listaRecortada == []:                 # Prevenir que al mandar una lista vacía, se produzca un error
        return '[]'
    if listaRecortada == [1]:        # Prevenir que la función pop marque un error al trabar únicamente con un elemento
        return '[]'
    listaRecortada.pop(0)            # Eliminar el primer número
    listaRecortada.pop(-1)           # Eliminar el segundo número
    return listaRecortada


def estanOrdenados(listaNumeros): # Recibe una lista y determina si los datos de esta están ordenados.
    contadorValor = 0
    if listaNumeros == []:           # Prevenir que regrese None si la lista esta vacía
        return True
    for k in range(len(listaNumeros)):  #Explorar los índices de la lista
        if listaNumeros[k] <= listaNumeros[-1]:
                return True
        return False

def sonAnagramas(CadenaX, CadenaY):        # Recibe dos palabras y determina si son anagramas
    listaX = []          # Lista donde se guardarán las letras de la primera cadena
    listaY = []          # Lista donde se guardarán las letras de la segunda cadena
    for palabra in CadenaX:    # Visitar la palabra de la cadena X
        for letra in palabra:   # Visitar cada letra de la palabra
            Mayus=letra.upper()  # Convertir a mayúscula cada letra
            listaX.append(Mayus)  # Guardar las letras de la palabra en mayúsculas
    for palabra in CadenaY:     # Visitar la palabra de la cadena Y
        for letra in palabra:   # Visitar cada letra de la palabra
            Mayus= letra.upper()  # Convertir a mayúscula cada letra
            listaY.append(Mayus)  # Guardar las letras de la palabra en mayúsculas
    listaX.sort()               # Acomodar las letras de la palabra x alfabéticamente
    listaY.sort()               # Acomodar las letras de la palabra y alfabéticamente
    if listaY == listaX:
        return True
    return False


def hayDuplicados(listaNumeros):            # Busca números duplicados dentro de una lista
    repetidos = []                          # Lista donde se guardarán los valores que se repitan
    if listaNumeros == []:                  # Si la lista está vacía entonces, no hay duplicados
        return False
    for numero in listaNumeros:              # Visitar cada número dentro de la lista
        contar = listaNumeros.count(numero)  # contar cuantas veces aparece cada número
        repetidos.append(contar)             # Añadir a la lista el número de veces que se repite un valor
    for dato in repetidos:                   # Visitar los datos de la lista repetidos
        if dato >= 2:                        # Si un dato se repite dos o más veces
            return True
        return False


def borrarDuplicados(listaDuplicados):       # Elimina números duplicados de una lista
    for dato in listaDuplicados:             # Visitar cada dato de la lista de duplicados
        while listaDuplicados.count(dato) > 1:  # Mientras el dato se encuentre duplicado
            listaDuplicados.remove(dato)        # Remover el dato
    return listaDuplicados

def main():

    listaNumeros = [1,2,3]
    listaDuplicados = []
    print(sumarAcumulado(listaNumeros))
    print(recortarLista(listaNumeros))
    print(estanOrdenados(listaNumeros))
    print(sonAnagramas('Sergio', 'Riesgo'))
    print(hayDuplicados(listaNumeros))
    print(borrarDuplicados(listaDuplicados))


main()