from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    organization = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    message = models.TextField()

# Create your models here.
