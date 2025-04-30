from django.urls import path
from . import views

# This tells Django which function to call for which URL

urlpatterns = [
    path('', views.home, name='home')
]