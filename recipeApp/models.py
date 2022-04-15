from django.db import models

# Create your models here.

class Recipes(models.Model):
    title = models.CharField(max_length=150)
    img=models.ImageField(upload_to="recipe_images")
    desc= models.TextField()
    cookTime=models.IntegerField()
    ingredients=models.TextField()
    author=models.CharField(max_length=100)
    date = models.DateField()