# Generated by Django 3.0.4 on 2020-04-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0039_auto_20200419_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedproduct',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
    ]
