from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Orders.models import OrderModel
from Car.models import CarModel

# Create your views here.


class SignupView(CreateView):
    model = User
    form_class = forms.SignupForm
    template_name = 'author/signup.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Signup'
        return context


class UserLoginView(LoginView):
    template_name = 'author/signup.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Login Information Incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context


@login_required
def Profile(request):
    cars = OrderModel.objects.filter(author=request.user)
    return render(request, 'author/profile.html', {'cars': cars})


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch')
class EditProfileView(UpdateView):
    model = User
    form_class = forms.ProfileEditForm
    template_name = 'author/signup.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Error Updating Profile')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Edit Profile'
        return context


def UserLogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')


def buy_car(request, id):
    car = CarModel.objects.get(pk=id)
    if car.quantity > 0:
        car.quantity -= 1
        messages.success(request, 'Congratulations! You bought the car')
        car.save()
        OrderModel.objects.create(author=request.user, car=car)
    else:
        messages.warning(request, 'Sorry, this car is not available')
    return redirect('profile')
