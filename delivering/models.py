from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


# категорія продукту
class Category(models.Model):
    field = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    slug = models.SlugField(max_length=500, unique=True)

    def get_absolute_url(self):
        return reverse('category_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.field)


class Product(models.Model):

    STATUS = (
        ('В наявності', 'В наявності'),
        ('Товар відсутный', 'Товар відсутный')
    )

    slug = models.SlugField(max_length=500, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500)
    status = models.CharField(choices=STATUS, max_length=50)
    old_price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
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
    brand = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500)
    number = models.PositiveIntegerField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.number
        super(SelectedProduct, self).save(*args, **kwargs)


class Order(models.Model):

    STATUS = (
        ('В роботі', 'В роботі'),
        ('Опрацьовано', 'Опрацьовано')
    )

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sure_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    transporter = models.CharField(max_length=15)
    area = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    department = models.CharField(max_length=40)
    wish = models.TextField(max_length=500, blank=True)
    total_price = models.IntegerField()
    data = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} - {}'.format(self.name, self.last_name, self.email)


class BoughtProduct(models.Model):
    session = models.CharField(max_length=200)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    image = models.ImageField()
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=500)
    number = models.PositiveIntegerField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
