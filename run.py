
"""Upload item descriptions to web server"""

#! /usr/bin/env python3
import os
import requests
source_folder = r"/home/student-03-62cae6f335dc/supplier-data/descriptions"
filelist = []
textdictionary = {}

#Append all files in the source folder to a list
for file in os.listdir(source_folder):
    filelist.append(file)

#Iterate through each file in the list create a dictionary and upload to the webservice using post
for filename in filelist:
    if filename != ".DS_Store":
        with open(source_folder+"/"+filename, "r") as tx:
            count = 0
            for line in tx.readlines():
                if count == 0:
                    textdictionary["name"] = line.strip("\n")
                elif count == 1:
                    we = line.strip("\n")
                    textdictionary["weight"] = int(we.strip("lbs"))
                elif count == 2:
                    textdictionary["description"] = line.strip("\n")
                count += 1
            textdictionary["image_name"] = filename.strip("txt")+"jpeg"
            print(textdictionary)
            response = requests.post("http://104.197.87.235/fruits/", data=textdictionary)
            print(response.status_code)
            print(response.text)
            if response.status_code == 201:
             print("success")

