# Generated by Django 3.1.4 on 2021-01-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0005_auto_20210106_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
