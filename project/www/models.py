from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='images')    
    discription = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Trip(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discription = models.CharField(max_length=100, default='')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now=False, auto_now_add=True)
   
     
    def __str__(self):
        return self.name 


class Favorite(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)