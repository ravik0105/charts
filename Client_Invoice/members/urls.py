from django.urls import URLPattern, path
from .import views
from unicodedata import name



urlpatterns =[
path('',views.login_user,name='Home'),
path ('login',views.login_user,name="login"),
path ('logout',views.logout_user,name="logout"),


]