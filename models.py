from peewee import PostgresqlDatabase, Model, AutoField, CharField, IntegerField
import os
# import private

database = PostgresqlDatabase(
    os.getenv(DATABASE),
    os.getenv(USER),
    os.getenv(PASSWORD),
    os.getenv(HOST),
    os.getenv(PORT)
    # database=private.DATABASE,
    # user=private.USER,
    # password=private.PASSWORD,
    # host=private.HOST,
    # port=private.PORT,
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

