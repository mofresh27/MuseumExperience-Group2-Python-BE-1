from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('register/visitor', views.visitor_register.as_view(), name='visitor_register'),
    path('register/staff', views.staff_register.as_view(), name='staff_register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]  
