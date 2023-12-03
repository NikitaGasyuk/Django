from django.urls import path,include
from . import views


urlpatterns = [
    path('start', views.index, name='home'),
    path('about', views.about, name='about'),
    
]