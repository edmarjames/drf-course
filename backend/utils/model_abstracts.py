import uuid
from django.db import models

# The Model class defines a single field id of type UUIDField, which is used as the primary key for the model.
class Model(models.Model):
    # The primary_key=True argument specifies that the id field should be the primary key for the model, which means that it will be used to uniquely identify each record in the model's database table.

    # The default=uuid.uuid4 argument specifies that a new UUID value should be generated automatically for each new record in the table, using the uuid.uuid4() function from the uuid module.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # This attribute tells Django that this is an abstract base class that should not be instantiated directly, but instead should be subclassed by other model classes that inherit its fields and methods.
    class Meta:
        abstract = True