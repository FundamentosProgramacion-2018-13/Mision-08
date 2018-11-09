def sumarAcumulado(lista):
    nueva = []
    acumulador=0

    for k in lista:
        nueva.append(k+acumulador)
        acumulador=k+acumulador
        k+=1


    return nueva

def recortarLista(lista):
    nueva=[]
    for k in range(len(lista)):
        if k != (len(lista)-1) and k != 0:
            nueva.append(lista[k])
    return nueva


def estanOrdenados(lista):

    for k in range(len(lista)-1):
        acumulado=lista[k]
        acumulado2=lista[k+1]
        k+=1

        if acumulado > acumulado2 :
            return False

    return True

def sonAnagramas(a,b):
    a=a.upper()
    b=b.upper()
    m=list(a)
    n=list(b)

    for k in m:
        if k in n and len(n)==len(m):
            return True
        return False


def hayDuplicados(lista):
    for k in lista:
        if lista.count(k) > 1:
            return True
        else:
            return False



def borrarDuplicados(lista):
    for k in range(len(lista)-1,-1,-1):
        if lista.count(lista[k]) > 1:
            lista.remove(lista[k])
    #profe, no pude invertir el orden para que borrara los primeros. Traté usando la misma programación para encontrar los
    #duplicados y de ahí seleccionarlos y borrarlos, pero me marcaba error y no supe por qué, espero que sea válido así



    return lista


def main():

    lista1= [1,2,3,4,5]
    a1=[1,2,3,4,5]
    lista2= [2]
    a2=[2]
    lista3 =[]
    a3=[]
    lista4=[1,2]
    a4=[1,2]
    lista5=[5,12,4]
    a5=[5,12,4]
    lista6=[3,5,6]
    a6=[3,5,6]
    lista7=[1,3,3,1]
    a7=[1,3,3,1]
    lista8=[4,4,5,6,7]
    a8=[4,4,5,6,7]
    a="Amor"
    b="Roma"
    c="Ana"
    d="Anan"
    e="Hola"
    f="Hello"
    print("""
    Ejercicio 1:
    La lista """,a1,"""regresa la lista """,  sumarAcumulado(lista1),
    """
    la lista""",a2,"""regresa la lista: """, sumarAcumulado(lista2),
    """
    la lista """,a3, """regresa la lista """ ,sumarAcumulado(lista3),
          """
    Ejercicio 2: 
    La lista """,a1,"""regresa la lista """,  recortarLista(lista1),
    """
    la lista""",a4,"""regresa la lista: """, recortarLista(lista4),
    """
    la lista """,a3, """regresa la lista """ ,recortarLista(lista3),
          """
    Ejercicio 3:
    La lista """,a1, """¿está ordenada? """, estanOrdenados(lista1),
    """
    la lista""",a5, """¿está ordenada? """, estanOrdenados(lista5),
    """
    la lista """,a6, """¿está ordenada? """, estanOrdenados(lista6),
          """
    Ejercicio 4:
     """, a," y ",b, """ ¿son anagramas? """, sonAnagramas(a,b),
          """
     """, c," y ",d, """ ¿son anagramas? """, sonAnagramas(c,d),
          """
     """, e," y ",f, """ ¿son anagramas? """, sonAnagramas(e,f),
     """
     Ejercicio 5:
     En """, a1, """¿hay duplicados? """, hayDuplicados(lista1),
          """
     En """, a7, """¿hay duplicados? """, hayDuplicados(lista7),
          """
     En """, a8, """¿hay duplicados? """, hayDuplicados(lista8),
     """
     Ejercicio 2: 
     La lista """, a1, """regresa """, borrarDuplicados(lista1),
     """
     la lista""", a7, """regresa """, borrarDuplicados(lista7),
     """
     la lista """, a8, """regresa """, borrarDuplicados(lista8))

main()




