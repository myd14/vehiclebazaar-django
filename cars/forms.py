from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Car, Message


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'brand',
            'title',
            'model',
            'vehicle_type',
            'year',
            'price',
            'mileage',
            'fuel_type',
            'transmission',
            'color',
            'seller_phone',
            'description',
            'image',
        ]


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'content']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your message'}),
        }