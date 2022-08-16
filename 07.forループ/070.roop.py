from re import X


tm = ["god" , "narcos" , "vice"]
i = 0
for show in tm:
    new = tm[i]
    new = new.upper()
    tm[i] = new
    i += 1
print(tm)


tv = ["got" , "mevius"]
for i , new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)


x = 10
while x > 0:
    print(x)
    x -= 1
print("end")


qs = ["name?",
      "fav.color?",
      "quest?"]
n = 0
while True:
    print("quit type q!!")
    a = input(qs[n])
    if a == "q":
        break
    n = (n +1 ) %3


for i in range(1,6):
    if i == 3:
        continue
    print(i)
