from django.db import models

# Create your models here.
class background_index(models.Model):
    backimage = models.URLField()

class background2(models.Model):
    background = models.URLField()