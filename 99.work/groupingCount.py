import glob
import os

FILE_COUNT_DIR = "grouping"
TARGET = "zoom"  # all , zoom 

# 1. search grouping folder
grouping_dirs = glob.glob("./**/"+ FILE_COUNT_DIR , recursive = True )

for grouping_dir in grouping_dirs:
    grouping_files = os.path.basename(grouping_dir)
    
    if TARGET == "all":
        grouping_files = glob.glob(grouping_dir + "/*")
        print(grouping_dir + ":全ファイルをカウント -> " + str(len(grouping_files)))
            
    elif TARGET == "zoom":
        grouping_files = glob.glob(grouping_dir + "/*zoom*")
        print(grouping_dir + ":zoom画像のみカウント -> " + str(len(grouping_files)))
