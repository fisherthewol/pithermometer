import datetime
import peewee

db = peewee.PostgresqlDatabase(None)


class BaseModel(peewee.Model):
    """Base model to use our PostgreSQL Database."""
    class Meta:
        database = db


class Reading(BaseModel):
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    sensor = peewee.FixedCharField(max_length=15)
    temperature = peewee.FloatField()
