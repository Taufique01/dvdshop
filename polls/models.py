from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Catagory(models.Model):
    
    catagory = models.CharField('Catagory',max_length=100,primary_key=True)
    def __str__(self):
        return self.catagory

class Movie(models.Model):
    
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='Movie_catagory')
    description=models.TextField()
    title=models.CharField(max_length=200)
    actors=models.CharField(max_length=200)
    director=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    sub_language=models.CharField(max_length=50)
    year=models.CharField(max_length=6)
    image = models.ImageField(upload_to='posters')
    price=models.FloatField(default=0)

    def __str__(self):
        return self.title


class Basket(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='basket_user')
    #movies = models.ManyToManyField(Movie,null=True)
    total=models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class BasketDetails(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_details')

    movie= models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='basket_movie')
    quantity=models.FloatField(default=0)

    def __str__(self):
        return str(self.basket.id)







