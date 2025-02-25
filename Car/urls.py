from django.urls import path
from . import views
urlpatterns = [
    path('detail/<int:id>/', views.CarDetaillView.as_view(), name='car_details')
]
