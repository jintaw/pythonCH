import os
import argparse
import sys 



parser = argparse.ArgumentParser()
parser.add_argument("-d" , "--first" ,required=True , help="dir")


args = parser.parse_args()
print(args)
args = str(args)


if os.path.isdir(args):
    print("引数１:" + args.first)
else:
    print("dir enter")

