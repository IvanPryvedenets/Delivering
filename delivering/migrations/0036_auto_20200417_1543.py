# Generated by Django 3.0.4 on 2020-04-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0035_auto_20200417_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedproduct',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='selectedproduct',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]