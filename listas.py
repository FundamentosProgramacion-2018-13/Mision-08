#Autor: David Rodriguez
#Prueba funciones con listas

#Suma los primeros dos elementos entre si y luego se suma el siguiente número
def sumarAcumulado(lista1):
    lista2 = []
    suma = 0
    for k in lista1:
        suma = suma+k
        lista2.append(suma)
    return lista2


#Recorta el primero y el último número de la lista
def recortarLista(lista1):
    listaRecortada = []
    listaRecortada = lista1[1:len(lista1)-1]
    return listaRecortada


#Revisa si la lista está ordenada
def estanOrdenados(lista1):
    lista2 = []
    for k in range(len(lista1)):
        if k != 0:
            if lista1[k] < lista1[k-1]:
                return False
    if   len(lista1) == 0:
        return True


#Revisa si la cadena1 es un anagrama de la cadena2
def sonAnagramas(cadena1, cadena2):
    lista1 = [cadena1]
    lista2 = [cadena2]
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        return True
    else:
        return False


#Entrega true si hay números repetidos o false de lo contrario
def hayDuplicados(lista1):
    for k in lista1:
        contador = lista1.count(k)
        if contador > 1:
            return True
        else:
            return False


#Borra los números duplicados de la lista original
def borrarDuplicados(lista1):
    lista2 = []
    for k in lista1:
        if lista2.count(k) == 0:
            lista2.append(k)
    lista1 = lista2
    return lista2


#Función principal
def main():
    lista1 = [1,2,3,4,4,1,5]
    cadena1 = "Amor"
    cadena2 = "Roma"
    print("Ejercicio1:")
    print("La lista", lista1, "regresa la lista acumulada", sumarAcumulado(lista1))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 2:")
    print("La lista original", lista1, "regresa", recortarLista(lista1))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 3:")
    print("La lista", lista1, "esta ordenada::", estanOrdenados(lista1))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 4:")
    print("La cadena", cadena1, "es un anagrama de", cadena2, ":", sonAnagramas(cadena1, cadena2))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 5:")
    print("En la lista", lista1, "hay caracteres duplicados:", hayDuplicados(lista1))
    print("-------------------------------------------------------------------------")
    print("Ejercicio 6:")
    print("Quitando los duplicados de", lista1, "se obtiene", borrarDuplicados(lista1))


#Llama a la función principal
main()