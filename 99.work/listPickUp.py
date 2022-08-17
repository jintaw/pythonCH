from copy import copy
from importlib.resources import path
import os
from posixpath import splitext
import sys
import glob
import datetime
import shutil

FLAG_COPY = False
FLAG_MOVE = True

# 1. list get
file_lists_txt_path = sys.argv[1]
with open(file_lists_txt_path , "r" , encoding="utf-8") as f:
    file_lists = [s.strip() for s in f.readlines()]
print(file_lists)

# 2. serch file path 
file_paths = []
for filename in file_lists:
    for file_path in glob.glob("./**/" + filename , recursive=True ):
        file_paths.append(file_path)

# 3. copy
now = datetime.datetime.now()
timestamp = now.strftime('%Y-%m-%d-%H-%M-%S')
result_path = "ListPickUp_" + timestamp

os.makedirs(result_path)

for file_path in file_paths:
    print(str(file_path))
    if FLAG_COPY:
        shutil.copy(file_path , result_path)
    
    if FLAG_MOVE:
        shutil.move(file_path , result_path)

