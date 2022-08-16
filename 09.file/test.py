import os
from tkinter import W
path = os.path.join("C:" , "WSL_work" )
print(path)

st = open("st.txt" , "w" , encoding = "utf-8")
st.write("こんにちは！")
st.close()

with open("st.txt" , "w" , encoding = "utf-8") as f :
    f.write("こんにちは !!")

with open ("st.txt" , "r" ,encoding="utf-8") as f:
    print(f.read())
    

my_list = []

with open("st.txt" , "r" , encoding= "utf-8") as f:
    my_list.append(f.read())

print(my_list)


import csv
with open("st.csv" , "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two" , "three"])
    w.writerow(["four" , "five" , "six"])

with open("st.csv" , "r") as f:
    r = csv.reader( f , delimiter=",")
    for row in r :
        print(",".join(row))
        

