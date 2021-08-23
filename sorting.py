import sys

from os import listdir
from os import makedirs


# directory list
lsdir = listdir(".")

# creating folder if it doesn't exist
def create_folder(folder_name=None):
    if folder_name not in lsdir:
        makedirs(folder_name)

# check if the file is video
def is_video(file=None):
    if file.endswith(".MOV") or file.endswith(".mov"):
        print()

# our main bro
def main():
    print(type(lsdir))
    print("------------")
    for file in range(len(lsdir)):
        print(type(file))
 

main()
