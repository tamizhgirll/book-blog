# Generated by Django 4.2.3 on 2023-07-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_books_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='static/media/'),
        ),
    ]
