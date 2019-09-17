from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='home'),
	path('Aboutus',views.Aboutus,name='Aboutus'),
	path('MyAccount',views.MyAccount,name='MyAccount'),
	path('MyOrders',views.MyOrders,name='MyOrders'),
	path('Myprofile',views.Myprofile,name='Myprofile'),
	path('Login',views.UserFromView.as_view(),name='Login'),
	path('Sign Up',views.SignUp,name='SignUp')
    
]