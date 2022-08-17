import os
from posixpath import splitext
import sys
import glob
import datetime
import shutil

json_lists = []
file_lists = []
pair_lists = []

target_dir = sys.argv[1]
#print(target_dir)
target_all_files = []
target_all_files = os.listdir(target_dir)
#print(target_all_files)

# jsonのファイル名リストを取得
os.chdir(target_dir)
json_lists = glob.glob(os.path.join('*json'))
#print(json_lists)
print("---")

#　拡張子削除
for json_list in json_lists:
    basename = os.path.basename(json_list)
    splitext = os.path.splitext(basename)[0] 
  
    # 画像ファイルと突合。あればpair_listsに追加
    if splitext +".JPG" in target_all_files:
        pair_lists.append(splitext+".JPG")
        pair_lists.append(basename)
    elif splitext +".jpg" in target_all_files:
        pair_lists.append(splitext+".jpg")
        pair_lists.append(basename)
    elif splitext +".png" in target_all_files:
        pair_lists.append(splitext+".png")
        pair_lists.append(basename)
    elif splitext +".PNG" in target_all_files:
        pair_lists.append(splitext+".PNG")
        pair_lists.append(basename)
    else:
        print("False:" + splitext)
        continue

print("---check---")
print(pair_lists)
print("Check count : " + str(len(pair_lists)))
print("-----------")

now = datetime.datetime.now()
new_dir_path="pairCopyResult_" + now.strftime("%Y-%m-%d-%H-%M")
os.makedirs(new_dir_path)

for copy_file in pair_lists:
    shutil.copy(copy_file,new_dir_path)
