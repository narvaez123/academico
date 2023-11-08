from django.db import models
from django.utils import timezone
import datetime

class User(models.Model):
    email= models.CharField(max_length=100, null=False)
    password= models.CharField(max_length=500, null=False)
    status= models.BooleanField(null = True)
    created_at= models.DateTimeField(default=datetime.datetime.now, null = False)
    update_at=models.DateTimeField(default=datetime.datetime.now, null = False)
    deleted_at=models.DateField(null = True)
# Create your models here.

class Students(models.Model):
    code = models.CharField(max_length=50, null=False)
    id_person = models.IntegerField(null=False)
    status= models.BooleanField(null = True)
    created_at= models.DateTimeField(default=datetime.datetime.now, null = False)
    update_at=models.DateTimeField(default=datetime.datetime.now, null = False)
    deleted_at=models.DateField(null = True)


