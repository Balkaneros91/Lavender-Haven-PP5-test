from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    # featured_image = CloudinaryField('image', default='placeholder')

    image = models.ImageField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    # def __str__(self):
    #     return self.title

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def number_of_likes(self):
        return self.likes.count()
