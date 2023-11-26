from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rating = models.IntegerField(default=5)
#     # note: The SQLLite database is included when we created a Django Project!


class Register(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    uid = models.CharField(max_length=25, unique=True)
