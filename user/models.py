from typing import Match
from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
# Create your models here.

#Information for Staff
class Profile(models.Model):
    staff= models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    img = models.ImageField(default= 'avatar.jpg', upload_to='Profile_Images')


    def __str__(self):
        return f'{self.staff.username}-Profile'
