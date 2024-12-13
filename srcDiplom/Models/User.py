from srcDiplom.Models.Base import *
from srcDiplom.Models.Role import Roles


class Users(Base):
    id = PrimaryKeyField()
    fullname = CharField(max_length=50)
    login = CharField(unique=True, max_length=50)
    password = CharField()
    role_id = ForeignKeyField(Roles)