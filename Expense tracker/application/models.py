from sqlalchemy import Column, Integer, String, DateTime, Float
import datetime
from application import db

class incomexpense(db.Model):
    id = Column("id", Integer, primary_key = True)
    type = Column("type", String(100), nullable = False)
    category = Column("category", String(500), nullable = False)
    date = Column("date", DateTime, default = datetime.datetime.now(), nullable = False)
    amount = Column("amount", Float, nullable = False)

    def __str__(self):
        return self.id