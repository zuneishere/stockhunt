# Generated by Django 2.0.2 on 2019-01-15 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190115_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='icon',
        ),
    ]