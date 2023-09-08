from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SkyCard
from django import forms
from django.forms import ModelForm


class RegistorUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CreateCardForm(ModelForm):
    class Meta:
        model = SkyCard
        fields = ['profile_image', 'business_logo',
                  'name', 'position', 'number', 'whats_app_number',
                  'email', 'insta', 'twitter', 'facebook', 'youtube',
                  'business_name', 'gst_number', 'stablish_year', 'website',
                  'tagline', 'tag', 'business_description', 'state', 'city', 'country',
                  'pincode', 'address'
                  ]
