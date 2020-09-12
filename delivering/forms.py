from django.forms import forms
from django import forms

from .models import *


class CheckoutForm(forms.ModelForm):

    class Meta:

        model = Order

        fields = ['name', 'last_name', 'sure_name', 'telephone', 'email', 'address', 'wish']

    name = forms.CharField(max_length=50, required=True, label="Ім'я")
    last_name = forms.CharField(max_length=50, required=True, label="Прізвище")
    sure_name = forms.CharField(max_length=50, required=True, label="По батькові")
    telephone = forms.CharField(max_length=14, min_length=14, required=True, label="Телефон")
    email = forms.EmailField(max_length=50, required=True, label="Пошта")
    address = forms.CharField(max_length=60, min_length=10, required=True, label="Адреса")
    wish = forms.CharField(widget=forms.Textarea, max_length=500, required=False, label="Побажання")

    name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    sure_name.widget.attrs.update({'class': 'form-control'})
    telephone.widget.attrs.update({'class': 'form-control', 'data-mask': '(000)00-00-000'})
    email.widget.attrs.update({'class': 'form-control'})
    address.widget.attrs.update({'class': 'form-control', 'placeholder': 'вул. Венниченка, 67а'})
    wish.widget.attrs.update({'class': 'form-control', 'rows': 4})


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ['name', 'email', 'text']

    name = forms.CharField(max_length=50, required=True, label="Ім'я")
    email = forms.EmailField(max_length=50, required=True, label="Пошта")
    text = forms.CharField(widget=forms.Textarea, max_length=300, required=True, label="Коментар")

    name.widget.attrs.update({'class': 'form-control', 'placeholder': "Ваше ім'я"})
    email.widget.attrs.update({'class': 'form-control', 'placeholder': "Ваш email"})
    text.widget.attrs.update({'class': 'form-control', 'rows': 4})


class LoginForm(forms.Form):

    name = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    name.widget.attrs.update({'class': 'form-control', 'name': 'name', 'placeholder': 'Name'})
    password.widget.attrs.update({'class': 'form-control', 'name': 'password', 'placeholder': 'Password'})

