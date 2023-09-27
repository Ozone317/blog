from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

# Posts, Author, Tag

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True, db_index=True)
    tags = models.ManyToManyField(Tag)