# Generated by Django 3.0.4 on 2020-04-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0028_auto_20200415_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedproduct',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
