#Imports
from flask import Flask, send_file, request
from flask_cors import CORS
from scripts import license, user

#Initialize server
app = Flask(__name__)
CORS(app)

#Routes
@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/retrieveData/<fingerprint>')
def retrieveData(fingerprint):
    #Make sure user exists
    if not user.exists(fingerprint): 
        ip = request.remote_addr
        user.add(fingerprint, ip)
        return {
            "documents":[]   
        }
    #Return the data
    return {
        "documents":user.documents(fingerprint)   
    }

@app.route('/redeemKey/<fingerprint>/<key>')
def redeemKey(fingerprint, key):
    #Make sure user exists
    if not user.exists(fingerprint): 
        return {
            "status": 404,
            "message": "This user does not exist"
        }
    #Make sure the key exists
    if not license.validate(key):
        return {
            "status": 404,
            "message": "This key does not exist"
        }
    #Make sure the key has not been redeemed
    if license.redeemed(key):
        return {
            "status": 404,
            "message": "This key has already been redeemed"
        }
    #All checks are succesful
    data = license.redeem(fingerprint, key)
    user.addDoc(fingerprint, data["name"], data["fp"], data["time"])
    return {
        "status": 200,
        "message": "This key has succesfully been redeemed"
    }

@app.route("/retrieveDocument/<fingerprint>/<documentName>")
def retrieveDocument(fingerprint, documentName):
    #Make sure user exists
    if not user.exists(fingerprint): 
        return {
            "status": 404,
            "message": "This user does not exist"
        }
    documents = user.documents(fingerprint)
    for document in documents:
        if documentName!=document["name"]:
            continue
        return send_file(document["fp"])
    return {
        "status": 400,
        "message": "This document does not exist under you ownership"
    }

#Function to start server
def start(): 
    #print("THIS WORKS")   
    app.run()
    

