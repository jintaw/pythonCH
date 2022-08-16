
import re
l = "Beautiful is better than ugly."

string = "Two too."
matches = re.findall("t[wo]o" , string , re.IGNORECASE)

print(matches)


boo = "the ghost that says boo haunts the loo"

match = re.findall(".oo" , boo ,re.IGNORECASE )
print(match)

