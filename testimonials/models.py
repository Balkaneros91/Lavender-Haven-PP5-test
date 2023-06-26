from django.db import models
import uuid


class Review(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    review = models.TextField(max_length=1000, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']
