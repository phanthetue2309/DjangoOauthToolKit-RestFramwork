from django.db import models
import uuid


class Instrument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
