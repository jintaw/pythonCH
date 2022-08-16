from genericpath import isfile
import os
import sys 



#parser = argparse.ArgumentParser()
#parser.add_argument("-d" , "--first" ,required=True , help="dir")

dir_name = sys.argv[1]
#args = parser.parse_args()
#print(args)
#print(sys.argv)
#args = str(args)

if os.path.isdir(dir_name):
    print("引数１:" + dir_name)
else:
    print("dir enter")

file_list = []
dir_list = []
for x in os.listdir(dir_name):
    if os.path.isfile(x):
        print("file:" +x)
        file_list.append(x)
    else:
        print("dir:" +x)
        dir_list.append(x)

file_list = str(file_list)
dir_list = str(dir_list)


with open("file_list.txt" , "w" , encoding="utf-8") as f:
    f.write(file_list)

with open("dir_list.txt" , "w" , encoding="utf-8") as f:
    f.write(dir_list)


