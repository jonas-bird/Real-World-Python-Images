#!/usr/bin/env python3
"""
Code for Week 1 lab for Automating Real World tasks module from
Google's IT Automation with Python

Jonas Bird
2021-12-20
"""

from pathlib import Path
from PIL import Image


def manipulate_images(fileNames):
    """function that recieves a list of files and rotates, resizes,
    and saves them in a format, and returns a list of the new filenames"""
    newFiles = []
    for filename in fileNames:
        image = Image.open(filename)
        image.show()
        newFiles.append(str(filename.with_suffix('.jpeg')))
    return newFiles

if __name__ == '__main__':

    alteredFiles = []
    # Prompt the user for a target directory, use a default if input is blank
    userInput = input("Please enter the target directory:")
    if len(userInput) < 1:
        userInput = './images/'
    # Trying out the newer pathlib rather than the os.path and globing
    dirName = Path(userInput)
    targetFiles = list(dirName.glob('*.ppm'))
    alteredFiles = manipulate_images(targetFiles)
    print(', '.join(alteredFiles))
