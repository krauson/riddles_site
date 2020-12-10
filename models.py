from enum import unique
from peewee import *


database = SqliteDatabase('users.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    user_id = AutoField(null=True)
    username = CharField(null=True, unique=True)
    password = CharField(null=True)
    points = IntegerField(null=True)
    
    

    class Meta:
        table_name = 'users'

