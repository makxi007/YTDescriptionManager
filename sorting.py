# sys
import sys
# shutil
from PIL import Image, ExifTags
# shutil
from shutil import move
# os
from os import listdir
from os import makedirs
from os import path
# subprocess
import subprocess

class VideoPhoto:
    # jpeg, jpg, png
    def is_photo(self, file=None):
        file = str(file).lower()
        if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):
            return True
    # mp4, mov
    def is_video(self, file=None):
        file = str(file).lower()
        if file.endswith(".mp4") or file.endswith(".mov"):
            return True

# creating folder if it doesn't exist
def create_folder(folder_name, dir):


    if folder_name not in dir:
        makedirs(dir + "/" + folder_name, exist_ok=True)
    else:
        print("PHOTO/VIDEO in directory")

# creating subprocess and getting metadata
def get_metadata(path_to_file):
    info_metadata = {}
    process = subprocess.Popen(["exiftool", path_to_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for tag in process.stdout:
        line = tag.strip().split(":")
        info_metadata[line[0].strip()] = line[-1].strip()

    for k, v in info_metadata.items():
        print(k, ":", v)

    return info_metadata

# saving metadata to the file
def saving_metadata(file_txt, metadata):
    with open(file_txt, "a") as md:
        for k, v in metadata.items():
            md.write(k + " : " + v + ";\n")

        md.write("*****************\n")

# our main bro
def main():

    metadata_file = "metadata.txt"

    if len(sys.argv) > 2:
        print("Too much arguments, taking only the first...")
        print(sys.argv[1])
        # directory list
        dir_path = sys.argv[1]
        lsdir = listdir(dir_path)
    else:
        print("Taking this one...")
        print(sys.argv[1])
        # directory list
        dir_path = sys.argv[1]
        lsdir = listdir(dir_path)

    video_photo = VideoPhoto()
    create_folder("VIDEO", sys.argv[1])
    create_folder("PHOTO", sys.argv[1])

    for file in range(len(lsdir)):
        # is video
        if video_photo.is_video(lsdir[file]):
            #move(f"{dir_path}/{lsdir[file]}", f"{dir_path}/VIDEO/{lsdir[file]}")
            pass
        # is photo
        if video_photo.is_photo(lsdir[file]):
            metadata = get_metadata(f"{dir_path}/{lsdir[file]}")

            saving_metadata(f"{dir_path}/{metadata_file}", metadata)



            #move(f"{dir_path}/{lsdir[file]}", f"{dir_path}/PHOTO/{lsdir[file]}")




main()
