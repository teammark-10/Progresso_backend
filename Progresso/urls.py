from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include('djangoapp.urls')),
    path("proggresso/", include('EventMaker.urls')),
]
