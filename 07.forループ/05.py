from hashlib import new


list1 = [8,19,148,4]
list2 = [9,1,33,83]
new_list = []

for x in list1:
    for y in list2:
        new_list.append(x * y)
        
print(new_list)

        
    