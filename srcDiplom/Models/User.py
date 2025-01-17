from srcDiplom.Models.Base import *
from srcDiplom.Models.Gender import Genders
from srcDiplom.Models.Role import Roles


class Users(Base):
    id = PrimaryKeyField()
    fullname = CharField(max_length=50)
    login = CharField(unique=True, max_length=50)
    phone = CharField(max_length=11)
    gender_id = ForeignKeyField(Genders)
    password = CharField()
    role_id = ForeignKeyField(Roles)