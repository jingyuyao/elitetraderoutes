__author__ = 'jingyu'

from uuid import uuid4
from django.db import models

class UUIDModel(models.Model):
    # Heavily used in css as a unique id referring to the object
    uuid = models.UUIDField(auto_created=uuid4, default=uuid4)

    class Meta:
        abstract = True
