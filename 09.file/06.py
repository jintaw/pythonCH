import csv

list_all = []

list1 = ["topgun" , "risky Businnes " , "minorityreprt"]
list2 = ["titanic" , "therevanant" , "inception"]
list3 = ["traing day" , "man on fire" , "flight"]
list4 = ["あいう" , "えお" , "かき"]

list_all = [list1] + [list2] + [list3] + [list4]

print(list_all)

with open("list.csv" , "w" , encoding="utf-8" ) as csvfile:
    w = csv.writer(csvfile , delimiter=",")
    for i , list in  enumerate(list_all):
        w.writerow(list)
