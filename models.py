from peewee import PostgresqlDatabase, Model


db = PostgresqlDatabase("test", user="test")


class BaseModel(Model):
    """Base model to use our PostgreSQL Database."""
    class Meta:
        database = db
