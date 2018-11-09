# Autor : Jonathan Sanabria Rocha
# Actividad: Resolver problemas usando listas


def sumarAcumulado(listaEnteros):
    nuevoValor = 0
    nuevaLista = []
    for valor in listaEnteros:
        nuevoValor += valor
        nuevaLista.append(nuevoValor)
    return nuevaLista


def recortarLista(listaEnteros):
    duplicaLista = listaEnteros [:]
    if duplicaLista != []:
        duplicaLista.pop(0)
        if duplicaLista != []:
            duplicaLista.pop()
    return duplicaLista


def estanOrdenados(listEnteros):

    for n in range(1, len(listEnteros)):

            if listEnteros[n] < listEnteros[n-1]:
                return False
    else: "No hay Valores"


def sonAnagramas(palabraUno, palabraDos):

    palabraDos = palabraDos.lower()
    palabraUno = palabraUno.lower()
    if len(palabraUno) == len(palabraDos):
        for l in palabraUno:
            if l in palabraDos:
              return True
            else: return False
    else: return False


def hayDuplicados(listaEnteros):
    for valor in listaEnteros:
        if listaEnteros.count(valor)>=2:
            return True
    return False


def borrarDuplicados(listaEnteros):
    for valor in listaEnteros:
        while listaEnteros.count(valor) >= 2:
            listaEnteros.remove(valor)
    return listaEnteros



def main():

    listaEnteros = [1,2,3,4,5]
    listaVacia = []
    listaDesordenada = [1,3,5,2,4,7,6,8]
    listaRepetidos = [2,3,4,9,2]
    listaRepetidosDos = [2,3,4,9,2,8,9]
    listaDos = [2,3]
    roma = "roma"
    mora = "mora"
    hola = "hola"
    hello = "hello"
    silla = "silla"
    villa = "villa"



    print("""
    Ejercicio 1
    La lista """,listaEnteros,"regresa la lista acumulada",sumarAcumulado(listaEnteros),"""
    La lista """,listaVacia,"regresa la lista acumulada",sumarAcumulado(listaVacia),"""
    La lista """,listaDos,"regresa la lista acumulada",sumarAcumulado(listaDos),"""


    Ejercicio 2
    La lista """, listaEnteros,"regresa la lista acumulada",recortarLista(listaEnteros),"""
    La lista """,listaDos,"regresa la lista acumulada",recortarLista(listaDos),"""
    La lista """,listaVacia,"regresa la lista acumulada",recortarLista(listaVacia),"""


    Ejercicio 3
    La lista """,listaEnteros,"regresa: ",estanOrdenados(listaEnteros),"""
    La lista """,listaDesordenada,"regresa: ",estanOrdenados(listaDesordenada),"""
    La lista """,listaVacia,"regresa: ",estanOrdenados(listaVacia),"""


    Ejercicio 4
    La cadena """,roma,"y",mora,"regresa",sonAnagramas(roma,mora),"""
    La cadena """,hola,"y",hello,"regresa",sonAnagramas(hola,hello),"""
    La cadena """,silla,"y",villa,"regresa",sonAnagramas(silla,villa),"""


    Ejercicio 5
    La lista """,listaEnteros,"regresa",hayDuplicados(listaEnteros),"""
    La lista """,listaRepetidos,"regresa",hayDuplicados(listaRepetidos),"""
    La lista """,listaRepetidosDos,"regresa",hayDuplicados(listaRepetidosDos),"""


    Ejercicio 6
    La lista """,listaRepetidos,"regresa",borrarDuplicados(listaRepetidos),"""
    La lista """,listaRepetidosDos,"regresa",borrarDuplicados(listaRepetidosDos))


main()


