#Alan Diaz Carrera
#Realia varias funciones a base de listas


def sumarAcumulado(lista):
    valor=0
    nuevaLista=[]
    for k in lista:
        if valor==0:
            valor=valor+k
            nuevaLista.append(valor)
        else:
            k1 = k
            valor=valor+k1
            nuevaLista.append(valor)

    return nuevaLista

def recortarLista(lista):
    orden =1
    nuevaLista=[]
    for k in lista:
        if orden !=1 and orden!=len(lista):
            orden+=1
            nuevaLista.append(k)
        elif orden ==1:
            orden+=1
    return nuevaLista

def estanOrdenados(lista):
    k1=0
    orden=0
    for k in lista:
        if k>k1:
            orden+=1
        k1=k
    if orden==len(lista):
        return True
    else:
        return False

def sonAnagramas(palabra1, palabra2):
    cantidad=0
    if len(palabra1)==len(palabra2):
        for k in palabra1.upper():
            for k1 in palabra2.upper():
                if k==k1:
                    cantidad+=1
    if cantidad==len(palabra1):
        return True
    else:
        return False



def hayDuplicados(lista):
    cantidad=len(lista)*-1
    for k in lista:
        for k2 in lista:
            if k2==k:
                cantidad+=1
    if cantidad<=0:
        return False
    if cantidad>0:
        return True

def borrarDuplicados(lista):
    lista=list(set(lista))
    return lista

def main():
    print("Ejercicio 1")
    lista1=[1,2,3,4,5]
    lista2=[]
    lista3=[5]
    print("La lista", lista1, "regresa la lista acumulada", sumarAcumulado(lista1))
    print("La lista", lista2, "regresa la lista acumulada", sumarAcumulado(lista2))
    print("La lista", lista3, "regresa la lista acumulada", sumarAcumulado(lista3))
    print("""
Ejercicio 2""")
    lista4=[1,2,3,4,5]
    lista5=[1,2,3]
    lista6=[]
    print("La lista", lista4, "regresa", recortarLista(lista4))
    print("La lista", lista5, "regresa", recortarLista(lista5))
    print("La lista", lista6, "regresa", recortarLista(lista6))
    print("""
Ejercicio 3""")
    lista7=[2,3,4,7]
    lista8=[1,3,2,7]
    lista9=[5,20]
    print("La lista", lista7, "esta ordenada?", estanOrdenados(lista7))
    print("La lista", lista8, "esta ordenada?", estanOrdenados(lista8))
    print("La lista", lista9, "esta ordenada?", estanOrdenados(lista9))
    print("""
Ejercicio 4""")
    palabra1 = "Roma"
    palabra2 = "Amor"
    print("La palabra", palabra1, "y la palabra", palabra2, "son anagramas?", sonAnagramas(palabra1, palabra2))
    palabra3 = "Hola"
    palabra4 = "Holis"
    print("La palabra", palabra3, "y la palabra", palabra4, "son anagramas?", sonAnagramas(palabra3, palabra4))
    print("""
Ejercicio 5""")
    lista10=[1,2,3,4,5]
    lista11=[2,7,3,4,8]
    lista12=[2,5,2,3,4,8,4]
    print("La lista", lista10, "tiene duplicados?", hayDuplicados(lista10))
    print("La lista", lista11, "tiene duplicados?", hayDuplicados(lista11))
    print("La lista", lista12, "tiene duplicados?", hayDuplicados(lista12))
    print("""
Ejercicio 6""")
    lista13=[2,5,2,3,4,8,4]
    lista14=[1,2,3,4,1,5,2]
    lista15=[2,10,8,2,50]
    print("La lista", lista13, "regresa", borrarDuplicados(lista13))
    print("La lista", lista14, "regresa", borrarDuplicados(lista14))
    print("La lista", lista15, "regresa", borrarDuplicados(lista15))

main()