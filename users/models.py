from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Users(AbstractUser):
    ADMIN = 'admin'
    MEMBER = 'membre'
    WEBMASTER = 'webmaster'
    STOCKER = 'stocker'
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MEMBER, 'Membre'),
        (WEBMASTER, 'Webmaster'),
        (STOCKER, 'Stocker'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Membre')
    avatar = models.URLField(max_length=500)
    def __str__(self):
        return self.username