#Autor: Damián Iván García Ravelo
#A01376354
#Programa que ejemplifica el uso de las listas

def sumarAcumulado(lista): #Función que de una primer lista, imprime el primer valor, y le suma el siguiente, así continuamente
    nuevaLista=[] #La nueva lista donde se guardarán estos nuevos valores
    acumulador=0 #Acumulador de la suma de datos inicializado en 0

    for dato in lista: #Se recorre de dato en dato la lista original
        acumulador += dato #El acumulador toma el valor de la suma de datos
        nuevaLista.append(acumulador) #Se agrega eñ valor acumulado
    return nuevaLista #Regresa la nueva lista

def recortarLista(lista): #Función que elimina el primer y último valor de una lista
    listaGenerada=[] #Nueva lista que se va a generar

    for valor in lista: #Copia identica de la lista dada a la nueva lista
        listaGenerada.append(valor)
    if listaGenerada==[]: #Si la lista generada está vacía
        return listaGenerada #regresa la lista vacía
    else: #Si la lista tiene contenido
        listaGenerada.pop() #elimina el ultimo valor
        listaGenerada.pop(0) #elimina el primer valor
    return listaGenerada #regresa la nueva lista modificada

def estanOrdenados(lista): #Función que verifica si una lista está ordenada
    if lista==[]: #Si la lista está vacía
        return False #No hay datos que ordenar, por lo tanto false
    for numero in lista: #Verifica cada numero en la lista
        if numero+1 >= numero: #Si el numero en la siguiente posición es mayor al numero en la posición anterior:
            return True #Regresa True
        else:
            return False #De lo contrario regresa False

def sonAnagramas(parametro1,parametro2): #Función que verifica si una lista de palabras es la misma a la otra
    #Cada parametro se vuelve en minusuclas, para que no haya problema en cuestión de mayúsculas y minúsculas
    parametro1=parametro1.lower()
    parametro2=parametro2.lower()

    lista1 = list(parametro1) #El primer parámetro se le asigna a la primer lista
    lista2 = list(parametro2) #El segundo parámetro se le asigna a la segunda lista

    if len(lista1)==len(lista2): #Hacemos la primer condición de que tengan la misma longitud
        for datos in lista1: #Recorre cada dato en la lista1
            if datos in lista2:#Si ese dato está en la lista2
                return True #Regresa true
            else:
                return False #De lo contrario es Falso
    else:
        return False #Si no tienen la misma longitud, directamente dice que no son anagramas

def hayDuplicados(lista): #Función que verifica si algún dato de lista está repetida o no
    if lista==[]:
        return False

    for valor in lista: #Recorre cada valor de la lista
        if lista.count(valor)>1: #Cuenta ese valor, y si se repite más de una vez
            return True #Regresa True, diciendo que si se repite
        else:
            return False #De lo contrario regresa False

def borrarDuplicados(lista): #Función que borra los valores duplicados, a excpeción de uno de ese conjunto repetido

    for valor in lista: #Recorre cada valor en la lista
        if lista.count(valor)==1: #Si la cuenta de ese valor va en 1
            pass #No lo toca
        elif lista.count(valor)>1: #Si la lista ya va mayor a 1
            lista.remove(valor) #Elimina los valores a partir de que la cuenta sea 2
    return lista #Regresa la lista




#Pruebas que demuestran el correcto funcionamiento de los codigos
def main():
    print("Prueba 1")
    print("---------------------------------------------------------------------------------------------------------------------")
    lista=[1,2,3,4,5]
    parametro1='ana'
    parametro2='nana'
    print("La lista original es:",lista,"y al acumular los número regresa",sumarAcumulado(lista))
    print("La lista original es:",lista,"y al recortar los números del principio y el fin regresa",recortarLista(lista))
    print("La lista original es:",lista,"¿Están ordenados?",estanOrdenados(lista))
    print("Las palabras",parametro1,"y",parametro2, "¿Son anagramas?",sonAnagramas(parametro1,parametro2))
    print("La lista original es:",lista,"¿Hay números duplicados?",hayDuplicados(lista))
    print("La lista original es:",lista,"y al borrar los números duplicados regresa",borrarDuplicados(lista))
    print()
    print("Prueba 2")
    print("---------------------------------------------------------------------------------------------------------------------")
    lista=[]
    parametro1='amor'
    parametro2='roma'
    print("La lista original es:",lista,"y al acumular los número regresa",sumarAcumulado(lista))
    print("La lista original es:",lista,"y al recortar los números del principio y el fin regresa",recortarLista(lista))
    print("La lista original es:",lista,"¿Están ordenados?",estanOrdenados(lista))
    print("Las palabras",parametro1,"y",parametro2, "¿Son anagramas?",sonAnagramas(parametro1,parametro2))
    print("La lista original es:",lista,"¿Hay números duplicados?",hayDuplicados(lista))
    print("La lista original es:",lista,"y al borrar los números duplicados regresa",borrarDuplicados(lista))
    print()
    print("Prueba 3")
    print("---------------------------------------------------------------------------------------------------------------------")
    lista=[1,2]
    parametro1='RotAr'
    parametro2='taRRo'
    print("La lista original es:",lista,"y al acumular los número regresa",sumarAcumulado(lista))
    print("La lista original es:",lista,"y al recortar los números del principio y el fin regresa",recortarLista(lista))
    print("La lista original es:",lista,"¿Están ordenados?",estanOrdenados(lista))
    print("Las palabras",parametro1,"y",parametro2, "¿Son anagramas?",sonAnagramas(parametro1,parametro2))
    print("La lista original es:",lista,"¿Hay números duplicados?",hayDuplicados(lista))
    print("La lista original es:",lista,"y al borrar los números duplicados regresa",borrarDuplicados(lista))
    print()
    print("Prueba 4")
    print("---------------------------------------------------------------------------------------------------------------------")
    lista=[10,10,9,9,8,7,6]
    parametro1='sapo'
    parametro2='Pasa'
    print("La lista original es:",lista,"y al acumular los número regresa",sumarAcumulado(lista))
    print("La lista original es:",lista,"y al recortar los números del principio y el fin regresa",recortarLista(lista))
    print("La lista original es:",lista,"¿Están ordenados de menor a mayor?",estanOrdenados(lista))
    print("Las palabras",parametro1,"y",parametro2, "¿Son anagramas?",sonAnagramas(parametro1,parametro2))
    print("La lista original es:",lista,"¿Hay números duplicados?",hayDuplicados(lista))
    print("La lista original es:",lista,"y al borrar los números duplicados regresa",borrarDuplicados(lista))
    print()

main()




