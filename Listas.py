#Autor Patricio Mondragón
#Tarea 8


#Esta función suma los indices de una lista y los pone en otra
def sumarAcumulado(lista1):
	res = []
	last = 0
	for no in lista1:
		numf = no + last
		res.append(numf)
		last = numf
	return res
#Esta fución recorta una lista quitando el primer y el último índice
def recortarLista(lista2):
	print(lista2)
	res = []
	for no in range(len(lista2)):
		if no == 0:
			lista2[no]
		elif no == len(lista2) - 1:
			lista2[no]
		else:
			res.append(lista2[no])
	return res
#Esta fución revisa si los numeros de una lista estan ordenados
def estanOrdenados(lista3):
	last = lista3[0]
	for no in range(len(lista3)):
		if lista3[no] == last:
			last = last + 1
			pass
		else:
			return False
	return True

def sonReverso(lista4):
	an = lista4[1][::-1]
	if lista4[0] == an:
		return True
	else:
		return False

def sonAnagramas(lista5):
	res = sorted(lista5[0])
	resres = sorted(lista5[1])
	if res == resres:
		return True
	else:
		return False

def hayDuplicados(lista6):
	lista6 = sorted(lista6)
	last = 0
	for no in lista6:
		if last == no:
			return False
		else:
			last = no
	return True

def borrarDuplicados(lista6):
	lista6 = list(set(lista6))
	return lista6

def main():
    print("Ejercicio 1")
    lista1 = [1,2,3]
    final_res = sumarAcumulado(lista1)
    print("La lista [1,2,3] regresa la lista ",final_res)
    lista1 = []
    final_res = sumarAcumulado(lista1)
    print("La lista [] regresa la lista ",final_res)
    lista1 = [5]
    final_res = sumarAcumulado(lista1)
    print("La lista [5] regresa la lista ",final_res)


    print("Ejercicio 2")
    lista2 = [1,2,3,4,5]
    listarecortada = recortarLista(lista2)
    print("lista original [1,2,3,4,5] regresa",listarecortada)
    lista2 = [1,2,3]
    listarecortada = recortarLista(lista2)
    print("lista original [1,2,3] regresa",listarecortada)
    lista2 = []
    listarecortada = recortarLista(lista2)
    print("lista original [] regresa",listarecortada)

    print("Ejercicio 3")

    lista3 = [1,2,3]

    numerosordenados = estanOrdenados(lista3)
    print("La lista [1,2,3] regresa",numerosordenados)
    lista3 = [1,3,2]
    numerosordenados = estanOrdenados(lista3)
    print("La lista [1,3,2] regresa", numerosordenados)

    print("Ejercicio 4")


    prms = ['amor', 'roma']
    anagramas= sonAnagramas(prms)
    print("amor y roma son anagramas",anagramas)
    prms = ["hola","hello"]
    anagramas = sonAnagramas(prms)
    print("hola y hello no son anagramas",anagramas)


    print("Ejercicio 5")
    lista6 = [1,2,2,3,4]
    duplicados = hayDuplicados(lista6)
    print("Si hay numeros duplicados",duplicados)
    lista6 = [1,2,3,4,5]
    duplicados = hayDuplicados(lista6)
    print("No hay numeros duplicados",duplicados)

    print("Ejercicio 6")
    lista6 = [1,2,2,4]
    listasinduplicados = borrarDuplicados(lista6)
    print("La lista [1,2,2,4] regresa",listasinduplicados)


main()