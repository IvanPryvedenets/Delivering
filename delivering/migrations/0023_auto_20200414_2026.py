# Generated by Django 3.0.4 on 2020-04-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivering', '0022_auto_20200408_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectedproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='selectedproduct',
            name='unit_id',
            field=models.IntegerField(default=39),
            preserve_default=False,
        ),
    ]