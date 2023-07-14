# Generated by Django 4.2.3 on 2023-07-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_books_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('bookName', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
