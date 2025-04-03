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
    art=models.ImageField(upload_to='art', null=True, blank=True)
    
    about=models.TextField()
    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    game = models.ForeignKey(Game,related_name='comments', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, null=True)
    ip = models.GenericIPAddressField(default=None, null=True)
    user_agent = models.CharField(max_length=200, default=None, null=True)


    def __str__(self):
        return self.name