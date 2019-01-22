# Generated by Django 2.0.2 on 2019-01-15 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='votes_total',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hunter',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
        migrations.AddField(
            model_name='product',
            name='from_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='stockid',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='to_date',
            field=models.DateTimeField(default=None),
        ),
    ]
