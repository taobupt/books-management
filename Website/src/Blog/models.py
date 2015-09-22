from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length = 16)
    permission = models.IntegerField()

    def __str__(self):
        return self.user.username

class Book(models.Model):
    name = models.CharField(max_length = 128)
    price = models.FloatField()
    author = models.CharField(max_length = 128)
    pubDate = models.DateField()
    typ = models.CharField(max_length = 128)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name

class Img(models.Model):
    name = models.CharField(max_length = 128)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'image')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name
# Create your models here.
