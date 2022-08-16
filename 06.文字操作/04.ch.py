from operator import index
from posixpath import split
from textwrap import indent


text = "where? who? when?"
text_split = text.split(" ")
print(text_split)

list = ["the" , "fox" , "jumped" , "."]
list = " ".join(list)
print(list)
list = list[0:-2] + "."
print(list)


doller = "A screaming comes across the sky."
doller = doller.replace("s" , "$")
print(doller)


first = "Hemingway"
first = first.index("m")
print(first)


three = "three"
for x in three:
    print(x)

