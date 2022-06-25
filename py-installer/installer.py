import time
import os
import requests
import math
import shutil

##SETTINGS##
vertion = "1.0.0"
auther = "Mr. GIitch"
directory = "GameHub"
standartFolder = "C:/Program Files (x86)/"
os.system('TITLE Quiz version ' + vertion) #Renames the windown titel

##FUNTIONS##
def locationfordownload(location):
    if location == "":
        locationfordownload == print("Downloading to " + standartFolder)
    elif location != "":
        locationfordownload == print("Downloading to " + location)

def progress_bar(progress, total):
    precent = 100 * (progress / float(total))
    bar = '█' * int(precent) + '-' * (100 - int(precent))
    print(f"\r|{bar}| {precent:.2f}%", end="\r")


print("Default folder is " + standartFolder)
print("Press enter to select Default folder")
location = input("Paste the path of the installation folder: ")
locationfordownload(location)

installation = requests.get("http://localhost/installer/vertion.txt")
print(installation)
time.sleep(2)
