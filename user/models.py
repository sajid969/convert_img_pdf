from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class signup(models.Model):
        username=models.CharField(max_length=30)
        password=models.IntegerField()
        email=models.EmailField()
        first_name=models.CharField(max_length=30)
        last_name=models.CharField(max_length=30)

class filefield(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    choosefile=models.ImageField(null=True)
