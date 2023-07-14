from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Books(models.Model):
    bookName = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    pages = models.IntegerField(blank=True)
    ratings = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.TextField()
    image = models.ImageField(upload_to="", default="")

    def __str__(self):
        return self.bookName

class Recommendations(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    bookName = models.CharField(max_length=255)
    author = models.CharField(max_length=25)