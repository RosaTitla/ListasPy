
listaH=[z for z in range(6) if z%2==0]
print(listaH)

list1=[elem for elem in listaH]
print(list1)
n=int(input('dame el num que borrar'))

lista2=[elem**2 for elem in listaH if elem>2]
print(lista2)