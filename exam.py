filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames=[]
for archi in filenames:
    newfilenames.append(archi.replace('.hpp','.c'))
print(newfilenames)


def pig_latin(text):
    say = ""
    lista1=list()
    # Separate the text into words
    words = text.split(' ')
    for word in words:
        # Create the pig latin word and add it to the list
        lista1.append(word[1:]+word[0]+'ay')
        # Turn the list back into a phrase
        say=' '.join(lista1)
    return say




print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"