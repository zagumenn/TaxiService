from srcDiplom.Models.Base import *

class Cars(Base):
    id = PrimaryKeyField()
    brand = CharField()
    model = CharField()
    color = CharField()
    state_number = CharField()