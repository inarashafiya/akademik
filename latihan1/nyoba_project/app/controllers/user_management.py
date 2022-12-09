from flask import request
from app import validators
from http import HTTPStatus
from app import responses

def Register():
    bodyJson = request.json 
    err = validators.Register(bodyJson)
    if err:
        return responses.Make(
            Status=HTTPStatus.BAD_REQUEST.value,
            Message="error",
            Data=str(err)
        ), HTTPStatus.BAD_REQUEST.value
        
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="succes",
        Data={}
    ), HTTPStatus.OK.value