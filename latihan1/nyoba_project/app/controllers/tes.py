# from distutils.log import error
# from flask import request
# from flask import jsonify
# from app import validators
# from app import responses
# from http import HTTPStatus
# from app import models

# def index():
#     data = [
#         {
#         "id" : 1,
#         "name" : "adi"
#         },
#         {
#             "id" : 2,
#             "name" : "andi"
#         }
#     ]   
#     return jsonify(data)

# def create():
#     bodyJson = request.json
#     err = validators.tes(bodyJson) 
#     if err:
#         return responses.Make(
#             Status=HTTPStatus.BAD_REQUEST.value,
#             Message="error",
#             Data=str(err)   
#         ), HTTPStatus.BAD_REQUEST.value
    
#     collUser = models.User(userName=bodyJson["userName"], userPassword=bodyJson["userPassword"])
#     collUser.save() 
    
#     return responses.Make(
#             Status=HTTPStatus.OK.value,
#             Message="succes",
#             Data={}   
#         ), HTTPStatus.OK.value