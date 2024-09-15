from decouple import config
from peewee import *

db_config = {
  'user': config('DB_USER'),
  'password': config('DB_PWD'),
  'host': config('DB_HOST'),
  'database': config('DB')
}

db = MySQLDatabase(**db_config)

class BaseModel(Model):
  class Meta:
    database = db
    
class User(BaseModel):
  id = BigAutoField(unique=True)
  username = CharField(null=True)
  first_name = CharField()
  last_name = CharField(null=True)
  created_at = DateTimeField()
  received_discount = BooleanField(null=False)
  
  class Meta:
    table_name = 'User'
  
class Interaction(BaseModel):
  user = ForeignKeyField(User)
  dick_size_result = IntegerField()
  created_at = DateTimeField()
  
  class Meta:
    table_name = 'Interaction'
    

# Create Tables
with db:
  db.create_tables([User, Interaction], safe=True)