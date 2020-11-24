
"""Email pdf report"""

#!/usr/bin/env python3
import os
import datetime
import reports
import emails


source_folder = r"/home/student-03-62cae6f335dc/supplier-data/descriptions"
filelist = []
textdictionary = ""

#Append all files in the source folder to a list
for file in os.listdir(source_folder):
    filelist.append(file)

#Iterate through each file
for filename in filelist:
    if filename != ".DS_Store":
        with open(source_folder+"/"+filename, "r") as tx:
            count = 0
            for line in tx.readlines():
                if count == 0:
                    textdictionary += "name: "+line.replace("\n","<br/>")
                elif count == 1:
                    textdictionary += "weight: "+line.replace("\n","<br/>")
                elif count == 2:
                    textdictionary += "<br/>"
                count += 1
x = datetime.date.today()
title = "Processed Update on "+x.strftime("%b, %d %Y")
reports.generate("/tmp/processed.pdf", title, textdictionary)
#print(textdictionary)
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
emails.send_email(message)


