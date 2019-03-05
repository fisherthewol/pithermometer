import datetime
import os
import peewee


db = peewee.SqliteDatabase(os.environ.get("database"),
                           pragmas={"journal_mode": "wal"})


class BaseModel(peewee.Model):
    """Base model."""
    class Meta:
        database = db


class Reading(BaseModel):
    """A reading of <temperature> from sensor <sensor>."""
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
    sensor = peewee.FixedCharField(max_length=15)
    temperature = peewee.FloatField()
