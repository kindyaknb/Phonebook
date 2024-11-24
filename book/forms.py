from django import forms
from .models import Contact, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']  # Поля, які будуть доступні у формі
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Напишіть ваш відгук тут...',
                'class': 'form-control',
                'rows': 4,
            }),
        }
