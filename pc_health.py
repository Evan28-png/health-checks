#!/usr/bin/env python3
import psutil
import shutil
import smtplib
import datetime

#Function to check CPU status
def check_cpu():
    check = psutil.cpu_percent(interval=.1)
    return check < 2


#Function to check storage
def check_storage():
    storage = shutil.disk_usage("/")
    per_storage = storage.used / storage.total * 100
    return per_storage < 70


if check_cpu() and check_storage():
    pass
else:
    #Sending email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail:
            mail.login('email', 'password')
            msg = "Computer health risk"
            mail.sendmail('email', 'email', msg)


