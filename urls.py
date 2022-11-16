# urls.py

from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('rfc/', views.registration, name='rfc'),
    path('course/', views.course, name='course'),

]
