
"""Convert Image from TIFF to JPEG, resize image to 600, 400 pixels"""

#!/usr/bin/env python3
from PIL import Image
import os
in_directory = r"/home/student-02-e6ae0def6e97/supplier-data/images"
filelist = []
#iterate through source folder and append file names to a list
for filename in os.listdir(in_directory):
    filelist.append(filename)

#Iterate through file names in the list to scale and convert image to JPEG
for file in filelist:
    if file != ".DS_Store":
     with Image.open(in_directory+"/"+file) as im:
        if im.mode != 'RGB':
         im = im.convert('RGB')
        im = im.resize((600, 400))
        im.save(in_directory+"/"+os.path.splitext(file)[0]+".jpeg")
