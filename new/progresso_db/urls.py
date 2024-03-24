from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path ('create/', views.addUser),  #to add user
    path ('validate/', views.validation),  #to send otp
    path ('otp/', views.otpveri),  #to verify otp
#     path ('read/<str:pk>', views.getUser),
#     path ('update/<str:pk>', views.updateUser),
#     path ('delete/<str:pk>', views.deleteUser),
]