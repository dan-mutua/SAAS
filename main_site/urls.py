from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
  path('', include('main.urls')),  
  path('admin/', admin.site.urls),
  path("stripe/", include("djstripe.urls", namespace="djstripe")), #add this
]