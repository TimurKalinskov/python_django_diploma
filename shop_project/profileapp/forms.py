from django import forms
from django.core.validators import RegexValidator

from .models import User


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    full_name = forms.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = forms.CharField(max_length=17, validators=[phone_regex])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control-file'}))
    password = forms.CharField(max_length=1000)

    class Meta:
        model = User
        fields = ['avatar', 'full_name', 'phone_number', 'email', 'password']
