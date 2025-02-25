from django.db import models
from Brand.models import BrandModel
# Create your models here.


class CarModel(models.Model):
    image = models.ImageField(upload_to='car_images/')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='cars')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand.name} - {self.name}"


class Comment(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented by {self.name}"