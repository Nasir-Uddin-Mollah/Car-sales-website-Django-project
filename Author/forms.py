from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Password", 
        help_text=""
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Confirm Password", 
        help_text=""
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': None
        }


class ProfileEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']