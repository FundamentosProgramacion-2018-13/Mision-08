# encoding: UTF-8
# Luis Jonathan Rosas Ramos
# A01377942
# Tarea 08


def sumarAcumulado(lista):
    listaSuma = [] # Crear una nueva lista
    for numero in range (len(lista)): # visitar el dato numero en la posicion de la lista
        acumulado = sum(lista[:numero+1])   #crear la suma de la lista, de numero en numero, gaurdandolo n acumulado
        listaSuma.append(acumulado) #Agregar este parametro a la lista y meterlo a una lista vacia
    return listaSuma


def recortarLista(lista):
    listaRecortada = lista[1:len(lista)-1] # la nueva lista, inicia el la posicion 2 y termina una antes de que acabe la cadina
    return listaRecortada


def estanOrdenados(lista):
    for k in range(len(lista)): #visitar cada elemento en cada posicion de la lista
        if k != 0:  # iniciar a comparar a partir del 0
            if lista[k] < lista[k-1]:   # si la posicion uno de la lisa es menor que la dos, en automatico no esta ordenada
                return False
    else:   # en caso contrario esta ordenada
        return True


def sonAnagramas(listaUno,listaDos):
    listaMayusculasUno = listaUno.upper()   # Transformar la listas en mayusculas
    listaMayusculasDos = listaDos.upper()
    contador = 0
    while len(listaUno) == len(listaDos): #Reliza una comparacion, donde las dos listas tengan el mismo numero de letras
        for i in listaMayusculasUno:    #visitar parametros de lista uno
            for k in listaMayusculasDos: #visitar paramtros de lista dos
                if i == k:  #Si ambos elementos son iguales
                    contador = contador + 1 #sumar a contador
                    if contador == len(listaUno):   #ya que si ya comparo todas los elementos de la lista 1 con la 2,
                        return True         #y estos llegan al contador igual al largo de la lista, quiere decir que todos
                                        # los elemntos de lista Uno estan en lista Dos
        else:
            return False
    else:
        return False


def hayDuplicados(lista):
    variable = 1
    for i in lista: #buscar datos en la lista
        for k in lista[variable::]: #crear otra busqueda de datos en la posicion 2
            variable += 1   #despues buscarla en una 3
            if i == k:  #si ambos son iguales regrear verdadero
                return True
        else:
            return False


def borrarDuplicados(listaNumeros):
    for k in range(len(listaNumeros) -1, -1, -1): #comenzar con la posicion de la lista de forma invertida
        duplicados = listaNumeros.count(listaNumeros[k]) #regresar la posicion de la lista duplicada
        if duplicados > 1: # si existe un numero duplicado, habra que quitarlo
            listaNumeros.remove(listaNumeros[k]) #quitar ese numero en la poscion que lo alla encontrado

def main():
    print('---------------------------------------------')
    print('Ejercicio 1:')
    for x in [[5, 10, 15, 20, 25], [], [10]]:
        print('La lista', x, 'regresa la lista acumulada', sumarAcumulado(x))
    print('--------------------------------------------------------')
    print('Ejercicio 2:')
    for x in [[1, 2, 3, 4, 5], [1,2,3], []]:
        print('Lista original', x, ', regresa', recortarLista(x))
    print('---------------------------------------------------')
    print('Ejercicio 3:')
    for x in [[7, 8, 9, 10], [4, 5, 3, 1, 30], [5, 5, 7]]:
        print('La lista', x, 'está ordenada?', estanOrdenados(x))
    print('---------------------------------------------------')
    print('Ejercicio 4: ')
    print('Perro y Ropa son anagramas?', sonAnagramas('perro', 'ropa'))
    print('Roma y mora son anagramas?', sonAnagramas('roma', 'mora'))
    print('tarta y trata son anagramas?', sonAnagramas('tarta', 'trata'))
    print('-----------------------------------------------------')
    print('Ejercicio 5: ')
    for x in [[5,10,15,20,25], [1,1,3,4,6,6,7,9,9], [6,6,8,10,1]]:
        print('La lista', x, 'tiene duplicados?', hayDuplicados(x))

    print("---------------------------------------------------")
    print('Ejercicio 6: ')
    for x in [[5,10,15,20,25], [1,1,3,4,6,6,7,9,9], [6,6,8,10,1]]:
        y = x.copy()
        borrarDuplicados(y)
        print('La lista', x, 'sin duplicados es:', y)


main()