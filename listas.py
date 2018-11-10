#Irma Gómez Carmona
#A01747743
#Funciones que utilizan listas

def sumarAcumulado(lista):
    nuevaLista=[]
    suma=0
    for j in range (len(lista)):
        b=lista[j]
        suma+=b   #se suma el valor de cada indíce en un acumulador
        nuevaLista.append(suma)  #el acumulador se agrega en la nueva lista
    return nuevaLista


def recortarLista(lista):
    listaRecortada=[]
    for k in range (1,len(lista)-1):  #apartir del segundo número hasta el penúltimo
        num=lista[k]
        listaRecortada.append(num)  #se agregan los valores a la nueva lista
    return listaRecortada


def estanOrdenados(lista):
      #si hay al menos un elemento en la lista
        for k in range (len(lista)-1):
            if lista[k]+1!=lista[k+1]:
                # si el valor del indice k mas 1 no es igual al valor de la siguiente indice no estan ordenados
                return False
        return True


def sonAnagramas(cadena1,cadena2):
    #se ponene todas las letras en mayusculas
    cadena1= cadena1.upper()
    cadena2= cadena2.upper()
    #se dividen las letras en elementos de una lista
    listaA=list(cadena1)
    listaB=list(cadena2)
    #se ordenan las letras alfabeticamente dentro de la lista
    listaA.sort()
    listaB.sort()
    if len(listaA)==len(listaB):
        #verificar si el tamaño de las cadenas es el mismo
        for k in range (len(cadena1)-1):
            #comparar cada elemento de la cadenaA con el de la cadenaB
            if listaA[k]!=listaB[k]:
                #si son diferentes regresa falso
                return False
    else:
        #si no son del mismo tamaño las cadenas regresa falso
        return False
    #si no aplica ninguna condición anterior, regresa falso
    return True


def hayDuplicados(lista):
    for k in range (len(lista)-1):  #define el indice de cada valor en la lista
        for j in range (len(lista)-1,k,-1): #recorre la lista del ultimo número hasta el que sigue después de k
            if lista[k]==lista[j]:
                #si llegar a coincidir algún valor, regresa true
                return True
    return False  #si no coincide ningun valor, regresa false


def borrarDuplicados(lista):
    for k in range (len(lista)-1):  #define el indice de cada valor en la lista
        for j in range (len(lista)-1,k,-1): #recorre la lista del ultimo número hasta el que sigue después de k
            if lista[k]==lista[j]:
                #si son iguales borrar el elemento en la posición j
                lista.pop(j)
    return lista


def main ():
    #listas de prueba
    listaEjemplo=[1,2,1,3,3,1,4,1,5]
    listaEjemplo2=[]
    listaEjemplo3=[1,2,3,4,5]
    #cadenas de prueba
    cadenaPrueba1="roma"
    cadenaPrueba2="Amor"
    cadenaPrueba3="ropa"
    cadenaPrueba4="examen"
    cadenaPrueba5="examenes"

    #Pruebas
    print("----Ejericio 1----")
    print("La lista",listaEjemplo,"regresa la lista acumulada",sumarAcumulado(listaEjemplo))
    print("La lista",listaEjemplo2,"regresa la lista acumulada",sumarAcumulado(listaEjemplo2))
    print("La lista", listaEjemplo3, "regresa la lista acumulada", sumarAcumulado(listaEjemplo3))
    print("----Ejericio 2----")
    print("Lista original",listaEjemplo,", regresa",recortarLista(listaEjemplo))
    print("Lista original", listaEjemplo2, ", regresa", recortarLista(listaEjemplo2))
    print("Lista original", listaEjemplo3, ", regresa", recortarLista(listaEjemplo3))
    print("----Ejericio 3----")
    print("Los elementos de la lista", listaEjemplo, "estan ordenados: ", estanOrdenados(listaEjemplo))
    print("Los elementos de la lista", listaEjemplo2, "estan ordenados: ", estanOrdenados(listaEjemplo2))
    print("Los elementos de la lista", listaEjemplo3, "estan ordenados: ", estanOrdenados(listaEjemplo3))
    print("----Ejericio 4----")
    print("'%s' y '%s' son anagramas: "%(cadenaPrueba1,cadenaPrueba2),sonAnagramas(cadenaPrueba1,cadenaPrueba2))
    print("'%s' y '%s' son anagramas: " % (cadenaPrueba2, cadenaPrueba3), sonAnagramas(cadenaPrueba2, cadenaPrueba3))
    print("'%s' y '%s' son anagramas: " % (cadenaPrueba4, cadenaPrueba5), sonAnagramas(cadenaPrueba4, cadenaPrueba5))
    print("----Ejericio 5----")
    print("Hay duplicados en la lista ",listaEjemplo,": ", sonDuplicados(listaEjemplo))
    print("Hay duplicados en la lista ", listaEjemplo2, ": ", sonDuplicados(listaEjemplo2))
    print("Hay duplicados en la lista ", listaEjemplo3, ": ", sonDuplicados(listaEjemplo3))
    print("----Ejericio 6----")
    print("Lista orginial: ",listaEjemplo,end=", ")
    print("lista sin duplicados:", borrarDuplicados(listaEjemplo))
    print("Lista orginial: ", listaEjemplo2, end=", ")
    print("lista sin duplicados:", borrarDuplicados(listaEjemplo2))
    print("Lista orginial: ", listaEjemplo3, end=", ")
    print("lista sin duplicados:", borrarDuplicados(listaEjemplo3))


main()

'''    '''
