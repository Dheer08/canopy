from django.db import models
from django import forms
# Create your models here.

class customer(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	order=models.CharField(max_length=30)
	order_status=models.CharField(max_length=30,default="Processing")

	def __str__(self):
		return (self.first_name+" "+self.last_name)

class UserForm(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)
	password=models.CharField(max_length=30,default="Processing")

	def __str__(self):
		return (self.first_name+" "+self.last_name)