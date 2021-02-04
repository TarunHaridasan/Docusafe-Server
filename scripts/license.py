import json
import secrets
import time
from datetime import datetime

#JSON reader
def read():
    with open("data//licenseKey.json") as f:
        data = json.load(f)
    return data

#JSON Writer
def write(data):
    with open("data//licenseKey.json", "w") as f:
        json.dump(data, f, indent=4)

#Check if a license key is valid and has been issued by owner
def validate(licenseKey):
    data = read()
    if licenseKey in data:
        return True
    else:
        return False

#Retrieve the document connected to the license Key (REMOVE)
def retrive(licenseKey):
    data = read()
    return data[licenseKey]

#Issue a license key
def issue(documentName, fp, key):
    data = read()
    data[key]={
        "name": documentName,
        "fp": fp,
        "redeemed": False,
    }
    write(data)
    return key

#Cancel a license key
def cancel(key):
    data=read()
    del data[key]
    write(data)

#Check if a license key has been redeemed
def redeemed(key):
    data = retrive(key)
    return data["redeemed"]

#This function will redeem a key and place the pdf in the user's account
def redeem(fingerprint, key): 
    data = read()
    data[key]["redeemed"]=True
    data[key]["fingerprint"]=fingerprint
    data[key]["time"]=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    write(data)    
    return retrive(key)



