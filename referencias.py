#¿Cuál es el valor de y
#después de que se haya evaluado el siguiente código:

w = ['Jamboree', 'get-together', 'party']
y = ['celebration']
y = w
print(y)

#¿Qué se imprime en las siguientes declaraciones?

alist = [4,2,8,6,5]
blist = alist
blist[3] = 999
print(alist)

alista = [4, 5, 6]
print('id',id(alista))
origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))

origlista = [45,32,88]
aliaslist = origlista
origlista += ["cat"]
origlista = origlista + ["cow"]

person = input('Enter your name: ')
print('Hello {}!'.format(person))


origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)



v = 2.34567
print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))