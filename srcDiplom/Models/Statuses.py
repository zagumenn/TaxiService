from srcDiplom.Models.Base import *


class Statuses(Base):
    id = PrimaryKeyField
    status = CharField(max_length=50)
