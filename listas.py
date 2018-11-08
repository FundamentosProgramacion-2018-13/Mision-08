# Autor: Luis Humberto Burgueño Paz
# Funciones con listas


# Recibe como parámetro una lista de números enteros y regresa una nueva con la suma acumulada de los datos.
def sumarAcumulado(lista):
   acumulados = []
   suma = 0
   for dato in lista:
       suma = suma + dato
       acumulados.append(suma)
   return acumulados


# Recibe como parámetro una lista de valores enteros y regresa una nueva lista, pero sin el primero y el último elemento
def recortarLista(lista):
   recorte = lista[1:len(lista)-1:]
   return recorte


# Recibe como parámetro una lista de valores y regresa True si los valores están ordenados, False en otro caso
def estanOrdenados(lista):
   for k in range(1, len(lista)):
       if lista[k] < lista[k-1]:
           return False
   return True


# Recibe dos cadenas como parámetro e indica si son anagramas
def sonAnagramas(cadena1, cadena2):
   cadena1Mayus = cadena1.upper()
   cadena2Mayus = cadena2.upper()
   cadenalista = list(cadena1Mayus)
   cadenalista.sort()
   cadenalista2 = list(cadena2Mayus)
   cadenalista2.sort()
   if cadenalista == cadenalista2:
       return True
   return False


# Recibe como parámetro una lista y checa si hay duplicados
def hayDuplicados(lista):
   for dato in lista:
       a = lista.count(dato)
       if a > 1:
           return True
   return False


# Recibe como parámetro una lista y la regresa ordenada y sin duplicados
def borrarDuplicados(lista):
   lista.sort()
   for dato in lista:
       while lista.count(dato) > 1:
           lista.remove(dato)
       lista=lista
   return lista


# Función Principal. Llama a las demás funciones. Prueba con 5 listas distintas
def main():
   lista = [1, 2, 3, 4, 5]
   lista2 = []
   lista3 = [5]
   lista4 = [1, 2, 3]
   lista5 = [1, 5, 3, 2, 1, 4, 3]
   listas = [lista, lista2, lista3, lista4, lista5]
   print("Ejercicio 1")
   for listaActual in listas:
       a = sumarAcumulado(listaActual)
       print("La lista", listaActual, "regresa la lista acumulada", a)
   print("Ejercicio 2")
   for listaActual in listas:
       a = recortarLista(listaActual)
       print("La lista", listaActual, "regresa la lista recortada", a)
   print("Ejercicio 3")
   for listaActual in listas:
       a = estanOrdenados(listaActual)
       if a == True:
           print("La lista", listaActual, "está ordenada")
       if a == False:
           print("La lista", listaActual, "no está ordenada")
   print("Ejercicio 4")
   palabra1 = "Mora"
   palabra2 = "amor"
   palabra3 = ""
   palabra4 = ""
   palabra5 = "leon"
   palabra6="leono"
   a = sonAnagramas(palabra1, palabra2)
   b = sonAnagramas(palabra3, palabra4)
   c = sonAnagramas(palabra5, palabra6)
   if a == True:
       print(palabra1, "y", palabra2, "son anagramas")
   if a == False:
       print(palabra1, "y", palabra2, "no son anagramas")
   if b == True:
       print(palabra3, "y", palabra4, "son anagramas")
   if b == False:
       print(palabra3, "y", palabra4, "no son anagramas")
   if c == True:
       print(palabra5, "y", palabra6, "son anagramas")
   if c == False:
       print(palabra5, "y", palabra6, "no son anagramas")
   print("Ejercicio 5")
   for listaActual in listas:
       a = hayDuplicados(listaActual)
       if a == True:
           print("La lista", listaActual, "tiene duplicados")
       if a == False:
           print("La lista", listaActual, "no tiene duplicados")
   print("Ejercicio 6")
   for listaActual in listas:
       a = borrarDuplicados(listaActual)
       print("La lista", listaActual, "regresa la lista sin duplicados", a)


main()
