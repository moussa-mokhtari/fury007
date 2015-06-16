#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user=models.OneToOneField(User)


class Phone(models.Model):
      number_phone= models.CharField(max_length=100)
      country_code= models.CharField(max_length=20)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at= models.DateTimeField(auto_now=True)
      owner=models.ForeignKey(Profile,related_name="phones")
      class Meta:
        ordering = ('created_at',)

class Address(models.Model):
      country= models.CharField(max_length=100)
      state=models.CharField(max_length=100)
      city=models.CharField(max_length=100)
      street=models.CharField(max_length=500)
      postal_code=models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at= models.DateTimeField(auto_now=True)
      owner=models.ForeignKey(Profile,related_name="addresses")
      class Meta:
        ordering = ('created_at',)