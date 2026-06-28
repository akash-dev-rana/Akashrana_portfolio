from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    desc = models.TextField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return  self.name;
