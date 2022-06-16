from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

    
    def __str__(self):
        return self.title