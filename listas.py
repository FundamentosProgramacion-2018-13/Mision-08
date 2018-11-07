#Zabdiel Valentín Garduño Vivanco
#Creación de funciones utilizando diferentes listas y ejercicios.


def sumarAcumulado(lista):
    listaN=[]
    for k in range(1,len(lista)+1):
        listaN.append(sum(lista[:k]))#Va sumando los numeros por secciones.
    return listaN


def recortarLista(lista):
    listaN=[]
    for k in range(1,len(lista)-1): #Se crea una lista nueva y con un For se agregan del 2° hasta el penultimo.
        listaN.append(lista[k])
    return listaN

def estanOrdenados(lista):
    variable=0
    for k in range(1,len(lista)):#Con un for analiza los datos por pares, si uno es mayor que otro.
        if lista[k]>lista[k-1]:
            variable=1
        else:
            variable=2  #Si en dado caso no estan ordenados se hace un break y termina el For
            break
    if variable==1:
        return 'True'
    if variable==2:
        return "False"

def sonAnagramas(cadena,cadena02):
    palabra01=cadena.lower()
    palabra02=cadena02.lower()
    variable=0
    for x in range(0,len(palabra01)):
        for y in range(0,len(palabra02)):#Se crea un For dentro de otro For
            if palabra01[x]==palabra02[y]:#Se analizan cada letra por cada letra de la otra palabra
                variable=1#Si una letra es igual hace un break y sigue con la siguiente
                break
            elif palabra01[x]!=palabra02[y]:#Si alguna palabra no fue encontrada entonces es False
                variable=2

    if variable==1 and len(palabra01)==len(palabra02):
        return 'True'
    elif variable==2:
        return "False"
    elif len(palabra01)!=len(palabra02):
        return "False"

def hayDuplicados(lista):
    variable=len(lista)#Se cuenta el numero de datos de la lista y almacena en variable

    variable02=len(list(set(lista)))#Con un comando se eliminan los datos duplicados y alamacena en variable 02
    if variable==variable02:#Si despues de la correccion siguen siendo lo mismo entonces es False
        return "False"
    if variable>variable02:#Si depues de la correcion hay diferecia de datos entonces es True
        return "True"
def borrarDuplicados(lista):
    lista=list(set(lista))#Solamente se eliminan y ordenan los datos en la lista ya creada.
    return lista


def main():
    lista00=[1,2,3,4,5]
    lista01=[]
    lista02=[5]
    print("Ejercicio 1: ")
    print("La lista",lista00,"regresa la lista acumulada",sumarAcumulado(lista00))
    print("La lista",lista01,"regresa la lista acumulada",sumarAcumulado(lista01))
    print("La lista",lista02,"regresa la lista acumulada",sumarAcumulado(lista02))
    print()#Espacio
    lista03=[1,2,3,4,5]
    lista04=[1,2,3]
    lista05=[]
    print("Ejercicio 2: ")
    print("La lista",lista03,"regresa ",recortarLista(lista03))
    print("La lista",lista04,"regresa ",recortarLista(lista04))
    print("La lista",lista05,"regresa ",recortarLista(lista05))
    print()#Espacio
    lista06=[1,2,3,4,5]
    lista07=[1,2,3,2]
    lista08=[7, 23, 15]
    print("Ejercicio 3: ")
    print("La lista",lista06,"regresa ",estanOrdenados(lista06))
    print("La lista",lista07,"regresa ",estanOrdenados(lista07))
    print("La lista",lista08,"regresa ",estanOrdenados(lista08))
    print()#Espacio
    print("Ejercicio 4:")
    print("Las palabras","Roma y Mora","regresa",sonAnagramas("Roma","Mora"))
    print("Las palabras","Hola y Hello","regresa",sonAnagramas("Hola","Hello"))
    print("Las palabras","ana y nana","regresa",sonAnagramas("ana","nana"))
    print()#Espacio
    lista09=[1,2,3,1,4,5]
    lista10=[5,7,4,6,10]
    lista11=[1,2,3,2,5]
    print("Ejercicio 5: ")
    print("La lista",lista09,"regresa ",hayDuplicados(lista09))
    print("La lista",lista10,"regresa ",hayDuplicados(lista10))
    print("La lista",lista11,"regresa ",hayDuplicados(lista11))
    print()#Espacio
    lista12=[1,8,3,4,3,1,8,2,7,8]
    lista13=[1,2,3,1,2,3]
    lista14=[1,2,3,4,5]
    print("Ejercicio 6: ")
    print("La lista",lista12,"regresa ",borrarDuplicados(lista12))
    print("La lista",lista13,"regresa ",borrarDuplicados(lista13))
    print("La lista",lista14,"regresa ",borrarDuplicados(lista14))

main()
