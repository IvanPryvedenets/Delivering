from django.forms import forms
from django import forms

from .models import *


class CheckoutForm(forms.ModelForm):

    TRANSPORTER = (
        ('Нова пошта', 'Нова пошта'),
    )

    AREA = (
        ('Вінницька', 'Вінницька'),
        ('Волинська', 'Волинська'),
        ('Дніпропетровська', 'Дніпропетровська'),
        ('Донецька', 'Донецька'),
        ('Житомирська', 'Житомирська'),
        ('Закарпатська', 'Закарпатська'),
        ('Запорізька', 'Запорізька'),
        ('Івано-Франківська', 'Івано-Франківська'),
        ('Київська', 'Київська'),
        ('Кіровоградська', 'Кіровоградська'),
        ('Луганська', 'Луганська'),
        ('Львівська', 'Львівська'),
        ('Миколаївська', 'Миколаївська'),
        ('Одеська', 'Одеська'),
        ('Полтавська', 'Полтавська'),
        ('Рівненська', 'Рівненська'),
        ('Сумська', 'Сумська'),
        ('Тернопільська', 'Тернопільська'),
        ('Харківська', 'Харківська'),
        ('Херсонська', 'Херсонська'),
        ('Хмельницька', 'Хмельницька'),
        ('Черкаська', 'Черкаська'),
        ('Чернівецька', 'Чернівецька'),
        ('Чернігівська', 'Чернігівська'),
    )

    class Meta:

        model = Order

        fields = ['name', 'last_name', 'sure_name', 'telephone', 'email', 'transporter', 'area', 'city', 'department', 'wish']

    name = forms.CharField(max_length=50, required=True, label="Ім'я")
    last_name = forms.CharField(max_length=50, required=True, label="Прізвище")
    sure_name = forms.CharField(max_length=50, required=True, label="По батькові")
    telephone = forms.CharField(max_length=17, min_length=17, required=True, label="Телефон")
    email = forms.EmailField(max_length=50, required=True, label="Email")
    transporter = forms.ChoiceField(choices=TRANSPORTER, label="Доставка")
    area = forms.ChoiceField(choices=AREA, label="Область")
    city = forms.CharField(max_length=20, label="Місто")
    department = forms.CharField(max_length=40, label="Відділення")
    wish = forms.CharField(widget=forms.Textarea, max_length=500, required=False, label="Побажання")

    name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    sure_name.widget.attrs.update({'class': 'form-control'})
    telephone.widget.attrs.update({'class': 'form-control', 'data-mask': '+38(000)000-00-00'})
    email.widget.attrs.update({'class': 'form-control'})
    transporter.widget.attrs.update({'class': 'form-control'})
    area.widget.attrs.update({'class': 'form-control'})
    city.widget.attrs.update({'class': 'form-control'})
    department.widget.attrs.update({'class': 'form-control'})
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

