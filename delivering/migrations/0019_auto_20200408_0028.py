# Generated by Django 3.0.4 on 2020-04-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0018_auto_20200408_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=500, unique=True),
        ),
    ]