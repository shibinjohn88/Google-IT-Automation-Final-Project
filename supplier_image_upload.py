
"""Upload Image to the web server"""

#!/usr/bin/env python3
import requests
import os
import re
in_directory = r"/home/student-03-62cae6f335dc/supplier-data/images"
url = "http://localhost/upload/"
filelist = []
#iterate through source folder and append file names to a list
for filename in os.listdir(in_directory):
    filelist.append(filename)

#Iterate through file names in the list to upload to web server
for file in filelist:
#Check the file is jpeg
    if re.search(r".jpeg",file) is not None:
        with open(in_directory+"/"+file, 'rb') as f:
        r = requests.post(url, files={'file': f})


