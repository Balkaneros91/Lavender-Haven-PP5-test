from django.db import models
import uuid


class Newsletter(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=500, blank=False, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.email)


# class Subscriber(models.Model):
#     email = models.EmailField(unique=True)
#     date_subscribed = models.DateTimeField(auto_now_add=True)
#     is_subscribed = models.BooleanField(default=True)

#     def __str__(self):
#         return self.email
