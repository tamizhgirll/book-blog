# Generated by Django 4.2.3 on 2023-07-05 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments_books_image_alter_books_pages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='ratings',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
