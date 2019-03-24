from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.name


class cycle(models.Model):
    BILLING_TYPE = (
        ('DAILY', 'DAILY'),
        ('WEEKLY', 'WEEKLY'),
        ('MONTHLY', 'MONTHLY'),
        ('ANNUALLY', 'ANNUALLY'),
    )
    type = models.CharField(max_length=120, blank=True,
                            choices=BILLING_TYPE)
    price = models.CharField(max_length=120, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=120,default="NO")
    item = models.TextField(blank=True, null=True)
    created = models.DateField(max_length=30, blank=True, null=True)

    def __str__(self):
        return "{0} - {1}".format(self.user.name, self.type)


class service(models.Model):
    item = models.CharField(max_length=120,blank=True,null=True)

    def __str__(self):
        return '%s' % self.item
