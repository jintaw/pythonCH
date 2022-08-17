import sys
import glob
import os
import json
import datetime
import shutil

IMAGE_MOVE_FRAG = "cp" # cp , mv 
SERCH_CLASS = "eiso4" # 好きなタグカテゴリ入力。完全一致。
serch_dir = sys.argv[1]


now =  datetime.datetime.now()
dt = now.strftime("%Y%m%d-%H%M%S")
RESULT_DIR = "tagClassif_" + dt


# 1. json のリスト作成
json_paths = []
json_paths = glob.glob(os.path.join(serch_dir, "*.json"))
print(json_paths)
print(f'[DEBUG] len(json_paths): {len(json_paths)}')

#　２．jsonの中身のクラス確認

copy_file_lists = []

for json_path in json_paths:
    print(json_path)
    with open(json_path , "r") as f:
        json_data = json.load(f)
        basename = os.path.basename(json_path)
        splitext = os.path.splitext(basename)[0]
        
        for json_class_only in json_data["detection"]:
            print(json_class_only["class"])
            if json_class_only["class"] == SERCH_CLASS:
                if json_path in copy_file_lists:
                    continue
                else:
                    copy_file_lists.append(json_path)

print(copy_file_lists)
print(len(copy_file_lists))

os.makedirs(RESULT_DIR)
for copy_file in copy_file_lists:
    shutil.copy(copy_file , RESULT_DIR)
