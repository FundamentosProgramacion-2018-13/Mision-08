#Jose Luis Mata Lomeli
#Mision 8

#Lista dada por el usuario

def crearLista():
    lista = []
    numero = int(input("Escribe tus valores [-1 para termina de agregar datos]: "))

    while numero != -1:
        #Agregar los num diferentes a -1 a la lista
        lista.append(numero)
        numero = int(input("Escribe tus valores [-1 para terminar de agregar datos]: "))

    #Imprimir la lista de los datos dados
    return (lista)

# Recibe como parametro la Lista Principal para crear y regresar una nueva xon la suma acumulada de los datos
def sumarAcumulado(lista):
    z = []
    suma = 0
    for i in lista:
        suma += i
        z.append(suma)
    return z

#Recortar el primer y ultimo numero de la lista dada por el usuario
def recortarLista(lista):
    return lista[1: len(lista) -1]

#Mostrar al usuario si la lista de numeros dada esta ordenada o no
def estanOrdenadas(lista):
    if lista == sorted(lista):
        return "Estan ordenados"
    else:
        return "La lista no esta ordenada. Es...", sorted(lista)

#Comprobar si dos palabras dadas son un anagrama
def sonAnagramas(cadena1, cadena2):

    #Con las palabras dadaa por el usuario, las convertimos listas por cada letra de estas
    lista1 = list(cadena1)
    lista2 = list(cadena2)

    #Luego las ordenamos
    lista1.sort()
    lista2.sort()

    #Aplicamos un contador y nombramos un true
    pos = 0
    igual = True

    #Mientras la posicion inicia en 0 y es menor a el conteo de la cadena 1 y true
    while pos < len(cadena1) and igual:
        #Si ambas listas son iguales
        if lista1[pos] == lista2[pos]:
            #Contador
            pos += 1
        else:
            igual = False

    return igual

#Borrar los duplicados de una lista dada
def borrarDuplicados(a):
    return list(set(a))


#Funciones
a = crearLista()
print(a)

b = sumarAcumulado(a)
print(b)

c = recortarLista(a)
print(c)

d = estanOrdenadas(a)
print(d)


cadena1 = input("Escribe una palabra: ")
cadena2 = input("Escribe otra palabra a comparar: ")

e = sonAnagramas(cadena1, cadena2)
print(e)


g = borrarDuplicados(a)
print(g)