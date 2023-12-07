from django.db import models

# Create your models here.

class Properties(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    

class Users(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=10)