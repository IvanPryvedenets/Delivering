from .views import *
from django.urls import path

urlpatterns = [
    path('', MainPage.as_view(), name='main_url'),
    path('product/<str:slug>/', ProductPage.as_view(), name='product_url'),
    path('basket/', BasketPage.as_view(), name='basket_url'),
    path('checkout/', CheckoutPage.as_view(), name='checkout_url'),

    path('comment_timerpage/', comment_sec, name='comment_sec_url'),

    path('access/', access_page),
    path('access/<str:link>/', access_form, name='access_form'),

    path('ajaxengine/', ajax_engine, name='ajax_engine'),
]
