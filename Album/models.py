from django.db import models
from accounts.models import User
import uuid


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
