from django.views import View
from django.http import JsonResponse

from django.shortcuts import render
from django.shortcuts import redirect
from django.template.loader import render_to_string

from engine.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login

import json
import datetime

import uuid

from django.utils import timezone


from .models import *
from .forms import *


class MainPage(View):
    def get(self, request):

        products = Product.objects.all()
        categories = Category.objects.all()

        return render(request, 'delivering/main.html', context={'products': products, 'categories': categories})


class CategoryPage(View):
    def get(self, request, slug):

        category = Category.objects.get(slug__iexact=slug)
        products = Product.objects.filter(category=category)

        return render(request, 'delivering/category.html', context={'products': products, 'category': category})


class ProductPage(View):
    def get(self, request, slug):

        product = Product.objects.get(slug__iexact=slug)
        form = CommentForm
        comments = Comment.objects.filter(product=product)

        return render(request, 'delivering/product.html', context={'product': product, 'form': form, 'comments': comments})

    def post(self, request, slug):

        session_key = request.session.session_key

        form = CommentForm(request.POST)

        product = Product.objects.get(slug__iexact=slug)

        comment = Comment.objects.filter(session=session_key).order_by('-id')

        if len(comment) > 0:
            time = comment[0].data + datetime.timedelta(minutes=30)
            now = timezone.now()
            if time > now:
                return redirect('/comment_timerpage/')

        if form.is_valid():
            comment = Comment.objects.create(
                session=session_key,
                product=product,
                mark=int(request.POST['mark']),
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
                data=datetime.datetime.now(),
            )

        form = CommentForm

        comments = Comment.objects.filter(product=product)

        info_message = 'Ваш відгук проходить перевірку'

        return render(request, 'delivering/product.html', context={'product': product, 'form': form, 'comments': comments, 'info_message': info_message})


def comment_sec(request):
    return render(request, 'delivering/comment_sec.html')


class BasketPage(View):
    def get(self, request):

        session_key = request.session.session_key

        products = SelectedProduct.objects.filter(session=session_key).order_by('id')

        return render(request, 'delivering/basket.html', context={'products': products})


class CheckoutPage(View):
    def get(self, request):

        session_key = request.session.session_key

        products = SelectedProduct.objects.filter(session=session_key).order_by('id')

        if len(products) == 0:
            redirect('/basket/')

        form = CheckoutForm

        return render(request, 'delivering/checkout.html', context={'products': products, 'form': form})

    def post(self, request):

        form = CheckoutForm(request.POST)

        session_key = request.session.session_key

        selectedproducts = SelectedProduct.objects.filter(session=session_key).order_by('id')

        price = sum([x.total_price for x in selectedproducts])

        if form.is_valid():

            order = Order.objects.create(
                name=form.cleaned_data['name'],
                last_name=form.cleaned_data['last_name'],
                sure_name=form.cleaned_data['sure_name'],
                telephone=form.cleaned_data['telephone'],
                email=form.cleaned_data['email'],
                transporter=form.cleaned_data['transporter'],
                area=form.cleaned_data['area'],
                city=form.cleaned_data['city'],
                department=form.cleaned_data['department'],
                wish=form.cleaned_data['wish'],
                total_price=price,
                data=datetime.datetime.now()
            )

            print(order)

            for product in selectedproducts:

                BoughtProduct.objects.create(
                    session=session_key,
                    order=order,
                    product=product.product,
                    image=product.image,
                    name=product.name,
                    brand=product.brand,
                    description=product.description,
                    number=product.number,
                    price=product.price,
                    total_price=product.total_price
                )

            print(selectedproducts)

            for x in selectedproducts:
                print(x)
                x.delete()

            subject = 'Замовлення на крутому сайті'
            message = 'Ваше замовлення виглядає наступним чином:'
            recipient = form.cleaned_data['email']
            bought_products = BoughtProduct.objects.filter(session=session_key, order=order)
            html = render_to_string('delivering/order_message.html', {'order': order, 'bought_products': bought_products})
            send_mail(subject, message, EMAIL_HOST_USER, recipient_list=[recipient], fail_silently=False, html_message=html,)

        else:
            print(form.errors)

        return redirect('/')


def access_page(request):

    form = LoginForm

    return render(request, 'delivering/access.html', context={'form': form})


def access_form(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/')


def ajax_engine(request):
    if request.method == 'POST':

        data = request.POST

        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key

        if data['action'] == 'create':

            obj, create = SelectedProduct.objects.get_or_create(
                session=session_key,
                product=Product.objects.get(id=data['id']),
                unit_id=data['id'],
                image=data['image'],
                name=data['name'],
                brand=data['brand'],
                description=data['description'],
                defaults={'number': int(data['number'])},
                price=float(data['price']),
            )

            if create == False:

                obj.number = int(data['number'])
                obj.save()

        elif data['action'] == 'delete':

            SelectedProduct.objects.get(session=session_key, unit_id=data['id']).delete()

        elif data['action'] == 'change':

            product = SelectedProduct.objects.get(session=session_key, unit_id=data['id'])

            product.number = int(data['number'])

            product.save()

        products = SelectedProduct.objects.filter(session=session_key).order_by('id')

        try:
            keys = [field.verbose_name for field in products[0]._meta.fields]
        except IndexError:
            keys = []

        items = lambda x: [field.value_from_object(x) if field.verbose_name != 'image' else str(field.value_from_object(x)) for field in x._meta.fields]

        data = {product.name: dict(zip(keys, items(product))) for product in products}

        for key in data.keys():
            data[key].update({'url': Product.objects.get(name=key).get_absolute_url()})

        print(data)

        return JsonResponse(data)
