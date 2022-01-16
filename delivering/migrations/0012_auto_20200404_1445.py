# Generated by Django 3.0.4 on 2020-04-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0011_selectedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='desc', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='selectedproduct',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='selectedproduct',
            name='name',
            field=models.CharField(default='name', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selectedproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='selectedproduct',
            name='total_price',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='selectedproduct',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]