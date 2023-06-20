from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db import models
import uuid


class Testimonial(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    review = models.TextField(max_length=1000, blank=False, null=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(f"New review from {self.name}")


STATUS = ((0, "Draft"), (1, "Published"))


class Testimonials(models.Model):
    """Testimonials model"""

    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonial")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Testimonials, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Testimonials'
        """Sorts testimonials in descending order"""
        ordering = ["-created"]

    def __str__(self):
        return self.title
