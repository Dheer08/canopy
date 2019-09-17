from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.views.generic import View
from KC import *
from .models import *


# Create your views here.
def index(request):
	return render(request,'KC/index.html')

def MyAccount(request):
		return render(request,'KC/MyAccount.html')

def Myprofile(request):
		return render(request,'KC/Myprofile.html')

def MyOrders(request):
		return render(request,'KC/MyOrders.html')

def Aboutus(request):
		return render(request,'KC/Aboutus.html')

def Login(request):
	if request.method=='POST':
		print(request.POST.get('email'))
		return render(request,'KC/Login.html')
	else:
		return render(request,'KC/Login.html')



class UserFormView(View):
	from_class=UserForm
	template_name='KC/SignUp.html'

	def get(self,request):
		form=self.from_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():

			User=form.save(commit=False) 
			Name=form.cleaned_data['Name']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user=authenticate(Name=Name,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('KC:index')



