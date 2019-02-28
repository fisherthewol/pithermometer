import datetime
import os
import peewee


db = peewee.PostgresqlDatabase(os.environ.get("database"),
                               user=os.environ.get("db_user"),
                               password=os.environ.get("db_passwd"))


class BaseModel(peewee.Model):
    """Base model to use our PostgreSQL Database."""
    class Meta:
        database = db


class Reading(BaseModel):
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    sensor = peewee.FixedCharField(max_length=15)
    temperature = peewee.FloatField()
