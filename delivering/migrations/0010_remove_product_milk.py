# Generated by Django 3.0.4 on 2020-04-02 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0009_auto_20200402_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='milk',
        ),
    ]