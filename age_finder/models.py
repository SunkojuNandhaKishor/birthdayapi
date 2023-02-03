import uuid
from django.db import models

class AgeRequest(models.Model):
    request_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    dob = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    request_count = models.IntegerField(default=0)