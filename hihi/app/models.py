from django.db import models

# Create your models here.
class UploadPic(models.Model):
    user = models.CharField(max_length=30)

    pic_name = models.CharField(max_length=100)
    pic_desc = models.CharField(max_length=50, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
