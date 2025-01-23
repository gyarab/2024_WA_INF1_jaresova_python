from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    perex = models.TextField(max_length=200)
    text = models.TextField()
    published = models.DateTimeField()

    def __str__(self):
        return self.title