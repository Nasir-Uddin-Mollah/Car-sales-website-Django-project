from django.db import models
from django.contrib.auth.models import User
from Car.models import CarModel
# Create your models here.


class OrderModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(auto_now_add=True)