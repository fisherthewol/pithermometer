import datetime
import os
import peewee


db = peewee.SqliteDatabase(os.environ.get("database"),
                           pragmas={"journal_mode": "wal"})


class BaseModel(peewee.Model):
    """Base model."""
    class Meta:
        database = db


class Sensor(BaseModel):
    """Representation of a sensor."""
    serial = peewee.FixedCharField(max_length=15)
    name = peewee.CharField()
    connected = peewee.BooleanField()


class Reading(BaseModel):
    """A reading of <temperature> from sensor <sensor>."""
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    sensor = peewee.FixedCharField(max_length=15)
    temperature = peewee.FloatField()


# Create tables (passes silently if already exists.)
with db:
    db.create_tables([Reading])
