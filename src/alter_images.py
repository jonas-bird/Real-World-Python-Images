!/usr/bin/env python3

# Solution to Google's IT Automation with Python: Automating Real World Tasks With Python: Week 1 Lab
# Jonas Bird
# 2021-12-23

from pathlib import Path
from PIL import Image


def manipulate_images(fileNames, destinationPath):
    """
    function that recieves a list of files, rotates and resizes them,
    and saves them as .jpeg
    """
    size = (128, 128)
    newFiles = []
    for filename in fileNames:
        try:
            newFileName = Path(filename).stem + '.jpeg'
            newFileName = Path(destinationPath) / newFileName
            with Image.open(filename) as im:
                im = im.convert("RGB")
                im.thumbnail(size)
                im = im.rotate(270, expand=True)
                im.save(newFileName, "JPEG")
        except Exception:
            pass

        newFiles.append(newFileName)
    return newFiles


if __name__ == "__main__":
    fileNames = []
    path = Path(
        '/home/student-04-3cd8df6fa80a/images/')
    # must be full path unless I add expand home
    destinationPath = '/opt/icons/'
    # I had originally assumed that the files would have a .tiff extension and would be globbing them that way
    for fNames in path.glob('*'):
        fileNames.append(fNames)

    newNames = manipulate_images(fileNames, destinationPath)
    print("New thumbnails saved as: ")
    for n in newNames:
        print(n)
