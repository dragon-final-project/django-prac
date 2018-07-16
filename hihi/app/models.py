from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    intro = models.CharField(max_length=100)

class Store(models.Model):
    name = models.CharField(max_length=100)
    # owner = models.ForeignKey(Person, on_delete=)

# models.py > migrations > migrate to db
#                             ALTER TABLE

class Norman(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.BooleanField()
    phone_number = models.DecimalField(max_digits=10,decimal_places=0)
