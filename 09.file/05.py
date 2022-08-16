
input = input("something:")

with open("input.txt" , "w" ,encoding="utf-8") as f:
    f.write(input)
    