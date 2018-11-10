#Autor: Diana Marisol Medina Bravo

def sumarAcumulado(listaNumeros1):
    n = 0
    nuevaLista = []
    for dato in listaNumeros1:
        num=dato+n
        n=num
        nuevaLista.append(n)

    return nuevaLista

def recortarLista(listaNumeros1):
        a=len(listaNumeros1)
        nuevaLista=[]
        if a>0:
            listaNumeros1.remove(a)
            listaNumeros1.remove(1)
            nuevaLista=listaNumeros1
        if a==0:
            listaNumeros1=[]
            nuevaLista = listaNumeros1

        return nuevaLista

def estanOrdenadas(listaNumeros2):
    n=0
    a=len(listaNumeros2)
    c=0
    for dato in listaNumeros2:
       if dato>n:
           n=dato
           c+=1
           if c==a:

               return True
       else:
           return False

def sonAnagramas(cadena1, cadena2):
    cadenaU = cadena1.lower()
    cadenaD = cadena2.lower()

    cadenaUno=list(cadenaU)
    cadenaDos=list(cadenaD)
    c=0
    for dato in cadenaUno:
        a = len(cadenaUno)
        b = len(cadenaDos)
        c += 1
        if a==b:
            if dato in cadenaDos:
                if c==a:
                    return True
            else:
                return False
        else:
            return False


def hayDuplicados(listaNumeros):
    for dato in listaNumeros:
        a=listaNumeros.count(dato)
        if a>1:
            return True
        else:
            return False

def borrarDuplicados(listaNumeros4):

        for k in range(len(listaNumeros4)):
            for datos in listaNumeros4:
                a = listaNumeros4.count(datos)
                if 1 < a:
                    listaNumeros4.remove(datos)

        return (listaNumeros4)

def main():
    #Pruebas problema 1
    print("Ejercicio 1")
    listaNumeros1 = [1,2,17,6,7]
    problema1=sumarAcumulado(listaNumeros1)
    print ("La lista", listaNumeros1 ,"regresa la lista acumulada", problema1)
    listaNumeros1=[]
    problema1 = sumarAcumulado(listaNumeros1)
    print("La lista", listaNumeros1, "regresa la lista acumulada", problema1)

    print("")

    # Pruebas problema 2
    print("Ejercicio 2")
    listaNumeros=[1,2,3,4,5]
    print("Lista original es",listaNumeros)
    problema2= recortarLista(listaNumeros)
    print("Regresa",problema2)
    listaNumeross = [1, 2, 3]
    print("Lista original es", listaNumeross)
    problema2 = recortarLista(listaNumeross)
    print("Regresa", problema2)

    print("")

    # Pruebas problema 3
    print("Ejercicio 3")
    listaNumeros2=[3,6,8,10]
    problema3=estanOrdenadas(listaNumeros2)
    print("Recibe lista", listaNumeros2,"y regresa",problema3)
    listaNumeros2 = [7,23,15]
    problema3 = estanOrdenadas(listaNumeros2)
    print("Recibe lista", listaNumeros2, "y regresa", problema3)
    listaNumeros2 = [6, 12, 4, 56]
    problema3 = estanOrdenadas(listaNumeros2)
    print("Recibe lista", listaNumeros2, "y regresa",problema3)

    print("")

    # Pruebas problema 4
    print("Ejercicio 4")
    cadena1="roma"
    cadena2="mora"
    problema4=sonAnagramas(cadena1,cadena2)
    print ("Recibe la cadena",cadena1,"y la cadena", cadena2,",regresa",problema4)

    cadena1="Hello"
    cadena2 = "Hola"
    problema4 = sonAnagramas(cadena1, cadena2)
    print("Recibe la cadena",cadena1,"y la cadena", cadena2,",regresa",problema4)

    print("")

    # Pruebas problema 5
    print("Ejercicio 5")
    listaNumeros3=[1,2,3,1,4,5]
    problema5=hayDuplicados(listaNumeros3)
    print("Lista",listaNumeros3,"regresa",problema5)
    listaNumeros3 = [5,7,4,6,10]
    problema5 = hayDuplicados(listaNumeros3)
    print("Lista",listaNumeros3,"regresa",problema5)

    print("")

    # Pruebas problema 6
    print("Ejercicio 6")
    print("Lista original es",listaNumeros3)
    problema6=borrarDuplicados(listaNumeros3)
    print("Regresa",problema6)
    listaNumeros4=[1,8,3,4,3,1,8,2,7,8]
    print("La lista original es:",listaNumeros4)
    problema6 = borrarDuplicados(listaNumeros4)
    print("Regresa",problema6)







main()