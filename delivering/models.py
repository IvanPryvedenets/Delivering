from django.db import models
from django.shortcuts import reverse


class Product(models.Model):

    CATEGORY_LIST = (
        ('Donuts', 'Donuts'),
        ('Waffles', 'Waffles'),
        ('Coffee', 'Coffee'),
    )

    slug = models.SlugField(max_length=500, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_LIST)
    image = models.ImageField()
    name = models.CharField(max_length=50)
    topping = models.CharField(max_length=50, blank=True)
    glaze = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500)
    amount = models.DecimalField(max_digits=1, decimal_places=1, null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def get_absolute_url(self):
        return reverse('product_url', kwargs={'slug': self.slug})

    def __str__(self):
        return 'Product: {}'.format(self.name)


class Comment(models.Model):
    session = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mark = models.IntegerField(blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    text = models.TextField()
    data = models.DateTimeField()
    audit = models.BooleanField(default=False)


class SelectedProduct(models.Model):
    session = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_id = models.IntegerField()
    image = models.ImageField()
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=1, decimal_places=1, null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    number = models.PositiveIntegerField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.number
        super(SelectedProduct, self).save(*args, **kwargs)


class Order(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sure_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    wish = models.TextField(max_length=500, blank=True)
    total_price = models.IntegerField()
    data = models.DateTimeField()
    status = models.BooleanField(default=False)


class BoughtProduct(models.Model):
    session = models.CharField(max_length=200)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    image = models.ImageField()
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=1, decimal_places=1, null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    number = models.PositiveIntegerField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
