#Autor: Marco González Elizalde
#Mision 08: Listas en Python


def sumarAcumulado(listaEnteros):
    suma = 0
    nuevaLista = []
    if len(listaEnteros)>0:
        for k in range(0,len(listaEnteros)):
            suma += listaEnteros[k]
            nuevaLista.append(suma)
        return (nuevaLista)
    else:
        return "Error, no hay datos"

def recortarLista(listaEnteros):
    listaRecortada = []
    if len(listaEnteros)>2:
        listaRecortada = listaEnteros
        for k in range(0,len(listaEnteros)-1,len(listaEnteros)-2):
            del listaRecortada[k]
        return listaRecortada
    else:
        return  listaRecortada


def estanOrdenados(lista): #Checar Secuencia en ciclo for (subin
    if len(lista) > 0:
        for k in range (len(lista)-1):
            if lista[k] > lista[k+1]:
                return  False
        return True
    else:
        return "Error, no hay datos"

def sonAnagramas(cadenaA,cadenaB):
    listaA = list(cadenaA.lower())
    listaB = list(cadenaB.lower())

    for k in listaA:
        if k in listaB and (len(listaA) == len(listaB)):
            return True
        else:
            return False


def hayDuplicados(lista):
    contador = 0
    for k in lista:
        if lista.count(k) > 1:
            contador +=1
    if contador != 0:
        return True
    else:
        return False

def borrarDuplicados(lista):
    for k in range (len(lista)-1,-1,-1):
        if lista.count(lista[k]) > 1:
            del lista[k]
        else:
            pass
    return lista

def main():
    listaA = [1,2,3,4,5]
    listaAA = [5]
    listaAAA = []

    listaB = [1,2,3,4,5]
    listaBB = [1,2]
    listaBBB = []

    listaC = [1,2,3,4,5]
    listaCC = [1,3,5,2,4]
    listaCCC = []

    cadenaD = "Mono"
    cadenaDA = "Nomo"
    cadenaDB = "Noomoo"
    cadenaDC = "No"

    listaE = [1,2,3,4,5]
    listaEE = [1,2,3,1,4,5]
    listaEEE = []

    listaF = [1,2,3,4,1,2,3]
    listaFF = [3,5,2,1,1,2,3,6,6,5]

    print("""
    Ejercicio 1:
    La lista""",listaA,"regresa la lista acumulada:",sumarAcumulado(listaA),"""
    La lista""",listaAA,"regresa la lista acumulada:",sumarAcumulado(listaAA),"""
    La lista""",listaAAA, "regresa la lista acumulada:", sumarAcumulado(listaAAA), """
    
    Ejercicio 2:
    Lista original:""",listaB,"regresa la lista:",recortarLista(listaB),"""
    Lista original:""",listaBB,"regresa la lista:",recortarLista(listaBB),"""
    Lista original:""",listaBBB,"regresa la lista:",recortarLista(listaBBB),"""
    
    Ejercicio 3:
    ¿Están ordenados los datos en la lista""", listaC,"?",estanOrdenados(listaC),"""
    ¿Están ordenados los datos en la lista""", listaCC,"?",estanOrdenados(listaCC),"""
    ¿Están ordenados los datos en la lista""", listaCCC,"?",estanOrdenados(listaCCC),"""
    
    Ejercicio 4:
    ¿Son""",cadenaD,"y",cadenaDA,"anagramas?",sonAnagramas(cadenaD,cadenaDA),"""
    ¿Son""",cadenaD,"y",cadenaDB,"anagramas?",sonAnagramas(cadenaD,cadenaDB),"""
    ¿Son""",cadenaD,"y",cadenaDC,"anagramas?",sonAnagramas(cadenaD,cadenaDC),"""
    
    Ejercicio 5:
    ¿Hay duplicados en la lista""",listaE,"?",hayDuplicados(listaE),"""
    ¿Hay duplicados en la lista""",listaEE,"?",hayDuplicados(listaEE),"""
    ¿Hay duplicados en la lista""",listaEEE,"?",hayDuplicados(listaEEE),"""
    
    Ejercicio 6:
    Borrando los duplicados en la lista""",listaF,"obtenemos:",borrarDuplicados(listaF),"""
    Borrando los duplicados en la lista""",listaFF,"obtenemos:",borrarDuplicados(listaFF)
    )

main()
