from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    perex = models.TextField(max_length=200)
    text = models.TextField()
    published = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title