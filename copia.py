lista=list()
lista.append(44)
lista.append(55)
lista.append(69)
lista.append(33)
lista.append(48)
lista2=[]
lista2=lista[:]
print(lista2)
print(lista)
lista3=[]
lista3=lista[2:] #slice  rebanada
print(lista3)
lista4=[]
lista4=lista[:-2] #antepenultimo
print(lista4)

for i in range(5):
    print(i,end=' ')
print()
for elem in lista:
    print(elem, end='\t')
print()
listaResumida=[i for i in range(10)]
print(listaResumida)
listaResumida1=[i for i in lista if i%2==0]
print(listaResumida1)