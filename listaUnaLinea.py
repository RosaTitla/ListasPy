#El siguiente ejemplo
# creará una lista llamada listaCuadrados en la que se almacenará
# los valores generados por range (desde el 3 hasta el 9)
# y con ayuda del for elevará al
# cuadrado cada número generado por el range

listaCuadrados = [x ** 2 for x in range(3,10)]
print('cuadrados', listaCuadrados)

#El siguiente ejemplo
# creará una lista llamada listapotencias en la que se almacenará
# los valores generados por range (desde el 0 hasta el 7)
# y con ayuda del for elevará el 2 a la i(0,1,2,3,4,5,6,7)

listaPotencia = [2 ** i for i in range(8)]
print('lista Potencia', listaPotencia)


#El siguiente ejemplo
# creará una lista llamada listaImpares en la que se almacenará
# solo los elementos impares de la lista cuadrados.

listaImpares = [x for x in listaCuadrados if x % 2 != 0]
print('impares', listaImpares)

listaP = [i/2 for i in range(100,120)]
print('lista Potencia', listaP)

lis=['Rosario', 'Jennifer', 'Pablo']

letras=['a','c,','t']

variosTipos=['r',5,'Joshua',3.6, True, [55,21,34,10]]

# in
num=16
if num in listaCuadrados:
    print("el numero", num, 'se encuentra en la lista')


# not in
num=1
if num not in listaCuadrados:
    print("el numero", num, 'NO se encuentra en la lista')

# intercambiar los elementos de la
# lista para revertir su orden:
miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print(miLista)
miLis=[0,0,0,0]
for i in range(4):
    miLis[i]=input('numero')
print(miLis)