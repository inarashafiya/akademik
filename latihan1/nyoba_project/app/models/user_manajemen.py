from enum import unique
from mongoengine import connect
from mongoengine import *
from datetime import datetime 
from app import configs

connect(alias='db_user_management', db="praxis")

class Roles(Document):
    roleName = StringField(required=True, unique=True)

class Users(Document):
    roleId = ReferenceField() 
    userName = StringField(max_length=25, required=True, unique=True)
    userEmail = EmailField(required=True, unique=True)
    userPassword =  StringField(required=True)
    # userFirstName = StringField(max_length=25)
    # userLastName = StringField(max_length=25)
    # userPhonenumber = StringField(max_length=25, required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    # updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    # updatedBy = ReferenceField("self", null=True)
    # createdBy = ReferenceField("self", null=True)
    """_summary_
    """    # isActive = BooleanField(required=True, default=True)
    # isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'db_user_management'}
    
array = ["DOSEN", "MAHASISWA"]
for d in array:
    coll = Roles(roleName=d)
    coll.save
    