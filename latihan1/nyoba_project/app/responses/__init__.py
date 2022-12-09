from flask import jsonify

def Make(Status, Message, Data):
    data = {
        "status" : Status,
        "Message" : Data
    }
    return data