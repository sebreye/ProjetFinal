from django.db import models

# Create your models here.
from django.db import models

class AboutUs(models.Model):
    location = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)  
    email = models.EmailField()
    fax = models.CharField(max_length=20)  


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()