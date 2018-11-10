#Autor: Luis Mari Cervantes Ortiz
#Descripcion: Uso de listas, regreso de otras listas y numeros
def sumarAcumulado(lista): #Sumar del numero anterior de la lista
    lis=[]
    for k in range (1,len(lista)+1):
        lis.append(sum(lista[:k]))
    return lis

def recortarLista(lista): #Borrar el primer y ultimo valor de la lista
    list=[]

    for k in range(1,len(lista)-1):
        list.append(lista[k])
    return list


def estanOrdenados (lista): #Demostrar que una lista estsa ordenada
    var=True
    for k in range(1,len(lista)):
        if lista[k]>lista[k-1]:
            var= True
        if not lista[k]>lista[k-1]:
            var= False
            break
    return var


def sonAnagramas(primerapalabra,segundapalabra): #Demostrar que 2 palabras son anagramas

    if sorted(primerapalabra.lower())==sorted(segundapalabra.lower()):
        return True
    else:
        return False


def hayDuplicados(lista): #Demostrar si hay duplicados en una lista

    if len(lista) == len(list(set(lista))):
        return False
    else:
        return True

def borrarDuplicados(lista): #Borrar los numeros duplicados en una lista

    lista=list(set(lista))
    return lista

def main(): #Ejecutar las listas
    print("Ejercicio 1")
    lista1 = [1,2,3,4,5]
    lista2 =[]
    lista3=[5]
    print("La lista", lista1,"regresa",sumarAcumulado(lista1))
    print("La lista", lista2, "regresa", sumarAcumulado(lista2))
    print("La listta", lista3, "regresa",sumarAcumulado(lista3))
    print()
    print("Ejercicio 2")
    lista4= [1,2,3,4,5]
    print("La lista original",lista4, "regresa",recortarLista(lista4))
    lista5=[1,2,]
    print("La lista original", lista5, "regresa", recortarLista(lista5))
    lista6=[]
    print("La lista original", lista6, "regresa", recortarLista(lista6))
    print()
    print("Ejercicio 3")
    lista7=[1,2,3,4,5]
    print("La lista", lista7,"es ", estanOrdenados(lista7))
    lista8= [7,5,2,3]
    print("La lista", lista8, "es ", estanOrdenados(lista8))
    lista9=[1]
    print("La lista", lista9, "es ", estanOrdenados(lista9))
    print()
    print("Ejercicio 4")
    print("Las palabras, Fiesta y termo son anagramas?", (sonAnagramas("fiesta","termno")))
    print("Las palabras, Roma y Mora son anagramas?", (sonAnagramas("Roma", "Mora")))
    print("Las palabras, Hola y Hello son anagramas?", (sonAnagramas("hOLa", "Hello")))
    print()
    print("Ejercicio 5")
    lista10=[1,2,3,1,4,5]
    print("La lista", lista10,"tiene números duplicados?",hayDuplicados(lista10))
    lista11=[5,7,4,6,10]
    print("La lista", lista11, "tiene números duplicados?", hayDuplicados(lista11))
    lista12=[1]
    print("La lista", lista12, "tiene números duplicados?", hayDuplicados(lista12))
    print("Ejercicio 6")
    lista13=[1,8,7,5,3,1,8]
    print("La lista",lista13, "da",borrarDuplicados(lista13))
    lista14=[4,5,6,7,8,9]
    print("La lista", lista14, "da", borrarDuplicados(lista14))
    lista15=[]
    print("La lista", lista15, "da", borrarDuplicados(lista15))

main()
