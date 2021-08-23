import sys

from os import listdir
from os import makedirs

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
def create_folder(folder_name=None):
    if folder_name not in lsdir:
        makedirs(folder_name)

# our main bro
def main():
    if len(sys.argv) > 2:
        print("Too much arguments, taking only the first...")
        print(sys.argv[1])
        # directory list
        lsdir = listdir(sys.argv[1])
    else:
        print("Taking this one...")
        print(sys.argv[1])
        # directory list
        lsdir = listdir(sys.argv[1])

    video_photo = VideoPhoto()

    for file in range(len(lsdir)):
        if video_photo.is_video(lsdir[file]):
            print(file, lsdir[file] , "VIDEO")

        if video_photo.is_photo(lsdir[file]):
            print(file, lsdir[file] , "PHOTO")

main()
