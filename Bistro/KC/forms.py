from django.contrib.auth.models import User
from django import forms

class userForm(forms.ModelForm):
	Password=forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields=['Name','email','Password']