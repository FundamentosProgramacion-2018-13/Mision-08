#Autor: Joshua Sánchez Martínez A01274269
#Cumple con una serie de funciones con distintos fines


#Recibe como parametro una lista de numeros y regresa una nueva con la suma de los datos
def sumarAcumulado(lista):
    nuevaLista = []
    b = lista[:]
    for i in range(len(b)):
        c = sum(b)
        nuevaLista.append(c)
        b.pop()
    nuevaLista.reverse()
    return nuevaLista


#Recibe una lista de parametros y regresa una nueva lista sin el primero y el ultimo
def recortarLista(lista):
    b = lista[:]
    if b != []:
        b.pop(0)
        if b != []:
            b.pop()
    return b


#Recibe una lista de valores y regresa True si los valores estan ordenados y False si no lo estan
def estanOrdenados(lista):
    r = True
    b = lista[:]
    for v in lista:
        b.pop(0)
        if b != []:
            if v < b[0]:
                continue
            elif v > b[0]:
                r = False
                break
    return r


#Recibe dos cadenas y regresa True si son anagramas y False si no
def sonAnagramas(int1, int2):
    lInt1 = set(int1.lower())
    lInt2 = set(int2.lower())
    r = True
    if lInt1 != lInt2:
        r = False
    return r


#Recibe una lista de numeros y regresa True si hay alguno duplicado y False si no
def hayDuplicados(lista):
    r = False
    for d in lista:
        if lista.count(d) > 1:
            r = True
            break
    return r


#Recibe una lista de valores y elimina los repetidos
def borrarDuplicados(lista):
    b = lista[:]
    b.reverse()
    for d in b:
        if lista.count(d) > 1:
            lista.reverse()
            lista.remove(d)
            lista.reverse()
    return lista


#Función principal
def main():
    lista = [11,12,13,14,15,13,14,15]
    int1 = "Rama"
    int2 = "Amar"

    print("Lista original ",lista," Primer palabra ",int1," Segunda palabra ", int2)
    print("sumarAcumulado",sumarAcumulado(lista))
    print("recordarLista", recortarLista(lista))
    print("estanOrdenados", estanOrdenados(lista))
    print("sonAnagramas",sonAnagramas(int1,int2))
    print("hayDuplicados", hayDuplicados(lista))
    print("borrarDuplicados", borrarDuplicados(lista))


#Llama a la función principal
main()