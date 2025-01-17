from srcDiplom.Models.Base import *
from srcDiplom.Models.Car import Cars
from srcDiplom.Models.Statuses import Statuses
from srcDiplom.Models.User import Users


class Orders(Base):
    id = PrimaryKeyField()
    driver_id = ForeignKeyField(Users)
    user_id = ForeignKeyField(Users)
    data = DateField()
    price = IntegerField()
    status_id = ForeignKeyField(Statuses)
    starting_place = CharField()
    car_id = ForeignKeyField(Cars)
    end_place = CharField()