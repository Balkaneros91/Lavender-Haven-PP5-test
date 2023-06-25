from django.db import models
import uuid
import random


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # noqa
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # noqa
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def generate_random_rating(self):
        # Generate a random rating between 0 and 5
        return round(random.uniform(0, 5), 2)

    def save(self, *args, **kwargs):
        if not self.sku:
            # Generate a unique SKU using UUID
            self.sku = str(uuid.uuid4())

        # Save the image URL if it is provided
        if self.image and not self.image_url:
            self.image_url = self.image.url

        if not self.rating:
            # Generate a random rating if it is not provided
            self.rating = self.generate_random_rating()

        super().save(*args, **kwargs)


# class Sculpture(models.Model):
#     id = models.UUIDField(
#         default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     title = models.CharField(max_length=200, unique=True)
#     description = models.CharField(max_length=200)
#     detailed_description = models.TextField(max_length=500)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = CloudinaryField('image', default='placeholder')
#     available = models.BooleanField(default=False)
#     quantity = models.DecimalField(max_digits=3, decimal_places=0, default=0)
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         """
#         Helper function to organize sculptures by newest first
#         """
#         ordering = ['-created_on']

#     def __str__(self):
#         return str(self.title)
