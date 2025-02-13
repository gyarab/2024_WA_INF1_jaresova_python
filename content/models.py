from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Game (models.Model):
    name=models.CharField(max_length=50)
    made_by=models.ManyToManyField(Category, related_name='companies')
    came_out_on=models.DateTimeField() 
    rating=models.FloatField()
    about=models.TextField()
    def __str__(self):
        return self.name

