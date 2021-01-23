from peewee import (PostgresqlDatabase, Model, AutoField, CharField, IntegerField)
import os


database = PostgresqlDatabase(
    os.getenv('DATABASE_NAME'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    host=os.getenv('HOST'),
    port=os.getenv('MYPORT')
)


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
