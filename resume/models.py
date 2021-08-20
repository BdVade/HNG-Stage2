from django.db import models


# Create your models here.

class FeedBack(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField()
    needs = models.TextField(max_length=2000)
    message = models.TextField(max_length=2000)
