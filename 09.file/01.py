import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dir")

args = str(parser.parse_args())
print(args)


file_list = []
file_list = os.listdir(path=".")
print(file_list)

for name in os.listdir(args):
    if os.path.isfile(name):
        print(f"file:{name}")
    else:
        print(f"dir:{name}")



with open("test.json" , "r") as f:
    for x in f:
        file_list = x
        #print(file_list)