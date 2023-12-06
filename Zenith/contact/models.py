from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    org = models.CharField(max_length=100)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

