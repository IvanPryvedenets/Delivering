# Generated by Django 3.0.4 on 2020-04-17 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0033_auto_20200417_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectedproduct',
            name='total_price',
        ),
    ]