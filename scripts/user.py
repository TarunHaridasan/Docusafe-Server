import json

#JSON reader
def read():
    with open("data//fingerprint.json") as f:
        data = json.load(f)
    return data

#JSON Writer
def write(data):
    with open("data//fingerprint.json", "w") as f:
        json.dump(data, f, indent=4)

#Checks if a user fingerprint is in the system
def exists(fingerprint):
    data = read()
    if fingerprint in data:
        return True
    else:
        return False

#Retrieves information under user's fingerprint
def retrieve(fingerprint): 
    data = read()
    return data[fingerprint]

#Retrieve the documents a user has
def documents(fingerprint):
    data = read()
    return data[fingerprint]["documents"]

#Add a user to the system
def add(fingerprint, ip):
    data = read()
    data[fingerprint]={
        "info": {
            "ip": ip,
            "alias": ""
        },
        "documents": []
    }
    write(data)

#Set a fingerprint to an alias
def setAlias(fingerprint, alias):
    data = read()
    data[fingerprint]["info"]["alias"] = alias
    write(data)

#Add ownership of a document to the user
def addDoc(fingerprint, documentName, fp, time):
    data = read()
    data[fingerprint]["documents"].append({"name":documentName, "fp":fp, "time":time})
    write(data)
    return "Success"

#Remove ownership of a document from the user
def removeDoc(fingerprint, documentName):
    data = read()
    i=0
    for document in data[fingerprint]["documents"]:
        if document["name"]==documentName:
            del data[fingerprint]["documents"][i]
            break
        i+=1
    write(data)



