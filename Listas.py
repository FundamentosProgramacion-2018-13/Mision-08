#Alberto Contreras Torres
#Misión 8, ejercicios de listas

#Ingresa una lista y regresa una nueva con la suma de los anteriores
def sumarAcumulado(lista):
    nueva = []
    suma = 0
    for k in lista:
        suma = suma + k
        nueva.append(suma)

    return nueva


#Recibe lista y regresa est sin el primer y ultimo digito
def recortarLista (lista):
    nueva = []
    if lista == []:
        return nueva
    else:
        lista.remove(lista[-1])
        lista.remove(lista[0])
        nueva= nueva + lista

    return nueva


#Recibe lista y regresa True o False, si estan ordenados
def estanOrdenados(lista):
    acumulador = 0
    for dato in lista:
        if dato>0:
            n= dato
            acumulador+= 1

            if acumulador == n:
                return True
    else:
        return False



#Recibe dos palabra y regresa True o False si son anagramas
def sonAnagramas(palabra1, palabra2):

    n= palabra1.lower()
    m= palabra2.lower()

    Anagrama1= list(n)
    Anagrama2= list(m)

    Anagrama1.sort()
    print(Anagrama1)
    Anagrama2.sort()
    print(Anagrama2)
    if Anagrama1 == Anagrama2:
        return True
    else:
        return False


#Recibe una lista y regresa True o False dependiendo si existen duplicados
def hayDuplicados(lista):
    if len(lista) != 0:
        for numero in range(len(lista)):
            for k in range(numero+1, len(lista)):
                if lista[numero] == lista[k]:
                    return True
    return False


#Recibe una lista y regresa la misma sin los multiplos de los numeros
def borrarDuplicados(lista):
    for k in lista:
        if 1 < lista.count(k):
            lista.remove(k)

    return(lista)


def main():

    #Probelma 1
    print("Problema 1")

    lista = [1,2,3,4,5]
    a=sumarAcumulado(lista)
    print(a)
    lista=[]
    b=sumarAcumulado(lista)
    print(b)
    lista=[5]
    c=sumarAcumulado(lista)
    print(c)

    #Problema 2
    print("Problema2")
    lista = [1,2,3,4,5]
    d=recortarLista(lista)
    print(d)
    lista=[1,2,3]
    e=recortarLista(lista)
    print(e)
    lista=[]
    f=recortarLista(lista)
    print(f)

    #Problema 3
    print("Problema 3")
    lista= [1,2,3,4,5]
    g=estanOrdenados(lista)
    print(g)
    lista= [7,23,15]
    h= estanOrdenados(lista)
    print(h)

    #Problema 4
    print("Problema 4")
    palabra1= "Mora"
    palabra2= "Roma"
    i=sonAnagramas(palabra1,palabra2)
    print(i)

    palabra1 = "Hola"
    palabra2 = "Hello"
    j=sonAnagramas(palabra1,palabra2)
    print(j)

    palabra1 = "Teresa"
    palabra2 = "Reseta"
    k=sonAnagramas(palabra1,palabra2)
    print(k)

    #Problema 5
    print("Problema 5")
    lista= [1,1,1,2,3,7,8,4]
    l=hayDuplicados(lista)
    print(l)
    lista=[1,2,3,7,8,4]
    m=hayDuplicados(lista)
    print(m)

    #Problema 6
    print("Problema 6")
    lista = [1,8,3,4,3,1,8,2,7,8]
    n=borrarDuplicados(lista)
    print(n)
    lista = []
    o = borrarDuplicados(lista)
    print(o)



main()