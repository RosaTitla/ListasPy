nums = [3, 5, 8]
accum = []
for w in nums:
    x = w**2
    accum.append(x)
print(accum)

alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)
#We can also remove elements from a list
# by assigning the empty list to them
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)
#We can even insert elements into a list
# by squeezing them into an empty slice
# at the desired location.
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
#alist[4] = ['e']
print(alist)

#Strings are Immutable
# greeting = "Hello, world!"
# greeting[0] = 'J'            # ERROR!
# print(greeting)

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was

phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
excited_phrase_complete = phrase_complete[:-1] + "!"

alist = [4,2,8,6,5]
alist[2] = True
print(alist)
#[4,2,True,6,5] no inserta un nuevo, sustituye




