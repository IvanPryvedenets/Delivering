# Generated by Django 3.0.4 on 2020-04-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0008_remove_product_coffee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='milk',
            field=models.CharField(blank=True, choices=[('З солоком', 'З солоком'), ('Без молока', 'Без молока')], max_length=20),
        ),
    ]
