def sumarAcumulado(lista):
    listaSumada=[]

    for k in (0,len(lista)+1):
        contador=0
        for x in range (0,k+1):
            contador=contador+lista[k]
            if k==x:
                listaSumada.append(contador)

    return listaSumada



def recortarLista(lista):
    listaRecor=[]
    for k in (1,len(lista),1):
        listaRecor.append(lista[k])

    return listaRecor


def estanOrdenados(lista):
    verdadero = True
    falso = False

    for k in range(1,len(lista)+1):
        if lista[k-1]<=lista[k]:
            pass
        else:
            return falso
    return verdadero

def sonAnagramas():
    pass

def hayDuplicados(lista):
    verdadero=True
    falso=False

    for x in range (0,len(lista)+1):
        contador = 0
        for k in range(0,len(lista)+1):
            if lista[x] == lista[k]:
                contador=contador+1
            if contador ==2:
                return falso
    return verdadero


def borrarDuplicados(lista):
    for x in range (0,len(lista)+1):
        contador = 0
        for k in range(0,len(lista)+1):
            if lista[x] == lista[k]:
                contador=contador+1
            if contador ==2:
                lista.pop(k)
    return lista




def main():
    lista = []  # Lista sin datos
    numero = int(input("Valor [-1 para terminar el programa]: "))
    while numero != -1:
        # procesan
        lista.append(numero)
        numero = int(input("Valor [-1 para terminar el programa]: "))



    sumarAcumulado(lista)
    recortarLista(lista)
    estanOrdenados(lista)
    sonAnagramas()
    estanOrdenados(lista)
    hayDuplicados(lista)
    borrarDuplicados(lista)







main()
