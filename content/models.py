from django.db import models

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'authors'

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    stars=models.FloatField(max_length=2)

    def __str__(self):
        return str(self.stars)    

class Game (models.Model):
    name=models.CharField(max_length=50)
    author=models.ManyToManyField(Author, related_name='games')
    came_out_on=models.DateField() 
    rating=models.ForeignKey(Rating, on_delete=models.CASCADE, related_name='games')
    
    about=models.TextField()
    def __str__(self):
        return self.name

