from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.Profile, name='profile'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('logout/', views.UserLogout, name='logout'),
    path('buy_car/<int:id>/', views.buy_car, name='buy_car'),
]
