
from django.db import models

# Create your models here.
class Menu(models.Model):
    user_name = models.CharField(default='',max_length=50)
    user_email = models.CharField(default='',max_length=50)
    price = models.IntegerField()
    menu = models.CharField(default='',max_length=50)


class Event(models.Model):
    user_name = models.CharField(default='',max_length=50)
    event_type= models.CharField(default='',max_length=50)
    capacity= models.IntegerField()


    def __str__(self):
        return self.user_name


class Vendor(models.Model):
    vendor_name = models.CharField(default='',max_length=50)
    vendor_password = models.CharField(default='',max_length=50)
    address = models.CharField(default='',max_length=50)
    mobileno = models.IntegerField()

    def __str__(self):
        return self.vendor_name

class Package(models.Model):
     package_name = models.CharField(default='',max_length=50)
     price = models.IntegerField()
     dis= models.CharField(default='',max_length=50)

class Customer(models.Model):
     name = models.CharField(default='',max_length=50)
     email= models.CharField(default='',max_length=50)
     price= models.IntegerField()
     suggesst=models.CharField(default='',max_length=100)
