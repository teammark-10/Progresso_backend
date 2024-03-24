from django.urls import path
from . import views

urlpatterns = [
     path('', views.getAllEvent),
     path('hello/', views.hello_world,name='hello_world'),
     path('create/', views.addEvent),
     path('update/<str:tag>', views.updateEvent),
     path('delete/<str:tag>', views.deleteEvent),
     path('events/<str:tag>', views.getEvent),
]
