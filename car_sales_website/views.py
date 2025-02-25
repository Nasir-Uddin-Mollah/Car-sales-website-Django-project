from django.shortcuts import render
from Car.models import CarModel
from Brand.models import BrandModel


def home(request, slug=None):
    cars = CarModel.objects.all()
    if slug is not None:
        brand = BrandModel.objects.get(slug=slug)
        cars = CarModel.objects.filter(brand=brand)
    brands = BrandModel.objects.all()

    return render(request, 'home.html', {'brands': brands, 'cars': cars})
