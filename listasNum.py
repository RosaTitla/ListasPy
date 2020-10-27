lista1=[] # creando una lista vacía
lista1.append(480) #agrega el número 480 a la lista1
print(lista1)

#solicitamos al usuario del programa
# el total de elementos que insertará en la lista
totElem=int(input('Total de elementos'))

#bucle para agregar a la lista los números dados por el usario
for i in range(totElem):
    numero=int(input('número:'))
    lista1.append(numero)
print(lista1)

#obtener el índice (posición) en el que se encuentra un elemento
print('el elemento 10 se encuentra en la posición: ',lista1.index(10))

#la función len calcula la longitud o tamaño de la lista
longitud=len(lista1)
print('longitud de la lista: ',longitud)
#bucle para sumar los elementos de la lista1
suma=0
for i in range(longitud):
    suma=suma+lista1[i]
print('suma total: ',suma)

#generar mediante range un conjunto de valores que se encuentren
# en el rango entre 3 y 9 y almacenálos en la lista1
#recuerda que range genera un número y lo almacena en la var i
lista2=[]
for i in range(3,10):
    lista2.append(i)
print("lista2:",lista2)

print("lista1:",lista1)

#borrar el elemento 10 de la lista
lista1.remove(10)
print('elemento 10 borrado')
print(lista1)

#otro método para borrar el elemento de la lista
# es del y borrará el elemento que se encuentra en la posición 2
del lista1[2]
print('elemento de la posición 2 borrado')
print(lista1)


#insert (posición,dato)
print('insertado 500 en la pos cero')
lista1.insert(0,500)
print(lista1)
print('insert varios elementos a partir de la posición especificada')
#ejemplo en la posición inserta el 99 y en la pos 3 el 88
# y los demas valores los recorre
lista1[2:2]=[99,88]
print(lista1)

print('sustituir el valor de una pos especificada')
#en la pos 3 sustiye al valor actual con 77
lista1[3]=77
print(lista1)

#ordenar una lista en forma ascendente
lista1.sort()
print(lista1)

#ordenar la lista en forma descendente
lista1.reverse()
print(lista1)

a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)
b[0] = 5
print(a)
print(b)

#  el contenido de la lista1 a lista3
lista3=[]
lista3=lista1[:]
print('lista 3: ', lista3)
lista4=[]
#realiza una copia de lista1 a lista4
# desde el elemento que se encuentra en la posición 2
# hasta el elemento que se encuentra la posición 4
print('lista1',lista1)
lista4=lista1[2:5]
print('lista 4',lista4)

lista5=[]
#realiza una copia de lista1 a lista5
# desde el elemento que se encuentra en la posición 2
# hasta el último elemento de la lista
#Si especificamos unicamente : esto indica el ult. elem
print('lista 1', lista1)
lista5=lista1[2:]
print('lista 5',lista5)

lista6=[]
#realiza una copia de lista1 a lista6
# desde el elemento que se encuentra en la posición 3
# hasta el penúltimo elemento de la lista
print('lista 1 ', lista1)
lista6=lista1[3:-1]
print('lista 6',lista6)


# otra forma para recorrer la lista1 por sus elementos
# en el siguiente ejemplo se recorre la lista1 y en
# la variable k se va almacenando el valor de cada elemento
# de la lista1, para elevarlo al cubo y asignarlo
# en la variable cubo y mostrarlo en pantalla

for k in lista1:
    cubo=k**3
    print('cubo:',cubo)

listaPares=[]
for i in range(2,11,2):
    listaPares.append(i)
print(listaPares)


