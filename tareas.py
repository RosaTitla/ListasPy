listaPares=[3,4,2,1,8,3,5,7,2,1,8,0]
s=0

for m in range(2,11,2):
  s=s+listaPares[m]
print(listaPares)
print(s)
#Escribir un programa que reemplace
# el número que se encuentra en la
# pocision central en la lista con un
# número entero ingresado por el usuario
lista=[3,4,2,1,8,3,5,7,2,1,8]
print(lista)
long=len(lista)
#divide entre 2 y se queda con la parte entera
posCentral=long//2
num=int(input('numero: '))
for m in range(long):
    if m==posCentral:
        lista[m]=num
print(lista)
ultimo=len(lista)
print(len(lista))
del lista[ultimo-1]

#ordenarlas y eliminar el ultimo de la lista
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)
#Removes and returns the last item
lastitem = mylist.pop()
print(lastitem)
#pop parametro position
#Removes and returns the item at position
encontrado=mylist.pop(2)
print(mylist)

#operador + para agregar un elem a la list
origlist = [45,32,88]
#origlist.append("cat")
origlist=origlist+["cat"]
print(origlist)

alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)

lst= [3,0,9,4,1,7]
new_list=[]
for i in range(len(lst)):
   new_list.append(lst[i]+5)
print(new_list)


#Dada la lista de números,
# numbs, cree una nueva lista de esos mismos números
# aumentados en 5.
# Guarde esta nueva lista en la variable newlist.
numbs = [5, 10, 15, 20, 25]
newlist=[]

for x in numbs:
    newlist.append(x+5)
print(newlist)

#Desafío Ahora haga lo mismo que en el problema
# anterior, pero no cree una nueva lista.
# Sobrescriba los números de la lista de modo que
# cada uno de los números originales aumente en 5.


numbss = [5, 10, 15, 20, 25]
for i in (range(len(numbss))):
    numbss[i]=numbss[i]+5
print(numbss)

lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums=[]
for n in lst_nums:
    larger_nums.append(n*2)
print(larger_nums)


