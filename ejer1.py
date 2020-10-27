miLista=list()
miLista.append(1)
miLista.append(9)
miLista.append(55)
miLista.append(10)
print(miLista)
print('longitud', len(miLista))
print('minimo',min(miLista))
print('maximo',max(miLista))
print('suma',sum(miLista))
print('promedio',sum(miLista)/len(miLista))

print('valor', miLista[2])
print(('pos', miLista.index(1)))

for i in range(10):
    miLista.append(i)
print(miLista)
lista2=list()
for x in range(len(miLista)-1):
    lista2.append(miLista[x]+10)

print(miLista)
print(lista2)

for z in range(5):
    num=int(input('numero'))
    lista2.append(num)
print(lista2)

lista2.remove(19)
print(lista2)

del lista2[2]
print(lista2)
lista2.insert(3,100)
lista2[5]=800
print(lista2)