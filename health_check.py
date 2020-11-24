

"""Check system health and send email alert"""

#!/usr/bin/env python3
import psutil
import shutil
import socket
import email.message
import smtplib

Error=""
total, used, free = shutil.disk_usage("/")
disk_free = (free/total)*100
if psutil.cpu_percent() > 80:
    Error = "Error - CPU usage is over 80%"
elif psutil.virtual_memory().available < 500*1000000:
    Error = "Error - Available memory is less than 500MB"
elif disk_free < 20:
    Error = "Error - Available disk space is less than 20%"
elif socket.gethostbyname("localhost") != "127.0.0.1":
    Error = "Error - localhost cannot be resolved to 127.0.0.1"
#print(Error)


message = email.message.EmailMessage()
message["From"] = "automation@example.com"
message["To"] = "student-03-62cae6f335dc@example.com"
message["Subject"] = Error
message.set_content("Plase check your system and resolve the issue as soon as possible")

"""Sends the message to the configured SMTP server."""
mail_server = smtplib.SMTP('localhost')
mail_server.send_message(message)
mail_server.quit()
