from srcDiplom.Connect.connection import *

class Base(Model):
    class Meta:
        database = connect_db()