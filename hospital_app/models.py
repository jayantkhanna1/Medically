from django.db import models
from datetime import datetime
# Create your models here.
class patient(models.Model):
    name=models.CharField(max_length=100)
    sex=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone=models.BigIntegerField()
    department=models.CharField(max_length=100)
    doc_seen=models.BooleanField(default=False)
    ailment=models.CharField(max_length=1000)
    prescription=models.CharField(max_length=1000)
    date_time=models.DateTimeField(default=datetime.now,auto_now=False, auto_now_add=False, blank=True)
class staff(models.Model):
    name=models.CharField(max_length=100)
    sex=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=600)
    can_delete=models.BooleanField(default=False)
    phone=models.BigIntegerField()
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    sex=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=600)
    can_delete=models.BooleanField(default=False)
    phone=models.BigIntegerField()