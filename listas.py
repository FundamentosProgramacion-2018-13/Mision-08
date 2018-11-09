#Autor: Carlos Alberto Reyes Ortiz
#Matricula: A01376349
# Este programa cuenta con 6 ejercicio de listas y un main que imprime tres ejemplos de cada uno.



def sumarAcumulador(listaNumerosEnteros): # De la lista dada va sumando acumulativamente
                                          # los datos de izquierda a derecha en una lista nueva
    sumaAcumulada = []

    for n in range(len(listaNumerosEnteros)):
        sumando = listaNumerosEnteros[0:n+1]
        sumaAcumulada.append(sum(sumando))

    return sumaAcumulada



def recortarLista(listaNumerosEnteros): #De la lista dada recorta el 1er y último número en una lista nueva

    if len(listaNumerosEnteros) >= 2:

        listaRecortada = listaNumerosEnteros.copy()
        listaRecortada.remove(listaRecortada[-1])
        listaRecortada.remove(listaRecortada[0])
    else: listaRecortada = []

    return listaRecortada



def estanOrdenados(listaNumerosEnteros): #De la lista dada regresa True si estan ordendados y False si no lo estan

    for n in range(1, len(listaNumerosEnteros)):

            if listaNumerosEnteros[n] < listaNumerosEnteros[n-1]:
                return False
    else: return True



def sonAnagramas(cadenaUno, cadenaDos): # De las dos cadenas dadas regresa True si son anagramas  y False si no lo son.

    cadenaDos = cadenaDos.lower()
    cadenaUno = cadenaUno.lower()
    if len(cadenaUno) == len(cadenaDos):
        for l in cadenaUno:

            if l in cadenaDos:
              return True
            else: return False

    else: return False



def hayDuplicados(listaNumerosEnteros):#De la lista dada regresa True si hay números duplicados y False si no hay

    if len(listaNumerosEnteros) > 0:
        for k in listaNumerosEnteros:

                if listaNumerosEnteros.count(k) >= 2:
                    return True
                else: return False
    else: return False


def borrarDuplicados(listaNumerosEnteros):#Recibe una lista y regresa la misma lista sin los números duplicados
    for k in listaNumerosEnteros:
        while listaNumerosEnteros.count(k) >= 2:
            listaNumerosEnteros.remove(k)
    return listaNumerosEnteros



def main(): # Función Principal que prueba todos los ejercicios y da tres ejemplos de cada uno.
    listaNumerosEnteros = [1,2,3,4,5]
    listaVacia = []
    listaDosUno = [21]
    listaDesordenada = [5,1,3,4,7,2]
    listaDuplicados = [1,2,3,1,4,]
    listaDuplicadosDos = [1,8,7,2,3,5,8,1]
    roma = "Roma"
    mora = "Mora"
    hola = "Hola"
    hello = "Hello"
    casa = "Casa"
    casas = "Casas"


    print("""
    Ejercicio 1:
        La lista""",listaNumerosEnteros,"regresa la lista acumulada", sumarAcumulador(listaNumerosEnteros),"""
        La lista """,listaVacia, "regresa la lista acumulada", sumarAcumulador(listaVacia),"""
        La lista """,listaDosUno, "regresa la lista acumulada", sumarAcumulador(listaDosUno),"""
    
    Ejercicio 2:
        La lista""",listaNumerosEnteros,"regresa la lista acumulada", recortarLista(listaNumerosEnteros),"""
        La lista""",listaVacia,"regresa la lista acumulada", recortarLista(listaVacia),"""
        La lista""",listaDosUno,"regresa la lista acumulada", recortarLista(listaDosUno),""""
    
    Ejercicio 3:
        La lista""",listaNumerosEnteros,"regresa", estanOrdenados(listaNumerosEnteros),"""
        La lista""",listaDesordenada,"regresa", estanOrdenados(listaDesordenada),"""
        La lista""",listaVacia,"regresa", estanOrdenados(listaVacia),"""
    
    Ejercicio 4:
        Las cadenas""",roma,"y", mora,"regresa", sonAnagramas(roma,mora),"""
        Las cadenas""",hola,"y",hello,"regresa", sonAnagramas(hola,hello),"""
        Las cadenas""",casa,"y",casas,"regresa", sonAnagramas(casa, casas),"""
    
    Ejercicio 5:
         La lista""",listaNumerosEnteros,"regresa", hayDuplicados(listaNumerosEnteros),"""
         La lista""",listaDuplicados,"regresa", hayDuplicados(listaDuplicados),"""
         La lista""",listaDuplicadosDos,"regresa", hayDuplicados(listaDuplicadosDos))

    print("""
    Ejercicio 6:
        La lista""",listaNumerosEnteros,"regresa", borrarDuplicados(listaNumerosEnteros))
    print()
    print("""        La lista""",listaDuplicados,"regresa")
    print("""                                        """,borrarDuplicados(listaDuplicados))
    print("""        La lista""",listaDuplicadosDos,"regresa")
    print("""                                        """"",borrarDuplicados(listaDuplicadosDos))
        
     
     
    

main()

