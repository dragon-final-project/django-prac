from django.db import models

# Create your models here.
class Character (models.Model):
    battleNet = models.CharField(max_length=12, primary_key=True)
    profession = models.CharField(max_length=10)
    level = models.IntegerField()

class Gift
    aim = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
